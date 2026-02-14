"""
Comprehensive tests for the OrganizationalScorer module.

Tests validate all core algorithms:
- ADLI process scoring
- LeTCI results scoring
- Organizational-level aggregation
- Integration Health Index (IHI)
- Gap analysis and prioritization
- Scorecard generation
"""

import pytest
import numpy as np
import pandas as pd
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from algorithms.organizational_scoring import OrganizationalScorer, ScoreResult


class TestADLIScoring:
    """Tests for ADLI (Approach-Deployment-Learning-Integration) scoring."""

    def setup_method(self):
        self.scorer = OrganizationalScorer()

    def test_adli_perfect_score(self):
        """All indicators at 1.0 should yield 100."""
        result = self.scorer.compute_item_score(
            category=1, item_id=1,
            indicators={'P_A': 1.0, 'P_D': 1.0, 'P_L': 1.0, 'P_I': 1.0}
        )
        assert result.score == pytest.approx(100.0, abs=0.1)

    def test_adli_zero_score(self):
        """All indicators at 0.0 should yield 0."""
        result = self.scorer.compute_item_score(
            category=1, item_id=1,
            indicators={'P_A': 0.0, 'P_D': 0.0, 'P_L': 0.0, 'P_I': 0.0}
        )
        assert result.score == pytest.approx(0.0, abs=0.1)

    def test_adli_weighted_calculation(self):
        """Validate ADLI weighted calculation: A=30%, D=30%, L=20%, I=20%."""
        result = self.scorer.compute_item_score(
            category=2, item_id=3,
            indicators={'P_A': 0.75, 'P_D': 0.45, 'P_L': 0.60, 'P_I': 0.55}
        )
        expected = 0.75 * 30 + 0.45 * 30 + 0.60 * 20 + 0.55 * 20
        assert result.score == pytest.approx(expected, abs=0.1)

    def test_adli_score_bounds(self):
        """All ADLI scores should be in [0, 100]."""
        for a, d, l, i in [(0.3, 0.5, 0.7, 0.2), (0.9, 0.8, 0.7, 0.6)]:
            result = self.scorer.compute_item_score(
                category=1, item_id=1,
                indicators={'P_A': a, 'P_D': d, 'P_L': l, 'P_I': i}
            )
            assert 0 <= result.score <= 100

    def test_adli_returns_scoreresult(self):
        """Return type should be ScoreResult."""
        result = self.scorer.compute_item_score(
            category=1, item_id=1,
            indicators={'P_A': 0.7, 'P_D': 0.6, 'P_L': 0.5, 'P_I': 0.5}
        )
        assert isinstance(result, ScoreResult)
        assert result.category == 1
        assert result.item == 1

    def test_adli_breakdown_present(self):
        """ScoreResult should include dimensional breakdown."""
        result = self.scorer.compute_item_score(
            category=1, item_id=1,
            indicators={'P_A': 0.7, 'P_D': 0.6, 'P_L': 0.5, 'P_I': 0.5}
        )
        assert isinstance(result.breakdown, dict)
        assert len(result.breakdown) > 0


class TestLeTCIScoring:
    """Tests for LeTCI (Levels-Trends-Comparisons-Integration) scoring."""

    def setup_method(self):
        self.scorer = OrganizationalScorer()

    def test_letci_perfect_score(self):
        """All LeTCI indicators at 1.0 should yield 100."""
        result = self.scorer.compute_item_score(
            category=7, item_id=1,
            indicators={'R_Lv': 1.0, 'R_Tr': 1.0, 'R_Cp': 1.0, 'R_I': 1.0}
        )
        assert result.score == pytest.approx(100.0, abs=0.1)

    def test_letci_weighted_calculation(self):
        """Validate LeTCI weights: Lv=35%, Tr=25%, Cp=25%, I=15%."""
        result = self.scorer.compute_item_score(
            category=7, item_id=1,
            indicators={'R_Lv': 0.85, 'R_Tr': 0.90, 'R_Cp': 0.75, 'R_I': 0.70}
        )
        expected = 0.85 * 35 + 0.90 * 25 + 0.75 * 25 + 0.70 * 15
        assert result.score == pytest.approx(expected, abs=0.1)

    def test_letci_category_7(self):
        """Category 7 should use LeTCI scoring."""
        result = self.scorer.compute_item_score(
            category=7, item_id=1,
            indicators={'R_Lv': 0.8, 'R_Tr': 0.7, 'R_Cp': 0.6, 'R_I': 0.5}
        )
        expected = 0.8 * 35 + 0.7 * 25 + 0.6 * 25 + 0.5 * 15
        assert result.score == pytest.approx(expected, abs=0.1)


