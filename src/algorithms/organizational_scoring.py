"""
Organizational Scoring Module
==============================

Comprehensive scoring system for organizational excellence assessment
integrating ADLI-LeTCI framework with gap analysis and integration health metrics.

Authors:
    Rungtiva Saosing, Chatchai Tritham, Chattabhorn Tritham, Sudasawan Ngammongkolwong
    Faculty of Science and Technology, Rajamangala University of Technology Krungthep

Reference:
    Saosing et al. (2026). From Excellence Guidelines to Computable Performance Systems.
    IEEE ACCESS.
"""

from typing import Dict, List, Optional, Tuple
import numpy as np
import pandas as pd
from dataclasses import dataclass
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CategoryType(Enum):
    """BEB-EdPEx category types."""
    LEADERSHIP = 1
    STRATEGY = 2
    CUSTOMERS = 3
    MEASUREMENT = 4
    WORKFORCE = 5
    OPERATIONS = 6
    RESULTS = 7


@dataclass
class ScoreResult:
    """Score result with metadata."""
    score: float
    category: int
    item: Optional[int]
    breakdown: Dict[str, float]
    confidence: float = 1.0
    metadata: Optional[Dict] = None


class OrganizationalScorer:
    """
    Comprehensive organizational scoring engine.

    Integrates ADLI scoring for process categories (1-6) and LeTCI scoring
    for results category (7) with organizational-level aggregation.
    """

    # Default category weights (balanced)
    DEFAULT_CATEGORY_WEIGHTS = {
        1: 1/7,  # Leadership
        2: 1/7,  # Strategy
        3: 1/7,  # Customers
        4: 1/7,  # Measurement
        5: 1/7,  # Workforce
        6: 1/7,  # Operations
        7: 1/7   # Results
    }

    # Integration dependencies (category relationships)
    INTEGRATION_EDGES = [
        (1, 2),  # Leadership → Strategy
        (2, 5),  # Strategy → Workforce
        (2, 6),  # Strategy → Operations
        (5, 4),  # Workforce → Measurement
        (6, 4),  # Operations → Measurement
        (4, 7)   # Measurement → Results
    ]

    def __init__(
        self,
        category_weights: Optional[Dict[int, float]] = None,
        adli_weights: Optional[Dict[str, float]] = None,
        letci_weights: Optional[Dict[str, float]] = None
    ):
        """
        Initialize organizational scorer.

        Args:
            category_weights: Custom weights for 7 categories
            adli_weights: Custom ADLI weights
            letci_weights: Custom LeTCI weights
        """
        self.category_weights = category_weights or self.DEFAULT_CATEGORY_WEIGHTS.copy()

        # Import scorers
        from .adli_scoring import ADLIScorer
        from .letci_scoring import LeTCIScorer

        self.adli_scorer = ADLIScorer(adli_weights)
        self.letci_scorer = LeTCIScorer(letci_weights)

        self._validate_category_weights()

        logger.info("OrganizationalScorer initialized successfully")

    def _validate_category_weights(self):
        """Validate category weights sum to 1.0."""
        weight_sum = sum(self.category_weights.values())
        if not np.isclose(weight_sum, 1.0, atol=1e-6):
            raise ValueError(f"Category weights must sum to 1.0, got {weight_sum}")

    def compute_item_score(
        self,
        category: int,
        item_id: int,
        indicators: Dict[str, float]
    ) -> ScoreResult:
        """
        Compute score for a single item.

        Args:
            category: Category number (1-7)
            item_id: Item identifier
            indicators: Normalized indicators [0,1]

        Returns:
            ScoreResult with score, breakdown, and metadata
        """
        if not 1 <= category <= 7:
            raise ValueError(f"Category must be 1-7, got {category}")

        try:
            if category <= 6:
                # Process category - use ADLI
                score = self.adli_scorer.compute_score(indicators)
                breakdown = self.adli_scorer.get_diagnostic_breakdown(indicators)
            else:
                # Results category - use LeTCI
                score = self.letci_scorer.compute_score(indicators)
                breakdown = self.letci_scorer.get_diagnostic_breakdown(indicators)

            return ScoreResult(
                score=score,
                category=category,
                item=item_id,
                breakdown=breakdown,
                confidence=self._compute_confidence(indicators),
                metadata={'method': 'ADLI' if category <= 6 else 'LeTCI'}
            )

        except Exception as e:
            logger.error(f"Error computing item score: {e}")
            raise

    def compute_category_score(
        self,
        category: int,
        item_scores: Dict[int, float],
        item_weights: Optional[Dict[int, float]] = None
    ) -> ScoreResult:
        """
        Aggregate item scores to category score.

        Args:
            category: Category number (1-7)
            item_scores: Dict of {item_id: score}
            item_weights: Optional item weights

        Returns:
            ScoreResult for category
        """
        if not item_scores:
            raise ValueError("item_scores cannot be empty")

        # Use ADLI or LeTCI scorer for aggregation
        scorer = self.adli_scorer if category <= 6 else self.letci_scorer
        category_score = scorer.compute_category_score(item_scores, item_weights)

        return ScoreResult(
            score=category_score,
            category=category,
            item=None,
            breakdown={'items': item_scores},
            confidence=np.mean([1.0] * len(item_scores))  # Simplified
        )

    def compute_organizational_score(
        self,
        category_scores: Dict[int, float]
    ) -> ScoreResult:
        """
        Compute organization-wide score from category scores.

        Args:
            category_scores: Dict of {category: score}

        Returns:
            ScoreResult for organization
        """
        if len(category_scores) != 7:
            logger.warning(f"Expected 7 categories, got {len(category_scores)}")

        org_score = sum(
            self.category_weights[cat] * score
            for cat, score in category_scores.items()
        )

        return ScoreResult(
            score=round(org_score, 2),
            category=0,  # Organization level
            item=None,
            breakdown=category_scores,
            confidence=self._compute_org_confidence(category_scores)
        )

    def compute_integration_health_index(
        self,
        category_scores: Dict[int, float]
    ) -> float:
        """
        Compute Integration Health Index (IHI) measuring cross-category coherence.

        Args:
            category_scores: Dict of {category: score}

        Returns:
            IHI score in [0, 1], where 1.0 = perfect alignment
        """
        coherences = []

        for source, target in self.INTEGRATION_EDGES:
            if source in category_scores and target in category_scores:
                # Edge coherence = 1 - |score_diff| / 100
                coherence = 1.0 - abs(
                    category_scores[source] - category_scores[target]
                ) / 100.0
                coherences.append(coherence)

        return np.mean(coherences) if coherences else 0.0

    def compute_gap_analysis(
        self,
        current_scores: Dict[int, Dict[int, float]],
        target_scores: Dict[int, Dict[int, float]],
        criticality: Optional[Dict[Tuple[int, int], float]] = None,
        risk: Optional[Dict[Tuple[int, int], float]] = None
    ) -> pd.DataFrame:
        """
        Compute gap analysis with prioritization.

        Args:
            current_scores: {category: {item: score}}
            target_scores: {category: {item: target}}
            criticality: Optional criticality weights [0,1]
            risk: Optional risk factors [0,1]

        Returns:
            DataFrame with gap analysis results
        """
        gaps = []

        for category, items in current_scores.items():
            for item, current in items.items():
                target = target_scores.get(category, {}).get(item, 100.0)
                gap = max(0, target - current)

                # Default criticality and risk
                crit = criticality.get((category, item), 0.5) if criticality else 0.5
                risk_val = risk.get((category, item), 0.5) if risk else 0.5

                priority = gap * crit * risk_val

                gaps.append({
                    'category': category,
                    'item': item,
                    'current_score': current,
                    'target_score': target,
                    'gap': gap,
                    'criticality': crit,
                    'risk': risk_val,
                    'priority': priority,
                    'status': 'Critical' if gap > 20 else 'Monitor' if gap > 10 else 'On Track'
                })

        df = pd.DataFrame(gaps)
        return df.sort_values('priority', ascending=False).reset_index(drop=True)

    def _compute_confidence(self, indicators: Dict[str, float]) -> float:
        """Compute confidence score based on indicator variance."""
        values = list(indicators.values())
        variance = np.var(values)
        # Lower variance = higher confidence
        return 1.0 - min(variance, 1.0)

    def _compute_org_confidence(self, category_scores: Dict[int, float]) -> float:
        """Compute organizational confidence score."""
        values = list(category_scores.values())
        variance = np.var(values)
        return 1.0 - min(variance / 1000, 1.0)  # Scale for 0-100 scores

    def generate_scorecard(
        self,
        category_scores: Dict[int, float],
        include_ihi: bool = True
    ) -> Dict:
        """
        Generate comprehensive organizational scorecard.

        Args:
            category_scores: Dict of {category: score}
            include_ihi: Include Integration Health Index

        Returns:
            Comprehensive scorecard dictionary
        """
        org_result = self.compute_organizational_score(category_scores)

        scorecard = {
            'organizational_score': org_result.score,
            'confidence': org_result.confidence,
            'category_scores': category_scores,
            'category_names': {
                1: 'Leadership',
                2: 'Strategy',
                3: 'Customers',
                4: 'Measurement',
                5: 'Workforce',
                6: 'Operations',
                7: 'Results'
            }
        }

        if include_ihi:
            ihi = self.compute_integration_health_index(category_scores)
            scorecard['integration_health_index'] = round(ihi, 3)
            scorecard['ihi_interpretation'] = self._interpret_ihi(ihi)

        # Add maturity level
        scorecard['maturity_level'] = self._compute_maturity_level(org_result.score)

        return scorecard

    def _interpret_ihi(self, ihi: float) -> str:
        """Interpret IHI value."""
        if ihi >= 0.9:
            return "Excellent - Strong cross-category alignment"
        elif ihi >= 0.8:
            return "Good - Moderate alignment with minor gaps"
        elif ihi >= 0.7:
            return "Fair - Some alignment issues need attention"
        else:
            return "Poor - Significant alignment gaps require intervention"

    def _compute_maturity_level(self, score: float) -> str:
        """Compute organizational maturity level."""
        if score >= 90:
            return "Advanced - World-class performance"
        elif score >= 75:
            return "Mature - Strong systematic approach"
        elif score >= 60:
            return "Developing - Early systematic approach"
        elif score >= 40:
            return "Emerging - Beginning systematic approach"
        else:
            return "Initial - Reactive approach"


