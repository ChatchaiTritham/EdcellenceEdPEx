"""Data module for edcellence package.

This module contains sample data files for demonstration and testing purposes.
"""

import os
import json


def get_sample_data_path():
    """Get path to sample organizational data JSON file.

    Returns:
        str: Absolute path to organizational_data.json

    Example:
        >>> from edcellence.data import get_sample_data_path
        >>> import json
        >>> with open(get_sample_data_path(), 'r') as f:
        ...     data = json.load(f)
    """
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'sample', 'organizational_data.json')


def load_sample_data():
    """Load sample organizational data.

    Returns:
        dict: Sample organizational data with categories and historical trends

    Example:
        >>> from edcellence.data import load_sample_data
        >>> data = load_sample_data()
        >>> print(list(data.keys()))
        ['categories', 'historical_trends']
    """
    with open(get_sample_data_path(), 'r', encoding='utf-8') as f:
        return json.load(f)


__all__ = ['get_sample_data_path', 'load_sample_data']
