# EdcellenceEdPEx

**From Excellence Guidelines to Computable Performance Systems: A Novel Framework for Educational Performance Excellence Assessment**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![IEEE ACCESS](https://img.shields.io/badge/Journal-IEEE%20ACCESS-blue)](https://ieeeaccess.ieee.org/)

---

## Overview

**EdcellenceEdPEx** (Excellence in Education Performance Excellence) is the first computational implementation of the Baldrige Excellence Framework (BEB) tailored for higher education institutions. This framework transforms qualitative excellence guidelines into quantifiable, automated performance assessment systems.

### Key Features

- **ADLI Scoring Algorithm** - Process categories assessment (Approach-Deployment-Learning-Integration)
- **LeTCI Scoring Algorithm** - Results category assessment (Levels-Trends-Comparisons-Integration)
- **Automated Performance Evaluation** - 69% reduction in assessment cycle duration
- **53 Professional Visualizations** - 28 static charts (300 DPI PNG) + 10 interactive dashboards (HTML) + 15 manuscript figures
- **Interactive Dashboards** - Plotly-powered HTML visualizations for exploratory analysis (no internet required)
- **Publication-Ready Figures** - 15 IEEE ACCESS-compliant figures (300 DPI, 4.5 MB total)
- **Comprehensive Testing** - 32 unit tests with 96.9% pass rate
- **Empirical Validation** - Proven effectiveness across 24 organizational units

---

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Features](#features)
- [Documentation](#documentation)
- [Visualizations](#visualizations)
- [Empirical Validation](#empirical-validation)
- [Citation](#citation)
- [License](#license)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

---

## Installation

### Prerequisites

- Python 3.13 or higher
- pip (Python package manager)
- Git

### Step 1: Clone Repository

```bash
git clone https://github.com/ChatchaiTritham/EdcellenceEdPEx.git
cd EdcellenceEdPEx
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv-edpex
venv-edpex\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv-edpex
source venv-edpex/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install matplotlib seaborn pandas numpy plotly networkx scipy statsmodels jupyter nbconvert
```

### Automated Setup (Windows)

```bash
# Run automated setup script
setup-venv.bat
```

---

## Quick Start

### Basic Framework Demo

```bash
python examples/complete_demo.py
```

**Outputs:** 7 visualizations demonstrating core framework features
- Radar chart (category performance)
- ADLI breakdown (process scoring)
- LeTCI breakdown (results scoring)
- Gap analysis heatmap
- Priority matrix
- 3D evolution surface
- Interactive scorecard

### Advanced Visualizations

```bash
python examples/advanced_visualizations_demo.py
```

**Outputs:** 11 advanced analytics visualizations
- Distribution comparisons
- Correlation matrices
- Network dependency diagrams
- Hierarchical sunburst charts
- Sankey flow diagrams
- Temporal decomposition
- 3D scatter plots
- Statistical summaries

### Jupyter Notebooks

```bash
jupyter notebook notebooks/01_Framework_Complete_Demo.ipynb
jupyter notebook notebooks/02_Advanced_Visualizations.ipynb
```

---

## Features

### 1. ADLI Scoring Algorithm

**Process Categories (1-6):** Leadership, Strategy, Customers, Measurement, Workforce, Operations

**Dimensions:**
- **Approach (30%):** Systematic methods and evidence of effectiveness
- **Deployment (30%):** Extent of implementation across organization
- **Learning (20%):** Refinement through evaluation and innovation
- **Integration (20%):** Alignment with organizational needs

**Usage:**

```python
from src.algorithms.organizational_scoring import OrganizationalScorer

scorer = OrganizationalScorer()
result = scorer.compute_item_score(
    category=2,
    item_id=1,
    indicators={
        'P_A': 0.75,  # Approach score
        'P_D': 0.65,  # Deployment score
        'P_L': 0.70,  # Learning score
        'P_I': 0.68   # Integration score
    }
)

print(f"Score: {result.score:.2f}")
print(f"Breakdown: {result.breakdown}")
```

### 2. LeTCI Scoring Algorithm

**Results Category (7):** Organizational Performance Results

**Dimensions:**
- **Levels (35%):** Current performance levels
- **Trends (25%):** Rate of performance improvement
- **Comparisons (25%):** Performance relative to benchmarks
- **Integration (15%):** Linkage to organizational priorities

**Usage:**

```python
result = scorer.compute_item_score(
    category=7,
    item_id=1,
    indicators={
        'R_Le': 0.85,  # Levels score
        'R_T': 0.75,   # Trends score
        'R_C': 0.70,   # Comparisons score
        'R_I': 0.80    # Integration score
    }
)
```

### 3. Organizational-Level Aggregation

**Category Weights:**
- Leadership: 12%
- Strategy: 12%
- Customers: 12%
- Measurement: 11%
- Workforce: 11%
- Operations: 11%
- Results: 45%

**Usage:**

```python
org_score = scorer.compute_organizational_score(category_scores)
print(f"Organizational Score: {org_score:.2f}")
```

### 4. Gap Analysis & Prioritization

```python
gap_df = scorer.compute_gap_analysis(current_scores, target_scores)
priority_items = gap_df.sort_values('priority', ascending=False).head(10)
```

### 5. Integration Health Index (IHI)

Measures cross-category alignment using Pearson correlation:

```python
ihi = scorer.compute_integration_health_index(historical_data)
print(f"Integration Health Index: {ihi:.3f}")
```

---

## Documentation

### Core Modules

- **`src/algorithms/organizational_scoring.py`** - ADLI/LeTCI scoring algorithms
- **`src/visualizations/scoring_visualizer.py`** - 18+ visualization methods
- **`src/visualizations/advanced_visualizer.py`** - Advanced analytics

### Example Scripts

- **`examples/complete_demo.py`** - Basic framework demonstration
- **`examples/advanced_visualizations_demo.py`** - Advanced analytics

### Jupyter Notebooks

- **`notebooks/01_Framework_Complete_Demo.ipynb`** - Interactive framework tutorial
- **`notebooks/02_Advanced_Visualizations.ipynb`** - Advanced visualization techniques

### Sample Data

- **`data/sample/organizational_data.json`** - Sample dataset with 5-year historical trends

### Manuscript Materials

- **`manuscript_figures/`** - 15 publication-ready figures (300 DPI PNG)
- **`MANUSCRIPT_FIGURES_README.md`** - Figure descriptions and captions
- **`IEEE_ACCESS_SUBMISSION_GUIDE.md`** - Complete submission guide

---

## Visualizations

The framework generates **38+ high-quality visualizations** for comprehensive performance analysis, including static charts (PNG, 300 DPI) and interactive dashboards (HTML). All visualizations are automatically generated and saved to the `outputs/` directory.

### Overview

| Category | Count | Format | Location | Purpose |
|----------|-------|--------|----------|---------|
| **Static Charts** | 28 files | PNG (300 DPI) | `outputs/*.png` | Publication-quality figures |
| **Interactive Dashboards** | 10 files | HTML (Plotly) | `outputs/*.html` | Exploratory analysis |
| **Manuscript Figures** | 15 files | PNG (300 DPI) | `manuscript_figures/*.png` | IEEE ACCESS submission |
| **Total** | **53 files** | Mixed | Multiple | Complete analytics suite |

### How to Generate Visualizations

**Method 1: Run Demo Scripts**

```bash
# Generate 16 core visualizations (6 PNG + 10 HTML)
python examples/complete_demo.py

# Generate 11 advanced visualizations (8 PNG + 3 HTML)
python examples/advanced_visualizations_demo.py
```

**Method 2: Run Jupyter Notebooks**

```bash
# Generate 9 visualizations (8 PNG + 1 HTML)
jupyter notebook notebooks/01_Framework_Complete_Demo.ipynb

# Generate 9 visualizations (6 PNG + 3 HTML)
jupyter notebook notebooks/02_Advanced_Visualizations.ipynb
```

**Method 3: Programmatic Generation**

```python
from src.algorithms.organizational_scoring import OrganizationalScorer
from src.visualizations.scoring_visualizer import ScoringVisualizer
import json

# Load data
with open('data/sample/organizational_data.json', 'r') as f:
    data = json.load(f)

# Initialize
scorer = OrganizationalScorer()
viz = ScoringVisualizer()

# Generate specific visualization
viz.plot_radar_chart(category_scores, save_path='outputs/my_radar.png')
viz.plot_interactive_scorecard(category_scores, save_path='outputs/my_scorecard.html')
```


### Visualization Categories & Use Cases

#### 1. Performance Assessment
- **Radar Chart** - Overall category performance at a glance
- **ADLI/LeTCI Breakdown** - Detailed dimension analysis
- **Statistical Summary** - Quantitative metrics with confidence intervals

#### 2. Gap Analysis & Planning
- **Gap Heatmap** - Identify underperforming areas
- **Priority Matrix** - Prioritize improvement initiatives
- **Trend Analysis** - Track historical performance

#### 3. Relationship Analysis
- **Correlation Matrix** - Understand category interdependencies
- **Network Diagram** - Visualize systemic relationships
- **Sankey Flow** - Track performance flow across categories

#### 4. Advanced Analytics
- **3D Visualizations** - Explore multi-dimensional performance space
- **Temporal Decomposition** - Separate trend, seasonal, and noise components
- **Parallel Coordinates** - Multi-dimensional data exploration
- **Distribution Analysis** - Statistical distribution comparison

#### 5. Interactive Exploration
- **Interactive Scorecard** - Drill-down into category details
- **Sunburst Hierarchy** - Navigate category-item hierarchy
- **3D Scatter** - Rotate and explore ADLI/LeTCI space

---

### Customization Options

All visualizations support extensive customization:

```python
from src.visualizations.scoring_visualizer import ScoringVisualizer

viz = ScoringVisualizer()

# Customize colors
viz.plot_radar_chart(
    scores,
    colors='viridis',  # Color scheme
    alpha=0.7,         # Transparency
    save_path='custom_radar.png'
)

# Customize dimensions
viz.plot_gap_heatmap(
    gap_data,
    figsize=(12, 10),   # Figure size
    dpi=300,            # Resolution
    cmap='RdYlGn',      # Color map
    save_path='custom_heatmap.png'
)

# Customize interactive features
viz.plot_interactive_scorecard(
    scores,
    title='Custom Dashboard',
    height=800,
    width=1200,
    save_path='custom_scorecard.html'
)
```

---

### File Naming Convention

| Prefix | Source | Example |
|--------|--------|---------|
| `01-16_*` | `complete_demo.py` | `01_radar_chart.png` |
| `adv_nb_*` | `advanced_visualizations_demo.py` | `adv_nb_01_distribution.png` |
| `nb_*` | Jupyter notebooks | `nb_01_adli.png` |
| `Fig[1-15]_*` | Manuscript figures | `Fig1_BEB-EdPEx_Category_Performance_Radar.png` |

---

### Technical Specifications

**Static Visualizations (PNG):**
- **Resolution:** 300 DPI (publication quality)
- **Color Space:** RGB
- **Compression:** PNG lossless
- **Typical Size:** 100-700 KB per file
- **Libraries:** Matplotlib 3.8+, Seaborn 0.13+

**Interactive Visualizations (HTML):**
- **Framework:** Plotly.js 2.27+
- **Compatibility:** All modern browsers (Chrome, Firefox, Safari, Edge)
- **Offline:** Fully functional without internet connection
- **Responsive:** Adapts to different screen sizes
- **File Size:** 300-600 KB per file

**Color Schemes:**
- **Categorical:** Tab10, Set2, Paired
- **Sequential:** Viridis, Plasma, Blues, Greens
- **Diverging:** RdYlGn, RdBu, Spectral
- **All schemes:** ColorBlind-friendly options available

---

## Empirical Validation

### Study Design

- **Sample Size:** 24 organizational units
- **Institution:** Rajamangala University of Technology Krungthep
- **Period:** Academic Year 2024-2025
- **Design:** Pre-post intervention study

### Key Results

| Metric | Baseline | Post-Implementation | Change | p-value | Effect Size |
|--------|----------|---------------------|--------|---------|-------------|
| **Assessment Cycle Duration** | 6.5 weeks | 2.0 weeks | **-69%** | p<0.001 | d=3.2 (Large) |
| **Documentation Artifacts** | 450 docs | 80 docs | **-82%** | p<0.001 | d=3.8 (Large) |
| **Measurement Consistency** | α=0.62 | α=0.88 | **+42%** | p<0.001 | d=2.1 (Large) |
| **Review Duration** | 4.5 hours | 2.5 hours | **-44%** | p<0.001 | d=2.4 (Large) |

**Interpretation:** All effects demonstrated large effect sizes (Cohen's d > 2.0), validating the framework's practical effectiveness in reducing administrative burden while improving measurement quality.

### Technical Performance

- **Category-level aggregation:** 47±12ms (mean±SD)
- **Institution-level synthesis:** 183±31ms
- **Query success rate:** 99.7%
- **Correlation with expert assessment:** r=0.91 (p<0.001)

---

## Citation

If you use this framework in your research, please cite:

### Paper (In Press)

```bibtex
@article{tritham2026edpex,
  title={From Excellence Guidelines to Computable Performance Systems: A Novel Framework for Educational Performance Excellence Assessment},
  author={Tritham, Chatchai and Saosing, Rungtiva and Kamlangkla, Kanchit and Tritham, Chattabhorn},
  journal={IEEE ACCESS},
  year={2026},
  note={In Press}
}
```

### Software

```bibtex
@software{tritham2026edpex_software,
  title={EdcellenceEdPEx: BEB-EdPEx Framework Implementation},
  author={Tritham, Chatchai and Saosing, Rungtiva and Kamlangkla, Kanchit and Tritham, Chattabhorn},
  year={2026},
  url={https://github.com/ChatchaiTritham/EdcellenceEdPEx},
  version={1.0}
}
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ⚠️ Liability and warranty limitations apply

---

## Authors

**Chatchai Tritham** (Corresponding Author & Project Manager)
Faculty of Science and Technology Rajamangala, University of Technology Krungthep, Bangkok 10120 Thailand
📧 chatchait66@nu.ac.th
🆔 ORCID: [0000-0001-7899-228X](https://orcid.org/0000-0001-7899-228X)

**Rungtiva Saosing** (First Author)
Faculty of Science and Technology Rajamangala, University of Technology Krungthep, Bangkok 10120 Thailand
📧 rungtiva.s@mail.rmutt.ac.th
🆔 ORCID: [0009-0007-8713-8190](https://orcid.org/0009-0007-8713-8190)

**Kanchit Kamlangkla** (Co-Author)
Faculty of Science and Technology Rajamangala, University of Technology Krungthep, Bangkok 10120 Thailand
📧 kanchit.k@mail.rmutk.ac.th

**Chattabhorn Tritham** (Co-Author & Software Engineer)
Thammasat School of Engineering (TSE)
Thammasat University, Thailand
📧 memodia@live.com
🆔 ORCID: [0009-0003-2408-7374](https://orcid.org/0009-0003-2408-7374)

### Contributions

- **C.T. (Chatchai):** Project management, conceptualization, software development, algorithm implementation
- **R.S.:** Methodology, validation, empirical study design, writing—original draft
- **K.K.:** Data analysis, institutional coordination, resources
- **C.T. (Chattabhorn):** Software engineering, statistical validation, visualization, writing—review

---

## Acknowledgments

### Data Contributors

We thank the 24 organizational units at Rajamangala University of Technology Krungthep who participated in the empirical validation study.

### Framework Foundation

This work builds upon the Baldrige Excellence Framework developed by the National Institute of Standards and Technology (NIST), USA.

---

## Repository Structure

```
EdcellenceEdPEx/
├── src/
│   ├── algorithms/
│   │   └── organizational_scoring.py    # ADLI/LeTCI scoring algorithms
│   └── visualizations/
│       ├── scoring_visualizer.py        # Core visualizations (18+ methods)
│       └── advanced_visualizer.py       # Advanced analytics
├── examples/
│   ├── complete_demo.py                 # Basic framework demo (16 visualizations)
│   └── advanced_visualizations_demo.py  # Advanced demo (11 visualizations)
├── notebooks/
│   ├── 01_Framework_Complete_Demo.ipynb # Interactive tutorial (9 visualizations)
│   └── 02_Advanced_Visualizations.ipynb # Advanced techniques (9 visualizations)
├── tests/
│   └── test_organizational_scoring.py   # 32 comprehensive tests (96.9% pass)
├── data/
│   └── sample/
│       └── organizational_data.json     # Sample dataset (5-year trends)
├── outputs/                              # Generated visualizations (auto-created)
│   ├── *.png                            # 28 static charts (300 DPI)
│   └── *.html                           # 10 interactive dashboards (Plotly)
├── manuscript_figures/                   # 15 publication-ready figures (300 DPI PNG, 4.5 MB)
│   ├── Fig1_BEB-EdPEx_Category_Performance_Radar.png
│   ├── Fig2_ADLI_Process_Scoring_Breakdown.png
│   ├── ...
│   └── Fig15_Empirical_Validation_Results.png
├── docs/                                 # Documentation
│   ├── MANUSCRIPT_FIGURES_README.md     # Figure captions
│   └── IEEE_ACCESS_SUBMISSION_GUIDE.md  # Submission guide
├── setup-venv.bat                        # Windows setup script
├── setup-venv.sh                         # Linux/Mac setup script
├── requirements.txt                      # Python dependencies
├── LICENSE                               # MIT License
└── README.md                             # This file
```

---

## Troubleshooting

### Common Issues

**Issue 1: Import errors**
```bash
# Solution: Ensure virtual environment is activated and dependencies installed
pip install -r requirements.txt
```

**Issue 2: Unicode encoding errors (Windows)**
```bash
# Solution: Use UTF-8 encoding
set PYTHONIOENCODING=utf-8
python examples/complete_demo.py
```

**Issue 3: Matplotlib backend errors**
```python
# Solution: Add at top of script
import matplotlib
matplotlib.use('Agg')
```

---

## FAQ

**Q: Can this framework be used for non-educational organizations?**
A: The algorithms are generalizable, but the category structure follows Baldrige Education Criteria. For business/healthcare/government, category definitions would need modification.

**Q: What's the minimum sample size for reliable results?**
A: Based on our validation (n=24), statistical power exceeds 0.99 for detecting large effects. Minimum recommended: n≥15 organizational units.

**Q: How long does assessment take?**
A: Post-implementation average: 2.0 weeks per assessment cycle (vs. 6.5 weeks baseline).

**Q: Is internet connection required?**
A: No. All computations run locally. Interactive HTML visualizations work offline.

**Q: Can I customize category weights?**
A: Yes. Modify `CATEGORY_WEIGHTS` dictionary in `organizational_scoring.py`.

---

## Roadmap

### Version 1.1 (Planned)

- [ ] REST API for web-based assessments
- [ ] Real-time dashboard (Streamlit/Dash)
- [ ] Multi-language support (Thai, Chinese, Japanese)
- [ ] Automated report generation (PDF/DOCX)
- [ ] Database integration (PostgreSQL/MongoDB)

### Version 2.0 (Future)

- [ ] Machine learning-based scoring recommendations
- [ ] Benchmark database (national/international)
- [ ] Mobile application (iOS/Android)
- [ ] Integration with institutional data systems

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### How to Contribute

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## Support

### Issues & Bug Reports

Please report issues via [GitHub Issues](https://github.com/ChatchaiTritham/EdcellenceEdPEx/issues)

### Contact

**For questions or collaboration inquiries:**

**Corresponding Author:**
- 📧 Chatchai Tritham: chatchait66@nu.ac.th
- 🆔 ORCID: [0000-0001-7899-228X](https://orcid.org/0000-0001-7899-228X)

**First Author:**
- 📧 Rungtiva Saosing: rungtiva.s@mail.rmutt.ac.th
- 🆔 ORCID: [0009-0007-8713-8190](https://orcid.org/0009-0007-8713-8190)

**Institution:**
- 🌐 Faculty of Science and Technology Rajamangala, University of Technology Krungthep, Bangkok 10120 Thailand
- 🌐 [Rajamangala University of Technology Krungthep](https://www.rmutk.ac.th)

---

## Changelog

### Version 1.0.0 (2026-02-14)

- ✅ Initial release
- ✅ ADLI/LeTCI scoring algorithms
- ✅ 38 publication-quality visualizations
- ✅ 2 interactive Jupyter notebooks
- ✅ 32 comprehensive unit tests
- ✅ Empirical validation (n=24)
- ✅ Complete documentation
- ✅ IEEE ACCESS manuscript materials

---

**🌟 If you find this framework useful, please star the repository and cite our work! 🌟**

---

*Last Updated: February 14, 2026*
*Version: 1.0.0*
*Repository: https://github.com/ChatchaiTritham/EdcellenceEdPEx*
