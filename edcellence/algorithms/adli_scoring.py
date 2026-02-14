"""
ADLI Scoring Algorithm
======================

Implements the ADLI (Approach-Deployment-Learning-Integration) scoring
methodology for process assessment in organizational excellence frameworks.

Mathematical Formulation:
    S_item[c,i] = 100 × (w_A·P_A[c,i] + w_D·P_D[c,i] + w_L·P_L[c,i] + w_I·P_I[c,i])

where:
    - P_A: Approach adequacy (normalized [0,1])
    - P_D: Deployment consistency (normalized [0,1])
    - P_L: Learning effectiveness (normalized [0,1])
    - P_I: Integration (normalized [0,1])
    - w_A, w_D, w_L, w_I: Weights (default: 0.30, 0.30, 0.20, 0.20)

Reference:
    Saosing et al. (2026). From Excellence Guidelines to Computable Performance Systems.
    IEEE ACCESS (under review).
"""

from typing import Dict, Optional
import numpy as np


class ADLIScorer:
    """ADLI scoring engine for process assessment."""

    # Default weights (sum = 1.0)
    DEFAULT_WEIGHTS = {
        'w_A': 0.30,  # Approach
        'w_D': 0.30,  # Deployment
        'w_L': 0.20,  # Learning
        'w_I': 0.20   # Integration
    }

    def __init__(self, weights: Optional[Dict[str, float]] = None):
        """
        Initialize ADLI scorer.

        Args:
            weights: Custom weights for ADLI dimensions. If None, uses defaults.
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
        Compute ADLI score for a process item.

        Args:
            indicators: Dictionary with keys 'P_A', 'P_D', 'P_L', 'P_I'
                       representing normalized indicators [0,1].

        Returns:
            ADLI score in range [0, 100].

        Raises:
            ValueError: If indicators are missing or out of range.

        Example:
            >>> scorer = ADLIScorer()
            >>> indicators = {
            ...     'P_A': 0.75,  # Approach adequacy
            ...     'P_D': 0.45,  # Deployment consistency
            ...     'P_L': 0.60,  # Learning effectiveness
            ...     'P_I': 0.55   # Integration
            ... }
            >>> score = scorer.compute_score(indicators)
            >>> print(f"ADLI Score: {score}")
            ADLI Score: 59.0
        """
        required_keys = {'P_A', 'P_D', 'P_L', 'P_I'}
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
            self.weights['w_A'] * indicators['P_A'] +
            self.weights['w_D'] * indicators['P_D'] +
            self.weights['w_L'] * indicators['P_L'] +
            self.weights['w_I'] * indicators['P_I']
        )

        return round(score, 2)

    def compute_category_score(
        self,
        item_scores: Dict[int, float],
        item_weights: Optional[Dict[int, float]] = None
    ) -> float:
        """
        Aggregate item scores to category score.

        Args:
            item_scores: Dictionary {item_id: score}
            item_weights: Optional weights {item_id: weight}. If None, uses equal weights.

        Returns:
            Category score in range [0, 100].

        Example:
            >>> scorer = ADLIScorer()
            >>> item_scores = {1: 75.0, 2: 59.0, 3: 82.0}
            >>> category_score = scorer.compute_category_score(item_scores)
            >>> print(f"Category Score: {category_score}")
            Category Score: 72.0
        """
        if not item_scores:
            raise ValueError("item_scores cannot be empty")

        # Use equal weights if not specified
        if item_weights is None:
            n_items = len(item_scores)
            item_weights = {item_id: 1.0/n_items for item_id in item_scores.keys()}

        # Validate weights sum to 1.0
        weight_sum = sum(item_weights.values())
        if not np.isclose(weight_sum, 1.0, atol=1e-6):
            raise ValueError(f"Item weights must sum to 1.0, got {weight_sum}")

        # Compute weighted average
        category_score = sum(
            item_weights[item_id] * score
            for item_id, score in item_scores.items()
        )

        return round(category_score, 2)

    def get_diagnostic_breakdown(self, indicators: Dict[str, float]) -> Dict[str, float]:
        """
        Get diagnostic breakdown showing contribution of each ADLI dimension.

        Args:
            indicators: Dictionary with keys 'P_A', 'P_D', 'P_L', 'P_I'

        Returns:
            Dictionary with contribution of each dimension to total score.

        Example:
            >>> scorer = ADLIScorer()
            >>> indicators = {'P_A': 0.75, 'P_D': 0.45, 'P_L': 0.60, 'P_I': 0.55}
            >>> breakdown = scorer.get_diagnostic_breakdown(indicators)
            >>> for dim, contrib in breakdown.items():
            ...     print(f"{dim}: {contrib}")
            Approach: 22.5
            Deployment: 13.5
            Learning: 12.0
            Integration: 11.0
        """
        total_score = self.compute_score(indicators)

        breakdown = {
            'Approach': round(100 * self.weights['w_A'] * indicators['P_A'], 2),
            'Deployment': round(100 * self.weights['w_D'] * indicators['P_D'], 2),
            'Learning': round(100 * self.weights['w_L'] * indicators['P_L'], 2),
            'Integration': round(100 * self.weights['w_I'] * indicators['P_I'], 2),
            'Total': total_score
        }

        return breakdown


def compute_adli_score(indicators: Dict[str, float], weights: Optional[Dict[str, float]] = None) -> float:
    """
    Convenience function to compute ADLI score with default or custom weights.

    Args:
        indicators: Dictionary with keys 'P_A', 'P_D', 'P_L', 'P_I'
        weights: Optional custom weights

    Returns:
        ADLI score in range [0, 100]

    Example:
        >>> score = compute_adli_score({'P_A': 0.75, 'P_D': 0.45, 'P_L': 0.60, 'P_I': 0.55})
        >>> print(score)
        59.0
    """
    scorer = ADLIScorer(weights)
    return scorer.compute_score(indicators)


if __name__ == "__main__":
    # Example usage
    print("ADLI Scoring Example")
    print("=" * 50)

    # Example from paper (Category 2, Item 3)
    indicators = {
        'P_A': 0.75,  # Approach well-specified
        'P_D': 0.45,  # Deployment inconsistent
        'P_L': 0.60,  # Moderate learning
        'P_I': 0.55   # Integration developing
    }

    scorer = ADLIScorer()
    score = scorer.compute_score(indicators)

    print(f"\nIndicators:")
    print(f"  Approach (P_A):    {indicators['P_A']:.2f}")
    print(f"  Deployment (P_D):  {indicators['P_D']:.2f}")
    print(f"  Learning (P_L):    {indicators['P_L']:.2f}")
    print(f"  Integration (P_I): {indicators['P_I']:.2f}")

    print(f"\nADLI Score: {score}")

    print(f"\nDiagnostic Breakdown:")
    breakdown = scorer.get_diagnostic_breakdown(indicators)
    for dimension, contribution in breakdown.items():
        print(f"  {dimension}: {contribution}")

    print(f"\nInterpretation:")
    print(f"  The score of {score} indicates early systematic maturity.")
    print(f"  Approach strength (P_A=0.75) is counterbalanced by")
    print(f"  deployment inconsistency (P_D=0.45), suggesting focus on")
    print(f"  deployment support and organizational change facilitation.")