class TestOrganizationalScoring:
    """Tests for organizational-level scoring aggregation."""

    def setup_method(self):
        self.scorer = OrganizationalScorer()
        self.sample_scores = {
            1: 75.0, 2: 65.0, 3: 82.0, 4: 70.0,
            5: 75.0, 6: 70.0, 7: 78.0
        }

    def test_org_score_returns_scoreresult(self):
        """Organizational score should return ScoreResult."""
        result = self.scorer.compute_organizational_score(self.sample_scores)
        assert isinstance(result, ScoreResult)

    def test_org_score_is_weighted_average(self):
        """Organizational score should be weighted average of categories."""
        result = self.scorer.compute_organizational_score(self.sample_scores)
        manual = sum(
            self.scorer.category_weights[cat] * score
            for cat, score in self.sample_scores.items()
        )
        assert result.score == pytest.approx(manual, abs=0.1)

    def test_org_score_bounds(self):
        """Organizational score should be in [0, 100]."""
        result = self.scorer.compute_organizational_score(self.sample_scores)
        assert 0 <= result.score <= 100

    def test_org_confidence_bounds(self):
        """Confidence should be in [0, 1]."""
        result = self.scorer.compute_organizational_score(self.sample_scores)
        assert 0 <= result.confidence <= 1

    def test_category_weights_sum_to_one(self):
        """Category weights should sum to 1.0."""
        total = sum(self.scorer.category_weights.values())
        assert total == pytest.approx(1.0, abs=0.001)


class TestIntegrationHealthIndex:
    """Tests for Integration Health Index (IHI) calculation."""

    def setup_method(self):
        self.scorer = OrganizationalScorer()

    def test_ihi_perfect_alignment(self):
        """Identical scores should yield IHI close to 1.0."""
        scores = {cid: 75.0 for cid in range(1, 8)}
        ihi = self.scorer.compute_integration_health_index(scores)
        assert ihi == pytest.approx(1.0, abs=0.01)

    def test_ihi_bounds(self):
        """IHI should always be in [0, 1]."""
        for scores in [
            {1: 80, 2: 60, 3: 90, 4: 40, 5: 70, 6: 50, 7: 85},
            {1: 50, 2: 50, 3: 50, 4: 50, 5: 50, 6: 50, 7: 50}
        ]:
            ihi = self.scorer.compute_integration_health_index(scores)
            assert 0 <= ihi <= 1

    def test_ihi_decreases_with_variance(self):
        """Higher variance across categories should lower IHI."""
        low_variance  = {cid: 75.0 for cid in range(1, 8)}
        high_variance = {1: 40, 2: 90, 3: 40, 4: 90, 5: 40, 6: 90, 7: 65}
        ihi_low  = self.scorer.compute_integration_health_index(low_variance)
        ihi_high = self.scorer.compute_integration_health_index(high_variance)
        assert ihi_low > ihi_high


