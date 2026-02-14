"""Pytest configuration and fixtures for edcellence tests."""

import pytest
import json
import os


@pytest.fixture
def sample_data():
    """Load sample organizational data for testing.

    Returns:
        dict: Sample data with categories and historical trends
    """
    from edcellence.data import load_sample_data
    return load_sample_data()


@pytest.fixture
def scorer():
    """Create OrganizationalScorer instance for testing.

    Returns:
        OrganizationalScorer: Configured scorer instance
    """
    from edcellence import OrganizationalScorer
    return OrganizationalScorer()


@pytest.fixture
def visualizer():
    """Create ScoringVisualizer instance for testing.

    Returns:
        ScoringVisualizer: Configured visualizer instance
    """
    from edcellence import ScoringVisualizer
    return ScoringVisualizer()


@pytest.fixture
def advanced_visualizer():
    """Create AdvancedVisualizer instance for testing.

    Returns:
        AdvancedVisualizer: Configured advanced visualizer instance
    """
    from edcellence import AdvancedVisualizer
    return AdvancedVisualizer()


@pytest.fixture
def temp_output_dir(tmp_path):
    """Create temporary directory for test outputs.

    Args:
        tmp_path: pytest tmp_path fixture

    Returns:
        Path: Path to temporary output directory
    """
    output_dir = tmp_path / "outputs"
    output_dir.mkdir()
    return output_dir
