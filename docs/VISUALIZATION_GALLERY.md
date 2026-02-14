# Visualization Gallery

**EdcellenceEdPEx Framework - Publication-Quality Visualizations**

---

## Overview

The EdcellenceEdPEx framework provides **17 distinct visualization types** across two modules:
- **Basic Visualizations** (8 types) - `scoring_visualizer.py`
- **Advanced Visualizations** (9 types) - `advanced_visualizer.py`

All visualizations are **publication-ready** with:
- **Static exports**: 300 DPI PNG for print publications
- **Interactive exports**: HTML with Plotly for digital supplements
- **Professional styling**: Academic journal quality

---

## Basic Visualizations (8 Types)

### 1. **Radar Chart** - Category Performance Profile
**File:** `01_radar_chart.png` (300 DPI PNG)

**Purpose:** Multi-dimensional performance comparison across 7 categories

**Features:**
- Current vs Target score comparison
- 7-axis radar plot
- Color-filled areas for easy comparison
- Professional gridlines and labels

**Use Cases:**
- Executive summaries
- Board presentations
- Annual reports
- IEEE ACCESS paper Figure 1

**Code Example:**
```python
from src.visualizations import ScoringVisualizer

viz = ScoringVisualizer()
viz.plot_category_scores_radar(
    category_scores={1: 75, 2: 68, 3: 82, 4: 70, 5: 74, 6: 69, 7: 87},
    target_scores={1: 85, 2: 80, 3: 90, 4: 80, 5: 85, 6: 80, 7: 95},
    save_path='radar_chart.png'
)
```

---

### 2. **ADLI Dimensional Breakdown** - Process Assessment
**File:** `02_adli_breakdown.png` (300 DPI PNG)

**Purpose:** Detailed breakdown of ADLI (Approach-Deployment-Learning-Integration) dimensions

**Features:**
- 4-bar chart (Approach, Deployment, Learning, Integration)
- Value labels on bars
- Color-coded dimensions
- Diagnostic insights

**Use Cases:**
- Process category analysis (Categories 1-6)
- Improvement planning
- Departmental reviews
- Research paper methodology figures

**Code Example:**
```python
viz.plot_adli_breakdown(
    adli_scores={'Approach': 22.5, 'Deployment': 13.5, 'Learning': 12.0, 'Integration': 11.0},
    title="ADLI Dimensional Breakdown - Strategy Category",
    save_path='adli_breakdown.png'
)
```

---

### 3. **LeTCI Dimensional Breakdown** - Results Assessment
**File:** `03_letci_breakdown.png` (300 DPI PNG)

**Purpose:** Detailed breakdown of LeTCI (Levels-Trends-Comparisons-Integration) dimensions

**Features:**
- 4-bar chart (Levels, Trends, Comparisons, Integration)
- Value labels and color coding
- Results-specific analysis
- Performance indicators

**Use Cases:**
- Results category analysis (Category 7)
- Outcome tracking
- Benchmark comparisons
- Research validation figures

**Code Example:**
```python
viz.plot_letci_breakdown(
    letci_scores={'Levels': 29.75, 'Trends': 22.5, 'Comparisons': 18.75, 'Integration': 10.5},
    title="LeTCI Dimensional Breakdown - Results Category",
    save_path='letci_breakdown.png'
)
```

---

### 4. **Gap Analysis Heatmap** - Priority Identification
**File:** `04_gap_heatmap.png` (300 DPI PNG)

**Purpose:** Visual identification of performance gaps across categories and items

**Features:**
- Color-coded severity (green=on track, yellow=monitor, red=critical)
- 7×N matrix (categories × items)
- Annotated values
- Hierarchical clustering

**Use Cases:**
- Improvement prioritization
- Resource allocation planning
- Risk assessment
- Management dashboards

**Code Example:**
```python
gap_df = pd.DataFrame({
    'category': [1,1,1,2,2,2,3,3,3],
    'item': [1,2,3,1,2,3,1,2,3],
    'gap': [10, 15, 7, 20, 18, 12, 8, 5, 10]
})
viz.plot_gap_analysis_heatmap(gap_df, save_path='gap_heatmap.png')
```

---

### 5. **Priority Matrix** - Impact vs Gap Analysis
**File:** `05_priority_matrix.png` (300 DPI PNG)

**Purpose:** 2D prioritization using impact and gap dimensions

**Features:**
- Scatter plot with quadrants
- Category-specific color coding
- Quadrant labels (High Priority, Quick Wins, Monitor, Low Priority)
- Median lines for segmentation

**Use Cases:**
- Strategic planning
- Project prioritization
- Budget allocation
- Executive decision support

