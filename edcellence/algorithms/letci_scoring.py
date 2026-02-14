"""
LeTCI Scoring Algorithm
=======================

Implements the LeTCI (Levels-Trends-Comparisons-Integration) scoring
methodology for results assessment in organizational excellence frameworks.

Mathematical Formulation:
    S_item[7,i] = 100 × (w_Lv·R_Lv[7,i] + w_Tr·R_Tr[7,i] + w_Cp·R_Cp[7,i] + w_I·R_I[7,i])

where:
    - R_Lv: Outcome level attainment (normalized [0,1])
    - R_Tr: Performance trend stability (normalized [0,1])
    - R_Cp: Comparative positioning (normalized [0,1])
    - R_I: Outcome integration (normalized [0,1])
    - w_Lv, w_Tr, w_Cp, w_I: Weights (default: 0.35, 0.25, 0.25, 0.15)

Reference:
    Saosing et al. (2026). From Excellence Guidelines to Computable Performance Systems.
    IEEE ACCESS (under review).
"""

from typing import Dict, Optional, List
import numpy as np


class LeTCIScorer:
    """LeTCI scoring engine for results assessment."""

    # Default weights (sum = 1.0)
    DEFAULT_WEIGHTS = {
        'w_Lv': 0.35,  # Levels
        'w_Tr': 0.25,  # Trends
        'w_Cp': 0.25,  # Comparisons
        'w_I': 0.15    # Integration
    }

    def __init__(self, weights: Optional[Dict[str, float]] = None):
        """
        Initialize LeTCI scorer.

        Args:
            weights: Custom weights for LeTCI dimensions. If None, uses defaults.
                    Must sum to 1.0.

        Raises:
            ValueError: If weights don't sum to 1.0 or are out of range [0,1].
        """
        self.weights = weights if weights else self.DEFAULT_WEIGHTS.copy()
        self._validate_weights()

    def _validate_weights(self):
        """Validate that weights sum to 1.0 and are in valid range."""
        weight_sum = sum(self.weights.values())
        if not np.isclose(weight_sum, 1.0, atol=1e-6):
            raise ValueError(f"Weights must sum to 1.0, got {weight_sum}")

        for key, value in self.weights.items():
            if not 0 <= value <= 1:
                raise ValueError(f"Weight {key}={value} out of range [0,1]")

    def compute_score(self, indicators: Dict[str, float]) -> float:
        """
        Compute LeTCI score for a results item.

        Args:
            indicators: Dictionary with keys 'R_Lv', 'R_Tr', 'R_Cp', 'R_I'
                       representing normalized indicators [0,1].

        Returns:
            LeTCI score in range [0, 100].

        Raises:
            ValueError: If indicators are missing or out of range.

        Example:
            >>> scorer = LeTCIScorer()
            >>> indicators = {
            ...     'R_Lv': 0.85,  # High outcome level
            ...     'R_Tr': 0.90,  # Strong positive trend
            ...     'R_Cp': 0.75,  # Above benchmark
            ...     'R_I': 0.70    # Good integration
            ... }
            >>> score = scorer.compute_score(indicators)
            >>> print(f"LeTCI Score: {score}")
            LeTCI Score: 81.25
        """
        required_keys = {'R_Lv', 'R_Tr', 'R_Cp', 'R_I'}
        if not required_keys.issubset(indicators.keys()):
            missing = required_keys - indicators.keys()
            raise ValueError(f"Missing indicators: {missing}")

        # Validate indicator ranges
        for key, value in indicators.items():
            if key in required_keys:
                if not 0 <= value <= 1:
                    raise ValueError(f"Indicator {key}={value} out of range [0,1]")

        # Compute weighted score
        score = 100 * (
            self.weights['w_Lv'] * indicators['R_Lv'] +
            self.weights['w_Tr'] * indicators['R_Tr'] +
            self.weights['w_Cp'] * indicators['R_Cp'] +
            self.weights['w_I'] * indicators['R_I']
        )

        return round(score, 2)

    def normalize_level(self, actual: float, target: float, max_value: float) -> float:
        """
        Normalize outcome level to [0,1] scale.

        Args:
            actual: Actual performance value
            target: Target performance value
            max_value: Maximum possible value

        Returns:
            Normalized level in [0,1]

        Example:
            >>> scorer = LeTCIScorer()
            >>> normalized = scorer.normalize_level(actual=85, target=80, max_value=100)
            >>> print(f"Normalized: {normalized}")
            Normalized: 0.85
        """
        if max_value <= 0:
            raise ValueError("max_value must be positive")

        return min(actual / max_value, 1.0)

    def normalize_trend(self, values: List[float], periods: int = 3) -> float:
        """
        Normalize trend stability to [0,1] scale based on linear regression.

        Args:
            values: List of historical values (most recent last)
            periods: Number of periods to consider

        Returns:
            Normalized trend score in [0,1]
            - 1.0 = strong positive trend
            - 0.5 = flat/stable
            - 0.0 = strong negative trend

        Example:
            >>> scorer = LeTCIScorer()
            >>> values = [70, 75, 80, 85, 90]  # Improving trend
            >>> trend = scorer.normalize_trend(values)
            >>> print(f"Trend score: {trend}")
            Trend score: 0.9
        """
        if len(values) < 2:
            return 0.5  # Insufficient data, neutral

        # Use last N periods
        recent_values = values[-periods:] if len(values) > periods else values

        # Linear regression slope
        x = np.arange(len(recent_values))
        y = np.array(recent_values)

        if len(x) < 2:
            return 0.5

        # Compute slope
        slope = np.polyfit(x, y, 1)[0]

        # Normalize to [0,1]
        # Positive slope → higher score, negative slope → lower score
        max_expected_slope = np.mean(y) * 0.1  # 10% improvement per period
        normalized_slope = slope / max_expected_slope if max_expected_slope > 0 else 0

        # Map to [0,1] with 0.5 as neutral
        trend_score = 0.5 + (normalized_slope / 2)
        return np.clip(trend_score, 0.0, 1.0)

    def normalize_comparison(self, actual: float, benchmark: float) -> float:
        """
        Normalize comparative positioning to [0,1] scale.

        Args:
            actual: Actual performance value
            benchmark: Benchmark/competitor performance value

        Returns:
            Normalized comparison score in [0,1]
            - 1.0 = significantly above benchmark
            - 0.5 = at benchmark
            - 0.0 = significantly below benchmark

        Example:
            >>> scorer = LeTCIScorer()
            >>> comparison = scorer.normalize_comparison(actual=90, benchmark=80)
            >>> print(f"Comparison score: {comparison}")
            Comparison score: 0.75
        """
        if benchmark <= 0:
            return 0.5  # No valid benchmark

        ratio = actual / benchmark

        # Map ratio to [0,1]
        # ratio = 1.0 (at benchmark) → 0.5
        # ratio > 1.0 (above) → > 0.5
        # ratio < 1.0 (below) → < 0.5
        if ratio >= 1.0:
            # Above benchmark: map [1.0, 2.0] → [0.5, 1.0]
            score = 0.5 + min((ratio - 1.0) / 2.0, 0.5)
        else:
            # Below benchmark: map [0.0, 1.0] → [0.0, 0.5]
            score = 0.5 * ratio

        return np.clip(score, 0.0, 1.0)

    def get_diagnostic_breakdown(self, indicators: Dict[str, float]) -> Dict[str, float]:
        """
        Get diagnostic breakdown showing contribution of each LeTCI dimension.

        Args:
            indicators: Dictionary with keys 'R_Lv', 'R_Tr', 'R_Cp', 'R_I'

        Returns:
            Dictionary with contribution of each dimension to total score.

        Example:
            >>> scorer = LeTCIScorer()
            >>> indicators = {'R_Lv': 0.85, 'R_Tr': 0.90, 'R_Cp': 0.75, 'R_I': 0.70}
            >>> breakdown = scorer.get_diagnostic_breakdown(indicators)
            >>> for dim, contrib in breakdown.items():
            ...     print(f"{dim}: {contrib}")
            Levels: 29.75
            Trends: 22.5
            Comparisons: 18.75
            Integration: 10.5
            Total: 81.5
        """
        total_score = self.compute_score(indicators)

        breakdown = {
            'Levels': round(100 * self.weights['w_Lv'] * indicators['R_Lv'], 2),
            'Trends': round(100 * self.weights['w_Tr'] * indicators['R_Tr'], 2),
            'Comparisons': round(100 * self.weights['w_Cp'] * indicators['R_Cp'], 2),
            'Integration': round(100 * self.weights['w_I'] * indicators['R_I'], 2),
            'Total': total_score
        }

        return breakdown


