# EdcellenceEdPEx: Computational Framework for Organizational Excellence

**From Excellence Guidelines to Computable Performance Systems**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![IEEE ACCESS](https://img.shields.io/badge/Publication-IEEE%20ACCESS-blue.svg)](https://ieeeaccess.ieee.org/)

---

## About This Project

This repository implements the computational framework described in our IEEE ACCESS publication, transforming abstract organizational excellence guidelines (EdPEx, Baldrige) into executable digital systems through mathematical formalization of ADLI--LeTCI assessment logic.

Developed at the Faculty of Science and Technology, Rajamangala University of Technology Krungthep, this framework addresses the persistent challenge of operationalizing qualitative excellence criteria into quantifiable, reproducible assessment methodologies suitable for continuous organizational learning.

**Authors:**
- Rungtiva Saosing (RMUTK)
- Chatchai Tritham (RMUTK & AppVisor)
- Chattabhorn Tritham (Thammasat University & AppVisor)
- Sudasawan Ngammongkolwong (Southeast Bangkok University)

---

## Core Innovation

Traditional excellence frameworks (Baldrige, EFQM, ISO) provide valuable conceptual guidance but resist direct computational implementation. Organizations struggle to translate narrative assessment criteria into systematic data analytics and real-time decision infrastructures.

Our framework resolves this through:

1. **Mathematical Formalization**: ADLI (Approach-Deployment-Learning-Integration) and LeTCI (Levels-Trends-Comparisons-Integration) evaluation logic expressed as normalized computational constructs with explicit equations and procedural algorithms.

2. **Multi-Framework Integration**: Unified evidence infrastructure consolidating EdPEx, TQF (Thailand Qualifications Framework), and AUN-QA (ASEAN University Network) requirements—eliminating duplicative documentation while preserving differentiated compliance artifacts.

3. **Empirical Validation**: Deployment across 24 organizational units demonstrated 69% reduction in assessment cycle duration, 82% decrease in documentation artifacts, and 42% improvement in measurement consistency (all p<0.001, Cohen's d=2.1-3.8).

---

## Key Features

### ADLI Process Evaluation
Process categories (Leadership, Strategy, Customers, Measurement, Workforce, Operations) assessed through:

```
S_item = 100 × (w_A·P_A + w_D·P_D + w_L·P_L + w_I·P_I)
```

Where normalized indicators [0,1] measure Approach adequacy, Deployment consistency, Learning effectiveness, and Integration coherence.

### LeTCI Outcome Assessment
Results category evaluated through:

```
S_item = 100 × (w_Lv·R_Lv + w_Tr·R_Tr + w_Cp·R_Cp + w_I·R_I)
```

Capturing outcome Levels, performance Trends, Comparative positioning, and Integration alignment.

### Integration Health Index (IHI)
Quantifies cross-category coherence through edge-based assessment of organizational system dependencies.

---

## Getting Started

### Installation

```bash
git clone https://github.com/yourusername/EdcellenceEdPEx.git
cd EdcellenceEdPEx
pip install -r requirements.txt
```

### Quick Example

```python
from src.algorithms import compute_adli_score, compute_letci_score

# Process assessment (ADLI)
process_score = compute_adli_score({
    'P_A': 0.75,  # Approach
    'P_D': 0.45,  # Deployment
    'P_L': 0.60,  # Learning
    'P_I': 0.55   # Integration
})
print(f"Process Score: {process_score}")  # Output: 59.0

# Results assessment (LeTCI)
results_score = compute_letci_score({
    'R_Lv': 0.85,  # Levels
    'R_Tr': 0.90,  # Trends
    'R_Cp': 0.75,  # Comparisons
    'R_I': 0.70    # Integration
})
print(f"Results Score: {results_score}")  # Output: 81.25
```

### Complete Demonstration

```bash
python examples/complete_demo.py
```

Generates comprehensive analytics including:
- Category-level radar charts
- ADLI/LeTCI dimensional breakdowns
- Gap analysis heatmaps
- 3D performance evolution surfaces
- Interactive HTML dashboards

---

## Repository Structure

```
EdcellenceEdPEx/
├── src/
│   ├── algorithms/          # Core ADLI-LeTCI scoring
│   │   ├── adli_scoring.py
│   │   ├── letci_scoring.py
│   │   └── organizational_scoring.py
│   └── visualizations/      # 2D/3D visualization suite
│       └── scoring_visualizer.py
├── data/sample/             # Sample institutional data
├── examples/                # Complete demonstrations
├── notebooks/               # Jupyter analysis notebooks
└── tests/                   # Unit tests (pytest)
```

---

## Empirical Validation Results

**Deployment Context:** 24 organizational units, Thai higher education
**Period:** Academic year 2024--2025
**Statistical Method:** Paired t-tests, Bonferroni correction (α=0.0125)

| Metric | Baseline | Post-Implementation | Improvement | p-value | Effect Size |
|--------|----------|---------------------|-------------|---------|-------------|
| Assessment Cycle | 6.5 weeks | 2.0 weeks | **-69%** | <0.001 | d=3.2 |
| Documentation | 450 docs | 80 docs | **-82%** | <0.001 | d=3.8 |
| Consistency (α) | 0.62 | 0.88 | **+42%** | <0.001 | d=2.1 |
| Review Duration | 4.5 hrs | 2.5 hrs | **-44%** | <0.001 | d=2.4 |

**Technical Performance:**
- Category aggregation: 47±12ms
- Institution synthesis: 183±31ms
- Query success rate: 99.7%
- Algorithm validation: r=0.91 vs expert consensus (p<0.001)

---

## Visualization Capabilities

### 2D Visualizations
- **Radar Charts**: Multi-category performance profiles
- **Bar Charts**: ADLI/LeTCI dimensional breakdowns
- **Heatmaps**: Gap analysis across categories/items
- **Scatter Plots**: Priority matrices (impact vs gap)
- **Trend Lines**: Temporal performance evolution

### 3D Visualizations
- **Surface Plots**: Category performance over time
- **Interactive Dashboards**: Plotly-based exploration

All visualizations export to publication-quality PNG (300 DPI) and interactive HTML formats.

---

## Framework Integration

| Framework | Coverage | Integration Method |
|-----------|----------|-------------------|
| **EdPEx** | 7 categories, comprehensive organizational assessment | Primary framework, ADLI-LeTCI native |
| **TQF** | Curriculum quality, learning outcomes | Evidence routing via mapping layer |
| **AUN-QA v4** | Programme-level quality assurance | Consolidated evidence repository |

Organizations maintain **one unified evidence infrastructure** serving multiple assessment regimes simultaneously.

---

## Technical Architecture

### Backend
- **Language**: Python 3.8+ (NumPy, Pandas, SciPy)
- **Database**: PostgreSQL 13+ (138-table star schema)
- **API**: FastAPI with async support
- **Testing**: pytest (>85% coverage target)

### Visualization
- **Static**: Matplotlib, Seaborn
- **Interactive**: Plotly, Dash
- **3D**: mplot3d, Plotly 3D surface

### Deployment
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Documentation**: Sphinx

---

## Citation

If you use this framework in your research or practice, please cite:

```bibtex
@article{saosing2026excellence,
  title={From Excellence Guidelines to Computable Performance Systems:
         A Multi-Layer Computational Framework Based on ADLI--LeTCI Logic},
  author={Saosing, Rungtiva and Tritham, Chatchai and
          Tritham, Chattabhorn and Ngammongkolwong, Sudasawan},
  journal={IEEE ACCESS},
  year={2026},
  publisher={IEEE}
}
```

---

## Contribution

We welcome contributions from researchers and practitioners. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Areas of Interest:**
- Extension to ISO 21001, EFQM 2025
- Machine learning for automated evidence categorization
- Cross-sector validation studies
- Multi-language support

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

## Contact

**Corresponding Author:** Chatchai Tritham
📧 Email: chatchait66@nu.ac.th
🏛️ Affiliation: Faculty of Science and Technology, RMUTK
🌐 GitHub Issues: [Report bugs or request features](https://github.com/yourusername/EdcellenceEdPEx/issues)

---

## Acknowledgments

This research was supported by the Faculty of Science and Technology, Rajamangala University of Technology Krungthep, under fiscal budget year 2025.

We acknowledge:
- National Institute of Standards and Technology (NIST) - Baldrige Excellence Framework
- Office of the Higher Education Commission (OHEC) - EdPEx Framework
- ASEAN University Network - AUN-QA Standards

---

## Related Resources

- [Baldrige Excellence Framework](https://www.nist.gov/baldrige)
- [EdPEx Thailand](http://www.mua.go.th/edpex)
- [SQUIRE Guidelines (QI Reporting)](https://www.squire-statement.org/)
- [AUN-QA](https://www.aun-qa.org/)

---

**Last Updated:** February 2026
**Version:** 1.0.0
**Status:** Active Development