class TestGapAnalysis:
    """Tests for gap analysis and prioritization."""

    def setup_method(self):
        self.scorer = OrganizationalScorer()
        self.current = {1: {1: 70, 2: 75}, 2: {1: 60, 2: 65}}
        self.targets = {1: {1: 85, 2: 85}, 2: {1: 80, 2: 80}}

    def test_gap_returns_dataframe(self):
        """Gap analysis should return a DataFrame."""
        result = self.scorer.compute_gap_analysis(self.current, self.targets)
        assert isinstance(result, pd.DataFrame)

    def test_gap_correct_columns(self):
        """Gap DataFrame should have required columns."""
        result = self.scorer.compute_gap_analysis(self.current, self.targets)
        required = {'category', 'item', 'current_score', 'target_score', 'gap', 'priority'}
        assert required.issubset(set(result.columns))

    def test_gap_values_non_negative(self):
        """Gap values should be non-negative."""
        result = self.scorer.compute_gap_analysis(self.current, self.targets)
        assert (result['gap'] >= 0).all()

    def test_gap_sorted_by_priority(self):
        """Results should be sorted by priority (descending)."""
        result = self.scorer.compute_gap_analysis(self.current, self.targets)
        assert list(result['priority']) == sorted(result['priority'], reverse=True)

    def test_gap_correct_calculation(self):
        """Gap should equal target minus current."""
        result = self.scorer.compute_gap_analysis(self.current, self.targets)
        for _, row in result.iterrows():
            expected_gap = max(0, row['target_score'] - row['current_score'])
            assert row['gap'] == pytest.approx(expected_gap, abs=0.01)

    def test_gap_status_classification(self):
        """Status should be correctly classified."""
        result = self.scorer.compute_gap_analysis(self.current, self.targets)
        for _, row in result.iterrows():
            if row['gap'] > 20:
                assert row['status'] == 'Critical'
            elif row['gap'] > 10:
                assert row['status'] == 'Monitor'
            else:
                assert row['status'] == 'On Track'


class TestScorecardGeneration:
    """Tests for scorecard generation."""

    def setup_method(self):
        self.scorer = OrganizationalScorer()
        self.scores = {1: 75, 2: 65, 3: 82, 4: 70, 5: 75, 6: 70, 7: 78}

    def test_scorecard_returns_dict(self):
        """Scorecard should return a dictionary."""
        result = self.scorer.generate_scorecard(self.scores)
        assert isinstance(result, dict)

    def test_scorecard_has_org_score(self):
        """Scorecard should include organizational score."""
        result = self.scorer.generate_scorecard(self.scores)
        assert 'organizational_score' in result

    def test_scorecard_with_ihi(self):
        """Scorecard with IHI flag should include IHI."""
        result = self.scorer.generate_scorecard(self.scores, include_ihi=True)
        assert 'integration_health_index' in result
        assert 0 <= result['integration_health_index'] <= 1

    def test_scorecard_maturity_level(self):
        """Scorecard should include maturity level."""
        result = self.scorer.generate_scorecard(self.scores)
        assert 'maturity_level' in result
        assert isinstance(result['maturity_level'], str)


class TestMaturityLevels:
    """Tests for maturity level classification."""

    def setup_method(self):
        self.scorer = OrganizationalScorer()

    def test_world_class(self):
        """Score >= 90 should be world-class."""
        level = self.scorer._compute_maturity_level(95)
        assert 'Advanced' in level or 'world-class' in level.lower() or 'World' in level

    def test_low_score(self):
        """Low score should not be high-maturity."""
        level = self.scorer._compute_maturity_level(30)
        assert 'World' not in level and 'Advanced' not in level

    def test_all_thresholds(self):
        """All scores [0-100] should return a non-empty string."""
        for score in range(0, 101, 10):
            level = self.scorer._compute_maturity_level(score)
            assert isinstance(level, str)
            assert len(level) > 0


class TestDataValidation:
    """Tests for input validation and edge cases."""

    def setup_method(self):
        self.scorer = OrganizationalScorer()

    def test_single_category_scores(self):
        """Should handle partial category input gracefully."""
        scores = {7: 80.0}
        result = self.scorer.compute_organizational_score(scores)
        assert isinstance(result, ScoreResult)
        assert result.score >= 0

    def test_empty_gap_analysis(self):
        """Empty input should return empty DataFrame."""
        result = self.scorer.compute_gap_analysis({}, {})
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
