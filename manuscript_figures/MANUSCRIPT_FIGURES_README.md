# Manuscript Figures for IEEE ACCESS Submission

## From Excellence Guidelines to Computable Performance Systems: BEB-EdPEx Framework for Higher Education

**Authors:** Rungtiva Saosing, Chatchai Tritham, Chattabhorn Tritham, Sudasawan Ngammongkolwong
**Affiliation:** Faculty of Science and Technology, Rajamangala University of Technology Krungthep
**Journal:** IEEE ACCESS
**Date:** February 2026

---

## Figure Inventory

This directory contains 15 publication-ready figures for the manuscript. All figures are 300 DPI PNG format, suitable for IEEE ACCESS submission requirements.

### Framework Overview (Figures 1-3)

| Figure | Filename | Description | Size |
|--------|----------|-------------|------|
| **Figure 1** | `Fig1_BEB-EdPEx_Category_Performance_Radar.png` | Radar chart showing organizational performance across all 7 BEB-EdPEx categories (Leadership, Strategy, Customers, Measurement, Workforce, Operations, Results). Demonstrates balanced performance profile with Results category showing highest scores (87/100). | 522 KB |
| **Figure 2** | `Fig2_ADLI_Process_Scoring_Breakdown.png` | ADLI (Approach-Deployment-Learning-Integration) dimensional breakdown for process categories (1-6). Illustrates weighted scoring algorithm with weights: Approach 30%, Deployment 30%, Learning 20%, Integration 20%. | 78 KB |
| **Figure 3** | `Fig3_LeTCI_Results_Scoring_Breakdown.png` | LeTCI (Levels-Trends-Comparisons-Integration) dimensional breakdown for Results category (7). Shows weighted scoring with: Levels 35%, Trends 25%, Comparisons 25%, Integration 15%. | 80 KB |

### Gap Analysis & Improvement Prioritization (Figures 4-5)

| Figure | Filename | Description | Size |
|--------|----------|-------------|------|
| **Figure 4** | `Fig4_Performance_Gap_Analysis_Heatmap.png` | Heatmap visualization of performance gaps between current scores and 2025 targets across all categories and items. Color-coded intensity indicates gap severity (red = critical gap >20 points, yellow = monitor 10-20 points, green = on track <10 points). | 178 KB |
| **Figure 5** | `Fig5_Improvement_Priority_Matrix.png` | Strategic priority matrix plotting gap size vs. category weight. Identifies high-priority improvement areas requiring immediate intervention. Strategy category shows largest weighted gap (12 points × 0.12 weight = 1.44 priority score). | 222 KB |

### Temporal Analysis (Figures 6-7)

| Figure | Filename | Description | Size |
|--------|----------|-------------|------|
| **Figure 6** | `Fig6_Five_Year_Performance_Trends_2020_2025.png` | Multi-category trend analysis showing 5-year performance evolution (Academic Years 2020-2025). All 7 categories demonstrate consistent upward trends averaging 2-4 points/year. Results category shows steepest growth (75→87 points, +16% over 5 years). | 344 KB |
| **Figure 7** | `Fig7_Three_Dimensional_Category_Evolution.png` | 3D surface plot depicting temporal evolution of all categories simultaneously. Z-axis shows scores (0-100), X-axis shows categories (1-7), Y-axis shows years (2020-2025). Reveals synchronized improvement patterns across organizational categories. | 644 KB |

### Statistical Distributions & Correlations (Figures 8-10)

| Figure | Filename | Description | Size |
|--------|----------|-------------|------|
| **Figure 8** | `Fig8_Category_Score_Distributions_BoxViolin.png` | Combined box-and-violin plots showing score distributions for all 7 categories. Box plots display quartiles and outliers; violin plots show probability density. Results category exhibits lowest variance (CV=8.2%), indicating consistent high performance. | 309 KB |
| **Figure 9** | `Fig9_Category_Performance_Correlation_Matrix.png` | Pearson correlation heatmap analyzing interdependencies between category performances (2020-2025 historical data). Strong positive correlation (r=0.96) between Leadership and Strategy indicates systemic alignment. Results category shows moderate correlation with process categories (r=0.65-0.78). | 162 KB |
| **Figure 10** | `Fig10_BEB_EdPEx_Category_Dependency_Network.png` | Network diagram visualizing process flow and dependencies between BEB-EdPEx categories. Node size proportional to category score; edge thickness represents dependency strength. Results (Category 7) serves as convergence point for all process chains, consistent with Baldrige framework philosophy. | 394 KB |

### Temporal Decomposition Analysis (Figures 11-13)

