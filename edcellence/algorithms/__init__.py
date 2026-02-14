"""
EdcellenceEdPEx Algorithms Package
===================================

This package contains the core computational algorithms for the ADLI-LeTCI
framework used in organizational excellence assessment.

Modules:
    adli_scoring: ADLI (Approach-Deployment-Learning-Integration) scoring for processes
    letci_scoring: LeTCI (Levels-Trends-Comparisons-Integration) scoring for results
    gap_analysis: Gap analysis and improvement prioritization (coming soon)
    integration_health: Integration Health Index computation (coming soon)

Example:
    >>> from src.algorithms import compute_adli_score, compute_letci_score
    >>>
    >>> # Compute ADLI score for a process item
    >>> adli_score = compute_adli_score({
    ...     'P_A': 0.75, 'P_D': 0.45, 'P_L': 0.60, 'P_I': 0.55
    ... })
    >>>
    >>> # Compute LeTCI score for a results item
    >>> letci_score = compute_letci_score({
    ...     'R_Lv': 0.85, 'R_Tr': 0.90, 'R_Cp': 0.75, 'R_I': 0.70
    ... })
"""

from .adli_scoring import ADLIScorer, compute_adli_score
from .letci_scoring import LeTCIScorer, compute_letci_score

__version__ = "1.0.0"
__author__ = "Rungtiva Saosing, Chatchai Tritham, Chattabhorn Tritham, Sudasawan Ngammongkolwong"

__all__ = [
    'ADLIScorer',
    'LeTCIScorer',
    'compute_adli_score',
    'compute_letci_score',
]