def create_sample_organization_data() -> Dict:
    """
    Create sample organizational assessment data for demonstration.

    Returns:
        Dict with sample category and item scores
    """
    return {
        'categories': {
            1: {'items': {1: 75, 2: 72, 3: 78}, 'weight': 1/7},
            2: {'items': {1: 65, 2: 59, 3: 70}, 'weight': 1/7},
            3: {'items': {1: 80, 2: 85, 3: 82}, 'weight': 1/7},
            4: {'items': {1: 68, 2: 72, 3: 70}, 'weight': 1/7},
            5: {'items': {1: 74, 2: 76, 3: 75}, 'weight': 1/7},
            6: {'items': {1: 69, 2: 71, 3: 68}, 'weight': 1/7},
            7: {'items': {1: 88, 2: 85, 3: 90}, 'weight': 1/7}
        },
        'organization_name': 'Sample University',
        'assessment_period': '2024-2025'
    }


if __name__ == "__main__":
    # Demonstration
    print("Organizational Scoring System")
    print("=" * 60)

    scorer = OrganizationalScorer()

    # Sample data
    sample_data = create_sample_organization_data()

    # Compute category scores
    category_scores = {}
    for cat_id, cat_data in sample_data['categories'].items():
        cat_score = np.mean(list(cat_data['items'].values()))
        category_scores[cat_id] = round(cat_score, 2)

    # Generate scorecard
    scorecard = scorer.generate_scorecard(category_scores)

    print(f"\nOrganization: {sample_data['organization_name']}")
    print(f"Period: {sample_data['assessment_period']}")
    print(f"\nOrganizational Score: {scorecard['organizational_score']}")
    print(f"Maturity Level: {scorecard['maturity_level']}")
    print(f"Integration Health Index: {scorecard['integration_health_index']}")
    print(f"IHI Interpretation: {scorecard['ihi_interpretation']}")

    print(f"\nCategory Scores:")
    for cat_id, score in scorecard['category_scores'].items():
        cat_name = scorecard['category_names'][cat_id]
        print(f"  {cat_id}. {cat_name:15s}: {score:5.1f}")