**Code Example:**
```python
viz.plot_priority_matrix(gap_df, save_path='priority_matrix.png')
```

---

### 6. **3D Surface Plot** - Temporal Evolution
**File:** `06_3d_evolution.png` (300 DPI PNG)

**Purpose:** 3D visualization of category performance over time

**Features:**
- 3D surface with color gradient
- Time × Category × Score dimensions
- Rotation for optimal viewing
- Contour projections

**Use Cases:**
- Multi-year trend analysis
- Performance evolution studies
- Longitudinal research
- Predictive modeling visualization

**Code Example:**
```python
historical = {
    '2020-2021': {1: 65, 2: 58, 3: 70, 4: 60, 5: 66, 6: 62, 7: 75},
    '2021-2022': {1: 68, 2: 62, 3: 74, 4: 64, 5: 69, 6: 65, 7: 79},
    # ... more years
}
viz.plot_3d_category_surface(historical, save_path='3d_evolution.png')
```

---

### 7. **Interactive Scorecard** - Real-time Dashboard
**File:** `07_interactive_scorecard.html` (Interactive HTML)

**Purpose:** Interactive organizational scorecard with drill-down

**Features:**
- Bar chart + Pie chart combination
- Hover tooltips
- Interactive legend
- Responsive design

**Use Cases:**
- Web dashboards
- Digital reports
- Supplementary materials
- Stakeholder presentations

**Code Example:**
```python
scorecard = {
    'organizational_score': 74.5,
    'category_scores': {1: 75, 2: 68, 3: 82, 4: 70, 5: 74, 6: 69, 7: 87},
    'category_names': {...}
}
viz.create_interactive_scorecard(scorecard, save_path='scorecard.html')
```

---

### 8. **Trend Analysis** - Category-specific Evolution
**File:** Dynamic filename (PNG)

**Purpose:** Temporal trend with regression line

**Features:**
- Line plot with markers
- Linear regression trend
- Slope annotation
- Period labels

**Use Cases:**
- Single-category deep dive
- Improvement tracking
- Forecasting
- Performance monitoring

---

## Advanced Visualizations (9 Types)

### 9. **Distribution Comparison** - Box + Violin Plots
**File:** `08_distribution_comparison.png` (300 DPI PNG)

**Purpose:** Statistical distribution analysis across categories

**Features:**
- **Box plots**: Quartiles, median, outliers, mean
- **Violin plots**: Density distributions
- Side-by-side comparison
- Statistical annotations

**Use Cases:**
- Variability analysis
- Outlier detection
- Distribution shape comparison
- Statistical research papers

**Code Example:**
```python
from src.visualizations import AdvancedVisualizer

viz = AdvancedVisualizer()
score_distributions = {
    'Leadership': [75, 72, 78, 74, 76],
    'Strategy': [65, 59, 70, 68, 67],
    # ... more categories
}
viz.plot_distribution_comparison(score_distributions, save_path='distributions.png')
```

---

### 10. **Correlation Matrix** - Inter-category Relationships
**File:** `09_correlation_matrix.png` (300 DPI PNG)

**Purpose:** Pearson correlation analysis between categories

**Features:**
- Lower-triangle heatmap
- Annotated coefficients
- Color-coded strength (-1 to +1)
- Hierarchical clustering

**Use Cases:**
- Dependency analysis
- System dynamics studies
- Predictive modeling
- Structural equation modeling

**Code Example:**
```python
correlation_data = pd.DataFrame({
    'Cat1': [75, 68, 71, 73, 75],
    'Cat2': [68, 62, 65, 67, 68],
    # ... more categories over time
})
viz.plot_correlation_matrix(correlation_data, save_path='correlation.png')
```

---

### 11. **Network Diagram** - Category Dependencies
**File:** `10_network_diagram.png` (300 DPI PNG)

**Purpose:** Graph visualization of BEB-EdPEx category dependencies

**Features:**
- Directed graph with arrows
- Node size proportional to score
- Color gradient by performance
- Spring layout algorithm
- Edge weights

**Use Cases:**
- Systems thinking visualization
- Dependency mapping
- Impact analysis
- Organizational architecture

**Code Example:**
```python
dependencies = [(1,2), (2,5), (2,6), (5,4), (6,4), (4,7)]
category_names = {1: 'Leadership', 2: 'Strategy', ...}
viz.plot_category_network(
    category_scores, dependencies, category_names,
    save_path='network.png'
)
```

---

### 12. **Sunburst Chart** - Hierarchical Structure
**File:** `11_sunburst_hierarchy.html` (Interactive HTML)

**Purpose:** Interactive hierarchical visualization (Organization → Categories → Items)

**Features:**
- 3-level hierarchy
- Click-to-zoom drill-down
- Color-coded by score
- Proportional sizing
- Hover details