| Figure | Filename | Description | Size |
|--------|----------|-------------|------|
| **Figure 11** | `Fig11_Temporal_Decomposition_Leadership.png` | Seasonal decomposition of Leadership category (2020-2025): trend component (+1.67 points/year), seasonal patterns (±2.3 points amplitude), and residual noise (σ=0.8). Demonstrates stable upward trajectory with minimal volatility. | 299 KB |
| **Figure 12** | `Fig12_Temporal_Decomposition_Strategy.png` | Strategy category temporal decomposition revealing consistent trend (+1.67 points/year) with moderate seasonal fluctuation (±3.1 points). Higher residual variance (σ=1.2) reflects implementation challenges. | 310 KB |
| **Figure 13** | `Fig13_Temporal_Decomposition_Customers.png` | Customers category decomposition showing strongest upward trend (+2.0 points/year) among process categories. Low seasonal variation (±1.8 points) indicates stable stakeholder engagement. | 296 KB |

### Statistical Validation (Figures 14-15)

| Figure | Filename | Description | Size |
|--------|----------|-------------|------|
| **Figure 14** | `Fig14_Statistical_Summary_95CI.png` | Statistical summary panel displaying means, standard deviations, and 95% confidence intervals for all 7 categories based on 24 organizational units (n=168 observations). Error bars represent ±1.96 SE. All categories show tight confidence intervals (max width=4.2 points), validating measurement reliability. | 490 KB |
| **Figure 15** | `Fig15_Empirical_Validation_Results.png` | Quantitative impact assessment comparing baseline vs. post-implementation metrics across 24 organizational units (Academic Year 2024-2025). Key findings: Assessment cycle duration reduced 69% (6.5→2.0 weeks, p<0.001, Cohen's d=3.2), documentation reduced 82% (450→80 artifacts, d=3.8), measurement consistency improved 42% (α=0.62→0.88, d=2.1), review time reduced 44% (4.5→2.5 hours, d=2.4). All effects statistically significant with large effect sizes. | 162 KB |

---

## Technical Specifications

### Image Format & Resolution
- **Format:** PNG (Portable Network Graphics)
- **Resolution:** 300 DPI (IEEE ACCESS requirement)
- **Color Space:** RGB
- **Bit Depth:** 24-bit (8 bits per channel)
- **Compression:** Lossless PNG compression

### Figure Dimensions
- **Typical Width:** 3600-4800 pixels (12-16 inches at 300 DPI)
- **Typical Height:** 2100-2400 pixels (7-8 inches at 300 DPI)
- **Aspect Ratio:** Varies by visualization type (typically 16:9 or 4:3)

### Software Used
- **Matplotlib:** 3.9.3 (static charts)
- **Seaborn:** 0.13.2 (statistical plots)
- **Plotly:** 5.24.1 (interactive charts, exported to PNG)
- **NetworkX:** 3.4.2 (network diagrams)
- **Python:** 3.13.12

### Font Specifications
- **Headings:** 14-16pt, bold
- **Axis Labels:** 12pt, bold
- **Tick Labels:** 10pt
- **Legends:** 10-11pt
- **Font Family:** DejaVu Sans (standard matplotlib font)

---

## Figure Usage Guidelines

### In-Text Citation Format

Use the following format when citing figures in the manuscript text:

```
As shown in Figure 1, organizational performance across all seven BEB-EdPEx
categories demonstrates balanced development with Results category achieving
the highest score (87/100).

The ADLI scoring algorithm (Figure 2) employs weighted dimensional assessment
with Approach and Deployment each contributing 30% to the final score, while
Learning and Integration contribute 20% each.

Figure 6 presents five-year performance trends (2020-2025), revealing consistent
upward trajectories across all categories with an average annual improvement
of 2-4 points.
```

### Caption Templates

**Standard Caption Format:**
```
Figure X. [Brief title]. [Detailed description including methodology, sample size,
statistical measures, and key findings]. [Data source/period if applicable].
```

**Example Captions:**

**Figure 1 Caption:**
```
Figure 1. Organizational Performance Radar Chart Across Seven BEB-EdPEx Categories.
The radar chart displays current performance scores for Leadership (75), Strategy (68),
Customers (82), Measurement (70), Workforce (75), Operations (69), and Results (87).
The Results category achieves the highest score, reflecting strong outcome-oriented
performance, while Strategy shows the largest improvement opportunity. Assessment
period: Academic Year 2024-2025, n=24 organizational units.
```

**Figure 6 Caption:**
```
Figure 6. Five-Year Performance Trend Analysis (2020-2025). Multi-category trend
lines illustrate annual performance evolution across all seven BEB-EdPEx categories.
All categories demonstrate consistent upward trends averaging 2-4 points per academic
year. The Results category exhibits the steepest growth trajectory, improving from
75 to 87 points (+16% over five years). Linear regression slopes range from +1.67
to +2.0 points/year, all statistically significant (p<0.001).
```

**Figure 15 Caption:**
```
Figure 15. Empirical Validation Results: Baseline vs. Post-Implementation Comparison.
Quantitative impact assessment across 24 organizational units (Academic Year 2024-2025)
demonstrating significant improvements in four key operational metrics. Assessment
cycle duration decreased 69% (6.5 to 2.0 weeks, p<0.001, Cohen's d=3.2), documentation
artifacts reduced 82% (450 to 80 documents, d=3.8), measurement consistency improved
42% (Cronbach's α from 0.62 to 0.88, d=2.1), and review duration decreased 44%
(4.5 to 2.5 hours, d=2.4). All changes statistically significant with large effect
sizes (d>2.0), validating framework effectiveness.
```

---

## Manuscript Integration Checklist

### Pre-Submission Verification

- [ ] All 15 figures present and correctly numbered (Fig1-Fig15)
- [ ] All figures meet 300 DPI resolution requirement
- [ ] File sizes appropriate for submission (<1 MB each except Fig7)
- [ ] Figures referenced in manuscript text in sequential order
- [ ] All figures have complete captions with methodology details
- [ ] Statistical measures (p-values, effect sizes, n) included in captions
- [ ] Color schemes accessible to colorblind readers (verified)
- [ ] Font sizes legible when printed (minimum 10pt)
- [ ] Axis labels and legends properly positioned
- [ ] No proprietary or sensitive data displayed

### IEEE ACCESS Specific Requirements

- [ ] Figures submitted as separate files (not embedded in manuscript)
- [ ] File naming convention: `FigX_descriptive_name.png`
- [ ] RGB color mode (not CMYK)
- [ ] Lossless compression (PNG format)
- [ ] Copyright permissions obtained if using third-party data (N/A - all original)
- [ ] Supplementary materials prepared for interactive versions (HTML files available)

### Accessibility Considerations

- [ ] Color palettes distinguish categories without relying solely on color
- [ ] Line styles varied (solid, dashed, dotted) in addition to colors
- [ ] Text contrast ratio meets WCAG 2.1 Level AA (≥4.5:1)
- [ ] All text content readable at normal viewing distance
- [ ] Alternative text descriptions prepared for figures (for screen readers)

---

## Data Sources & Reproducibility

### Sample Dataset
- **File:** `data/sample/organizational_data.json`
- **Organization:** Rajamangala University of Technology Krungthep
- **Assessment Period:** Academic Year 2024-2025
- **Units Assessed:** 24 organizational units
- **Historical Data:** 5 years (2020-2025)

### Code Availability
All figures can be reproduced using the provided Python scripts:

1. **Basic Visualizations (Fig1-7):**
   ```bash
   python examples/complete_demo.py
   ```

2. **Advanced Visualizations (Fig8-14):**
   ```bash
   python examples/advanced_visualizations_demo.py
   ```

3. **Notebook-based Generation:**
   - Notebook 1: `notebooks/01_Framework_Complete_Demo.ipynb`
   - Notebook 2: `notebooks/02_Advanced_Visualizations.ipynb`

### GitHub Repository
- **URL:** https://github.com/ChatchaiTritham/EdcellenceEdPEx
- **License:** MIT License (open source)
- **DOI:** (To be assigned upon GitHub release)

---

## Supplementary Materials

### Interactive Versions Available

The following figures have interactive HTML versions available in the `outputs/` directory:

- Figure 1 Alternative: `07_interactive_scorecard.html` (interactive radar + scorecard)
- Figure 10 Alternative: Network diagram with hoverable tooltips
- Additional 3D Visualizations: `14_3d_scatter_adli.html` (ADLI space exploration)

These interactive versions can be included as supplementary materials in the IEEE ACCESS submission, providing readers with enhanced exploration capabilities.

---

## Contact Information

**Corresponding Author:**
Rungtiva Saosing
Faculty of Science and Technology
Rajamangala University of Technology Krungthep
Bangkok, Thailand
Email: rungtiva.s@rmutk.ac.th

**Technical Inquiries:**
GitHub Issues: https://github.com/ChatchaiTritham/EdcellenceEdPEx/issues

---

## Citation

When using these figures, please cite as:

```
Saosing, R., Tritham, C., Tritham, C., & Ngammongkolwong, S. (2026).
From Excellence Guidelines to Computable Performance Systems: A Novel
Framework for Educational Performance Excellence Assessment.
IEEE ACCESS. (In Press)
```

---

**Document Version:** 1.0
**Last Updated:** February 14, 2026
**Generated by:** EdcellenceEdPEx Framework v1.0
