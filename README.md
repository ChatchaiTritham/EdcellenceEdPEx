# EdcellenceEdPEx
### From Excellence Guidelines to Computable Performance Systems
**A Multi-Layer Computational Framework Based on ADLI--LeTCI Logic**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)](https://www.postgresql.org/)
[![React](https://img.shields.io/badge/React-18+-blue.svg)](https://reactjs.org/)

---

## 📖 Overview

**EdcellenceEdPEx** transforms abstract organizational excellence frameworks (EdPEx, Baldrige) into executable computational systems through mathematical formalization of ADLI-LeTCI evaluation logic.

This framework enables:
- ✅ **Automated assessment** of organizational performance using ADLI (Approach-Deployment-Learning-Integration) logic
- ✅ **Real-time dashboards** for multi-framework quality governance (EdPEx, TQF, AUN-QA)
- ✅ **Unified evidence infrastructure** eliminating duplicative documentation across compliance regimes
- ✅ **Quantitative validation** with statistical rigor (Cohen's d = 2.1-3.8, p < 0.001)

---

## 🎯 Key Features

### 1. Mathematical Formalization
- **ADLI Process Evaluation**: `S_item[c,i] = 100 × (w_A·P_A + w_D·P_D + w_L·P_L + w_I·P_I)`
- **LeTCI Outcome Assessment**: `S_item[7,i] = 100 × (w_Lv·R_Lv + w_Tr·R_Tr + w_Cp·R_Cp + w_I·R_I)`
- **Integration Health Index**: Cross-category coherence measurement
- **Gap Analysis**: Automated prioritization of improvement initiatives

### 2. Multi-Framework Integration
| Framework | Coverage | Purpose |
|-----------|----------|---------|
| **EdPEx** | Organizational excellence | National assessment (Thailand) |
| **TQF** | Curriculum quality | Regulatory compliance |
| **AUN-QA v4** | Programme quality | International accreditation |

### 3. Technical Performance
- ⚡ **Category-level aggregations**: 47±12ms
- ⚡ **Institution-level syntheses**: 183±31ms
- ⚡ **Query success rate**: 99.7%
- 📊 **Database schema**: 138-table star schema
- 🎨 **Frontend**: React dashboard with real-time updates

### 4. Empirical Validation
Deployment across 24 organizational units yielded:
- 📉 **69% reduction** in assessment cycle duration (6.5 → 2.0 weeks, p<0.001)
- 📉 **82% reduction** in documentation artifacts (450 → 80 documents, p<0.001)
- 📈 **42% improvement** in measurement consistency (Cronbach's α: 0.62 → 0.88, p<0.001)
- 💪 **Large effect sizes**: Cohen's d = 2.1-3.8

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    BEB-EdPEx Framework                       │
├─────────────────────────────────────────────────────────────┤
│  System Drivers       │  Leadership (Cat. 1)                │
│                       │  Strategy (Cat. 2)                   │
├─────────────────────────────────────────────────────────────┤
│  Execution Systems    │  Customers (Cat. 3)                 │
│                       │  Workforce (Cat. 5)                  │
│                       │  Operations (Cat. 6)                 │
├─────────────────────────────────────────────────────────────┤
│  Enabling Layer       │  Measurement & KM (Cat. 4)          │
├─────────────────────────────────────────────────────────────┤
│  System Outputs       │  Results (Cat. 7)                   │
└─────────────────────────────────────────────────────────────┘
           ↑                                    ↓
      Feedback Loop (Review & Learning)
```

---

## 🚀 Quick Start

### Prerequisites
- **Python** 3.8+
- **PostgreSQL** 13+
- **Node.js** 16+ (for React dashboard)

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/EdcellenceEdPEx.git
cd EdcellenceEdPEx

# Install Python dependencies
pip install -r requirements.txt

# Set up database
psql -U postgres -f data/schemas/create_database.sql

# Install dashboard dependencies
cd src/dashboard
npm install

# Run migrations
python scripts/migrate_database.py
```

### Running the System

```bash
# Start API server
python src/api/server.py

# Start dashboard (in separate terminal)
cd src/dashboard
npm start
```

Access dashboard at: `http://localhost:3000`

---

## 📊 Usage Example

### 1. Compute ADLI Score for a Process Item

```python
from src.algorithms.adli_scoring import compute_adli_score

# Define normalized indicators [0, 1]
indicators = {
    'P_A': 0.75,  # Approach adequacy
    'P_D': 0.45,  # Deployment consistency
    'P_L': 0.60,  # Learning effectiveness
    'P_I': 0.55   # Integration
}

# Compute score
score = compute_adli_score(indicators)
print(f"ADLI Score: {score}")  # Output: 59
```

### 2. Generate Organizational Scorecard

```python
from src.api.scorecard import generate_scorecard

scorecard = generate_scorecard(
    organization_id=1,
    period='2024-2025',
    categories=[1, 2, 3, 4, 5, 6, 7]
)

print(scorecard.to_json())
```

### 3. Run Gap Analysis

```python
from src.algorithms.gap_analysis import prioritize_improvements

priorities = prioritize_improvements(
    current_scores=scores,
    target_scores=targets,
    criticality_matrix=criticality,
    risk_matrix=risks
)

for item in priorities[:5]:  # Top 5 priorities
    print(f"{item['category']}.{item['item']}: Gap={item['gap']}, Priority={item['priority']}")
```

---

## 📁 Repository Structure

```
EdcellenceEdPEx/
├── src/
│   ├── algorithms/          # ADLI-LeTCI scoring algorithms
│   │   ├── adli_scoring.py
│   │   ├── letci_scoring.py
│   │   ├── gap_analysis.py
│   │   └── integration_health.py
│   ├── database/            # Database schemas & migrations
│   │   ├── models/
│   │   └── migrations/
│   ├── api/                 # REST API endpoints
│   │   ├── server.py
│   │   ├── routes/
│   │   └── controllers/
│   └── dashboard/           # React dashboard UI
│       ├── src/
│       ├── public/
│       └── package.json
├── data/
│   ├── schemas/             # Database schema definitions
│   │   └── create_database.sql
│   └── sample/              # Sample datasets
│       └── sample_data.json
├── docs/
│   ├── ADLI_LETCI_Specification.md
│   ├── API_Reference.md
│   ├── Database_Schema.md
│   └── Deployment_Guide.md
├── tests/
│   ├── test_algorithms.py
│   ├── test_api.py
│   └── test_integration.py
├── scripts/
│   ├── migrate_database.py
│   └── seed_data.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 📚 Documentation

- **[ADLI-LeTCI Specification](docs/ADLI_LETCI_Specification.md)**: Mathematical formalization details
- **[API Reference](docs/API_Reference.md)**: REST API endpoints and usage
- **[Database Schema](docs/Database_Schema.md)**: 138-table star schema documentation
- **[Deployment Guide](docs/Deployment_Guide.md)**: Production deployment instructions

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run specific test suite
pytest tests/test_algorithms.py

# Run with coverage
pytest --cov=src tests/
```

**Test Coverage**: > 85%

---

## 🎓 Academic Reference

This repository implements the computational framework described in:

> Saosing, R., Tritham, C., Tritham, C., & Ngammongkolwong, S. (2026).
> **From Excellence Guidelines to Computable Performance Systems: A Multi-Layer Computational Framework Based on ADLI--LeTCI Logic.**
> *IEEE ACCESS* (under review).

**BibTeX Citation:**
```bibtex
@article{saosing2026excellence,
  title={From Excellence Guidelines to Computable Performance Systems: A Multi-Layer Computational Framework Based on ADLI--LeTCI Logic},
  author={Saosing, Rungtiva and Tritham, Chatchai and Tritham, Chattabhorn and Ngammongkolwong, Sudasawan},
  journal={IEEE ACCESS},
  year={2026},
  note={Under review}
}
```

---

## 📊 Performance Benchmarks

| Metric | Baseline | Post-Implementation | Improvement |
|--------|----------|---------------------|-------------|
| **Assessment Cycle Duration** | 6.5 weeks | 2.0 weeks | **-69%** (p<0.001) |
| **Document Artifacts** | 450 docs | 80 docs | **-82%** (p<0.001) |
| **Measurement Consistency** | α=0.62 | α=0.88 | **+42%** (p<0.001) |
| **Review Duration** | 4.5 hrs | 2.5 hrs | **-44%** (p<0.001) |
| **Query Response Time** | N/A | 47±12ms | Category-level |
| **Institution Synthesis** | N/A | 183±31ms | Full aggregation |

**Effect Sizes**: Cohen's d = 2.1-3.8 (very large)

---

## 🛠️ Technology Stack

### Backend
- **Language**: Python 3.8+
- **Framework**: Flask / FastAPI
- **Database**: PostgreSQL 13+
- **ORM**: SQLAlchemy
- **Analytics**: NumPy, Pandas, SciPy

### Frontend
- **Framework**: React 18+
- **State Management**: Redux / Context API
- **UI Library**: Material-UI / Ant Design
- **Visualization**: Recharts / D3.js
- **Build Tool**: Vite / Create React App

### DevOps
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Testing**: pytest, Jest
- **Documentation**: Sphinx, JSDoc

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Rungtiva Saosing** - Faculty of Science and Technology, RMUTK
- **Chatchai Tritham** - International College, RMUTK & AppVisor
- **Chattabhorn Tritham** - Thammasat School of Engineering & AppVisor
- **Sudasawan Ngammongkolwong** - Southeast Bangkok University

---

## 🙏 Acknowledgments

- Faculty of Science and Technology, Rajamangala University of Technology Krungthep
- National Institute of Standards and Technology (NIST) - Baldrige Excellence Framework
- Office of the Higher Education Commission (OHEC) - EdPEx Framework
- ASEAN University Network - AUN-QA Standards

---

## 📧 Contact

**Corresponding Author**: Chatchai Tritham
📧 Email: chatchait66@nu.ac.th
🌐 Website: [Coming Soon]
📝 Issues: [GitHub Issues](https://github.com/yourusername/EdcellenceEdPEx/issues)

---

## 🔗 Related Resources

- [Baldrige Excellence Framework](https://www.nist.gov/baldrige)
- [EdPEx Thailand](http://www.mua.go.th/edpex)
- [SQUIRE Guidelines](https://www.squire-statement.org/)
- [AUN-QA](https://www.aun-qa.org/)

---

## 📈 Roadmap

### Version 1.0 (Current)
- ✅ Core ADLI-LeTCI algorithms
- ✅ PostgreSQL database schema
- ✅ REST API endpoints
- ✅ React dashboard MVP

### Version 2.0 (Planned)
- 🔲 Machine learning for automated evidence categorization
- 🔲 Natural language processing for narrative report interpretation
- 🔲 Predictive modeling for performance projection
- 🔲 Mobile app (iOS/Android)
- 🔲 Multi-language support (Thai, English)

### Version 3.0 (Future)
- 🔲 Integration with ISO 21001, EFQM 2025
- 🔲 Cloud-native deployment (AWS, Azure, GCP)
- 🔲 AI-powered recommendation engine
- 🔲 Blockchain-based audit trail

---

**⭐ If you find this project useful, please consider giving it a star!**

---

*Last Updated: February 14, 2026*