**Use Cases:**
- Organizational structure
- Contribution analysis
- Hierarchical decomposition
- Interactive reports

**Code Example:**
```python
hierarchical_data = {
    'labels': ['Organization', 'Leadership', 'L1', 'L2', 'L3', ...],
    'parents': ['', 'Organization', 'Leadership', ...],
    'values': [0, 75, 75, 72, 78, ...]
}
viz.create_sunburst_chart(hierarchical_data, save_path='sunburst.html')
```

---

### 13. **Sankey Diagram** - Flow Analysis
**File:** `12_sankey_flow.html` (Interactive HTML)

**Purpose:** Flow visualization showing category contributions to overall score

**Features:**
- Flow width proportional to value
- Interactive hover
- Color-coded flows
- Source-target relationships

**Use Cases:**
- Contribution analysis
- Value flow mapping
- Process flow visualization
- Resource allocation studies

**Code Example:**
```python
flow_data = {
    'labels': ['Leadership (75)', 'Strategy (68)', ..., 'Overall'],
    'source': [0, 1, 2, 3, 4, 5, 6],
    'target': [7, 7, 7, 7, 7, 7, 7],
    'value': [75, 68, 82, 70, 74, 69, 87]
}
viz.create_sankey_diagram(flow_data, save_path='sankey.html')
```

---

### 14. **Temporal Decomposition** - Time Series Analysis
**Files:** `13_decomposition_cat[1-7].png` (300 DPI PNG)

**Purpose:** Decompose time series into components

**Features:**
- **Original series** - Raw data with markers
- **Trend component** - Moving average
- **Detrended** - Seasonal variations
- **Residuals** - Noise and irregularities

**Use Cases:**
- Trend extraction
- Seasonal analysis
- Forecasting preparation
- Anomaly detection

**Code Example:**
```python
time_series = pd.DataFrame({
    'period': ['2020-2021', '2021-2022', ...],
    'score': [65, 68, 71, 73, 75]
})
viz.plot_temporal_decomposition(time_series, 'Leadership', save_path='decomp.png')
```

---

### 15. **3D Scatter (Interactive)** - ADLI Dimensional Analysis
**File:** `14_3d_scatter_adli.html` (Interactive HTML)

**Purpose:** 3D visualization of ADLI dimensions with interactivity

**Features:**
- 3D coordinates: Approach, Deployment, Learning
- Color-coded by score
- Fully interactive (rotate, zoom, pan)
- Hover tooltips
- Category filtering

**Use Cases:**
- Multivariate analysis
- Pattern recognition
- Cluster identification
- Interactive exploration

**Code Example:**
```python
scatter_data = pd.DataFrame({
    'Approach': [80, 75, 70, ...],
    'Deployment': [70, 68, 66, ...],
    'Learning': [75, 72, 70, ...],
    'Score': [75, 72, 68, ...]
})
viz.create_3d_scatter_interactive(
    scatter_data, 'Approach', 'Deployment', 'Learning', 'Score',
    save_path='3d_scatter.html'
)
```

---

### 16. **Statistical Summary Panel** - Comprehensive Stats
**File:** `15_statistical_summary.png` (300 DPI PNG)

**Purpose:** 4-panel statistical analysis dashboard

**Panels:**
1. **Mean with 95% CI** - Central tendency with confidence intervals
2. **Coefficient of Variation** - Relative variability (CV%)
3. **Min-Max Range** - Score spread
4. **Quartile Distribution** - Q1, Median, Q3 visualization

**Use Cases:**
- Statistical reporting
- Variability assessment
- Quality control
- Research methodology

**Code Example:**
```python
viz.plot_statistical_summary(score_distributions, save_path='stats.png')
```

---

### 17. **Parallel Coordinates** - Multivariate Analysis
**File:** `16_parallel_coordinates.html` (Interactive HTML)

**Purpose:** Simultaneous visualization of multiple dimensions

**Features:**
- 7 parallel axes (all categories)
- Interactive filtering
- Color-coded by overall score
- Pattern recognition for correlations
- Brushing and linking

**Use Cases:**
- Multivariate analysis
- Pattern detection
- Outlier identification
- Comparative profiling

**Code Example:**
```python
parallel_data = pd.DataFrame({
    'Leadership': [75, 68, ...],
    'Strategy': [68, 62, ...],
    # ... all 7 categories
    'Overall': [74.5, 70.2, ...]
})
dimensions = ['Leadership', 'Strategy', 'Customers', ...]
viz.create_parallel_coordinates(
    parallel_data, dimensions, 'Overall',
    save_path='parallel.html'
)
```

---

## Visualization Summary Table

