"""
Edcellence - Educational Performance Excellence Assessment Framework

A computational implementation of the Baldrige Excellence Framework (BEB)
for higher education institutions.

Basic Usage:
    >>> from edcellence import OrganizationalScorer, ScoringVisualizer
    >>> scorer = OrganizationalScorer()
    >>> viz = ScoringVisualizer()
    >>>
    >>> # Load sample data
    >>> import json
    >>> with open('edcellence/data/sample/organizational_data.json', 'r') as f:
    ...     data = json.load(f)
    >>>
    >>> # Calculate scores
    >>> org_score = scorer.score_organization(data)
    >>> print(f"Organization Score: {org_score:.2f}")
"""

from edcellence._version import (
    __version__,
    __version_info__,
    __title__,
    __description__,
    __author__,
    __author_email__,
    __license__,
    __copyright__,
    __url__,
)

# Import main classes for convenient access
from edcellence.algorithms.organizational_scoring import OrganizationalScorer
from edcellence.visualizations.scoring_visualizer import ScoringVisualizer
from edcellence.visualizations.advanced_visualizer import AdvancedVisualizer

# Define public API
__all__ = [
    # Version info
    "__version__",
    "__version_info__",
    "__title__",
    "__description__",
    "__author__",
    "__author_email__",
    "__license__",
    "__copyright__",
    "__url__",
    # Main classes
    "OrganizationalScorer",
    "ScoringVisualizer",
    "AdvancedVisualizer",
]


def get_sample_data_path():
    """Get path to sample data file.

    Returns:
        str: Path to organizational_data.json sample file

    Example:
        >>> from edcellence import get_sample_data_path
        >>> import json
        >>> with open(get_sample_data_path(), 'r') as f:
        ...     data = json.load(f)
    """
    import os
    package_dir = os.path.dirname(__file__)
    return os.path.join(package_dir, 'data', 'sample', 'organizational_data.json')


# Add to public API
__all__.append("get_sample_data_path")
