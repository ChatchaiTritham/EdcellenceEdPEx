"""Setup script for edcellence package.

This setup.py is provided for backward compatibility with older tools.
Modern installations should use pyproject.toml (PEP 517/518).
"""

from setuptools import setup, find_packages
import os

# Read version from _version.py
version_file = os.path.join(os.path.dirname(__file__), 'edcellence', '_version.py')
version_info = {}
with open(version_file, 'r', encoding='utf-8') as f:
    exec(f.read(), version_info)

# Read README for long description
readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
with open(readme_file, 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="edcellence",
    version=version_info['__version__'],
    description=version_info['__description__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=version_info['__author__'],
    author_email=version_info['__author_email__'],
    url=version_info['__url__'],
    license=version_info['__license__'],
    packages=find_packages(exclude=['tests', 'tests.*', 'examples', 'examples.*', 'docs', 'docs.*']),
    package_data={
        'edcellence': ['data/sample/*.json'],
    },
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=[
        'matplotlib>=3.8.0',
        'seaborn>=0.13.0',
        'pandas>=2.1.0',
        'numpy>=1.26.0',
        'plotly>=5.18.0',
        'networkx>=3.2.0',
        'scipy>=1.11.0',
        'statsmodels>=0.14.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'black>=23.12.0',
            'flake8>=7.0.0',
            'mypy>=1.8.0',
            'jupyter>=1.0.0',
            'nbconvert>=7.14.0',
        ],
        'docs': [
            'sphinx>=7.2.0',
            'sphinx-rtd-theme>=2.0.0',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    keywords='education performance-excellence baldrige assessment higher-education quality-assurance',
    project_urls={
        'Documentation': 'https://github.com/ChatchaiTritham/EdcellenceEdPEx/blob/master/README.md',
        'Source': 'https://github.com/ChatchaiTritham/EdcellenceEdPEx',
        'Tracker': 'https://github.com/ChatchaiTritham/EdcellenceEdPEx/issues',
    },
)