| # | Visualization Type | File Format | Module | Primary Use |
|---|-------------------|-------------|--------|-------------|
| 1 | Radar Chart | PNG (300 DPI) | Basic | Category comparison |
| 2 | ADLI Breakdown | PNG (300 DPI) | Basic | Process analysis |
| 3 | LeTCI Breakdown | PNG (300 DPI) | Basic | Results analysis |
| 4 | Gap Heatmap | PNG (300 DPI) | Basic | Priority identification |
| 5 | Priority Matrix | PNG (300 DPI) | Basic | Strategic planning |
| 6 | 3D Surface | PNG (300 DPI) | Basic | Temporal evolution |
| 7 | Interactive Scorecard | HTML | Basic | Digital dashboard |
| 8 | Trend Analysis | PNG (300 DPI) | Basic | Time series |
| 9 | Distribution (Box+Violin) | PNG (300 DPI) | Advanced | Statistical analysis |
| 10 | Correlation Matrix | PNG (300 DPI) | Advanced | Relationships |
| 11 | Network Diagram | PNG (300 DPI) | Advanced | Dependencies |
| 12 | Sunburst Chart | HTML | Advanced | Hierarchy |
| 13 | Sankey Diagram | HTML | Advanced | Flow analysis |
| 14 | Temporal Decomposition | PNG (300 DPI) | Advanced | Time series components |
| 15 | 3D Scatter | HTML | Advanced | Multivariate 3D |
| 16 | Statistical Summary | PNG (300 DPI) | Advanced | Comprehensive stats |
| 17 | Parallel Coordinates | HTML | Advanced | Multivariate patterns |

---

## Usage Examples

### Quick Start - Generate All Visualizations

```bash
# Basic visualizations
python examples/complete_demo.py

# Advanced visualizations
python examples/advanced_visualizations_demo.py
```

### Custom Visualization Pipeline

```python
from src.visualizations import ScoringVisualizer, AdvancedVisualizer
import pandas as pd

# Initialize visualizers
basic_viz = ScoringVisualizer()
advanced_viz = AdvancedVisualizer()

# Load your data
category_scores = {...}  # Your scores

# Generate publication-ready figures
basic_viz.plot_category_scores_radar(category_scores, save_path='fig1.png')
advanced_viz.plot_statistical_summary(distributions, save_path='fig2.png')
advanced_viz.create_3d_scatter_interactive(data, ..., save_path='fig3.html')
```

---

## Publication Guidelines

### For IEEE ACCESS Paper

**Recommended Figures (Main Text):**
1. **Figure 1:** Radar Chart - Overall organizational profile
2. **Figure 2:** 3D Surface Plot - Temporal evolution
3. **Figure 3:** Network Diagram - Category dependencies
4. **Figure 4:** Gap Heatmap - Priority identification
5. **Figure 5:** Statistical Summary - Empirical validation

**Supplementary Materials:**
- All interactive HTML visualizations
- Additional statistical plots
- Temporal decomposition series
- Detailed dimensional breakdowns

### Quality Standards

- **Resolution:** 300 DPI minimum for print
- **Format:** PNG for static, HTML for interactive
- **Color:** RGB for digital, CMYK conversion for print
- **Size:** Minimum 1200px width for figures
- **Labels:** Clear, professional fonts (≥10pt)
- **Citations:** Include visualization type in figure captions

---

## Technical Specifications

### Dependencies
```
matplotlib >= 3.7.0
seaborn >= 0.13.0
plotly >= 5.18.0
networkx >= 3.1
scipy >= 1.10.0
pandas >= 2.0.0
numpy >= 1.24.0
```

### Performance
- **Static plots:** ~1-3 seconds per figure
- **Interactive plots:** ~2-5 seconds per figure
- **Batch generation:** Parallel processing supported
- **Memory:** < 500 MB per visualization

### Output Specifications
- **PNG:** 300 DPI, RGB color space, transparent background optional
- **HTML:** Plotly.js embedded, responsive layout, modern browser compatibility
- **File sizes:** PNG ~500KB-2MB, HTML ~1-3MB

---

## Authors

**Research Team:**
- Rungtiva Saosing (RMUTK)
- Chatchai Tritham (RMUTK & AppVisor)
- Chattabhorn Tritham (Thammasat University & AppVisor)
- Sudasawan Ngammongkolwong (Southeast Bangkok University)

**Citation:**
```bibtex
@article{saosing2026excellence,
  title={From Excellence Guidelines to Computable Performance Systems},
  author={Saosing et al.},
  journal={IEEE ACCESS},
  year={2026}
}
```

---

**Last Updated:** February 2026
**Framework Version:** 1.0.0
**Documentation Status:** Complete