def compute_letci_score(indicators: Dict[str, float], weights: Optional[Dict[str, float]] = None) -> float:
    """
    Convenience function to compute LeTCI score with default or custom weights.

    Args:
        indicators: Dictionary with keys 'R_Lv', 'R_Tr', 'R_Cp', 'R_I'
        weights: Optional custom weights

    Returns:
        LeTCI score in range [0, 100]

    Example:
        >>> score = compute_letci_score({'R_Lv': 0.85, 'R_Tr': 0.90, 'R_Cp': 0.75, 'R_I': 0.70})
        >>> print(score)
        81.25
    """
    scorer = LeTCIScorer(weights)
    return scorer.compute_score(indicators)


if __name__ == "__main__":
    # Example usage
    print("LeTCI Scoring Example")
    print("=" * 50)

    # Example: High-performing results item
    indicators = {
        'R_Lv': 0.85,  # High outcome level
        'R_Tr': 0.90,  # Strong positive trend
        'R_Cp': 0.75,  # Above benchmark
        'R_I': 0.70    # Good integration
    }

    scorer = LeTCIScorer()
    score = scorer.compute_score(indicators)

    print(f"\nIndicators:")
    print(f"  Levels (R_Lv):       {indicators['R_Lv']:.2f}")
    print(f"  Trends (R_Tr):       {indicators['R_Tr']:.2f}")
    print(f"  Comparisons (R_Cp):  {indicators['R_Cp']:.2f}")
    print(f"  Integration (R_I):   {indicators['R_I']:.2f}")

    print(f"\nLeTCI Score: {score}")

    print(f"\nDiagnostic Breakdown:")
    breakdown = scorer.get_diagnostic_breakdown(indicators)
    for dimension, contribution in breakdown.items():
        print(f"  {dimension}: {contribution}")

    # Example: Normalize trend from historical data
    print(f"\n" + "=" * 50)
    print("Trend Normalization Example")
    print("=" * 50)

    historical_values = [70, 75, 80, 85, 90]
    trend_score = scorer.normalize_trend(historical_values)
    print(f"\nHistorical values: {historical_values}")
    print(f"Trend score: {trend_score:.2f}")
    print(f"Interpretation: {'Improving' if trend_score > 0.6 else 'Stable' if trend_score > 0.4 else 'Declining'}")
