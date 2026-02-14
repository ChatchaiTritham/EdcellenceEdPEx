"""
Complete Demonstration: ADLI-LeTCI Framework
=============================================

Comprehensive example demonstrating all features of the organizational
excellence assessment framework with 2D and 3D visualizations.

Authors:
    Rungtiva Saosing, Chatchai Tritham, Chattabhorn Tritham, Sudasawan Ngammongkolwong
    Faculty of Science and Technology, Rajamangala University of Technology Krungthep

Usage:
    python examples/complete_demo.py
"""

import sys
import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from algorithms.adli_scoring import ADLIScorer, compute_adli_score
from algorithms.letci_scoring import LeTCIScorer, compute_letci_score
from algorithms.organizational_scoring import OrganizationalScorer, create_sample_organization_data
from visualizations.scoring_visualizer import ScoringVisualizer


def load_sample_data():
    """Load sample organizational data from JSON file."""
    data_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'data',
        'sample',
        'organizational_data.json'
    )

    if os.path.exists(data_path):
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        print("Warning: Sample data file not found. Using generated data.")
        return create_sample_organization_data()


def demo_adli_scoring():
    """Demonstrate ADLI scoring for process assessment."""
    print("\n" + "="*70)
    print("DEMO 1: ADLI Scoring (Process Assessment)")
    print("="*70)

    # Example from research paper: Category 2 (Strategy), Item 3
    indicators = {
        'P_A': 0.75,  # Approach: well-specified and documented
        'P_D': 0.45,  # Deployment: inconsistent across units
        'P_L': 0.60,  # Learning: moderate effectiveness
        'P_I': 0.55   # Integration: developmental stage
    }

    scorer = ADLIScorer()
    score = scorer.compute_score(indicators)
    breakdown = scorer.get_diagnostic_breakdown(indicators)

    print(f"\nCategory: Strategy (2)")
    print(f"Item: Strategic Planning Implementation (3)")
    print(f"\nNormalized Indicators (0-1 scale):")
    for dim, value in indicators.items():
        print(f"  {dim}: {value:.2f}")

    print(f"\nADLI Score: {score}/100")
    print(f"\nDimensional Breakdown:")
    for dim, contrib in breakdown.items():
        print(f"  {dim:15s}: {contrib:5.1f}")

    print(f"\nInterpretation:")
    print(f"  Score of {score} indicates early systematic maturity.")
    print(f"  Approach strength (P_A=0.75) is counterbalanced by")
    print(f"  deployment inconsistency (P_D=0.45).")
    print(f"  Recommendation: Focus on deployment support and")
    print(f"  organizational change facilitation.")

    return breakdown


def demo_letci_scoring():
    """Demonstrate LeTCI scoring for results assessment."""
    print("\n" + "="*70)
    print("DEMO 2: LeTCI Scoring (Results Assessment)")
    print("="*70)

    # High-performing results item
    indicators = {
        'R_Lv': 0.85,  # Outcome level: 85th percentile
        'R_Tr': 0.90,  # Trend: strong positive improvement
        'R_Cp': 0.75,  # Comparison: above national benchmark
        'R_I': 0.70    # Integration: good cross-category alignment
    }

    scorer = LeTCIScorer()
    score = scorer.compute_score(indicators)
    breakdown = scorer.get_diagnostic_breakdown(indicators)

    # Demonstrate trend normalization
    historical_values = [70, 75, 80, 85, 90]
    trend_score = scorer.normalize_trend(historical_values)

    print(f"\nCategory: Results (7)")
    print(f"Item: Student Learning Outcomes (1)")
    print(f"\nNormalized Indicators (0-1 scale):")
    for dim, value in indicators.items():
        print(f"  {dim}: {value:.2f}")

    print(f"\nLeTCI Score: {score}/100")
    print(f"\nDimensional Breakdown:")
    for dim, contrib in breakdown.items():
        print(f"  {dim:15s}: {contrib:5.1f}")

    print(f"\nTrend Analysis:")
    print(f"  Historical values: {historical_values}")
    print(f"  Trend score: {trend_score:.2f} (0.6+ = Improving)")

    return breakdown


def demo_organizational_scoring():
    """Demonstrate organizational-level scoring and analytics."""
    print("\n" + "="*70)
    print("DEMO 3: Organizational-Level Scoring")
    print("="*70)

    # Load sample data
    data = load_sample_data()

    # Initialize scorer
    scorer = OrganizationalScorer()

    # Compute category scores from sample data
    category_scores = {}
    for cat_id_str, cat_data in data['categories'].items():
        cat_id = int(cat_id_str)
        if 'items' in cat_data:
            item_scores = [item_data['score'] for item_data in cat_data['items'].values()]
            category_scores[cat_id] = np.mean(item_scores)

    # Generate comprehensive scorecard
    scorecard = scorer.generate_scorecard(category_scores, include_ihi=True)

    print(f"\nOrganization: {data['organization']['name']}")
    print(f"Period: {data['organization']['assessment_period']}")
    print(f"\n{'='*70}")
    print(f"Overall Organizational Score: {scorecard['organizational_score']:.1f}/100")
    print(f"Maturity Level: {scorecard['maturity_level']}")
    print(f"Confidence Level: {scorecard['confidence']:.3f}")
    print(f"\n{'='*70}")
    print(f"Integration Health Index (IHI): {scorecard['integration_health_index']:.3f}")
    print(f"Interpretation: {scorecard['ihi_interpretation']}")

    print(f"\n{'='*70}")
    print(f"Category Scores:")
    print(f"{'='*70}")
    for cat_id in sorted(category_scores.keys()):
        cat_name = scorecard['category_names'][cat_id]
        cat_score = category_scores[cat_id]
        print(f"  {cat_id}. {cat_name:15s}: {cat_score:5.1f}/100")

    return scorecard, data


def demo_gap_analysis(scorer, data):
    """Demonstrate gap analysis and prioritization."""
    print("\n" + "="*70)
    print("DEMO 4: Gap Analysis & Improvement Prioritization")
    print("="*70)

    # Extract current and target scores
    current_scores = {}
    target_scores = {}

    for cat_id_str, cat_data in data['categories'].items():
        cat_id = int(cat_id_str)
        current_scores[cat_id] = {}
        target_scores[cat_id] = {}

        if 'items' in cat_data:
            for item_id_str, item_data in cat_data['items'].items():
                item_id = int(item_id_str)
                current_scores[cat_id][item_id] = item_data['score']
                target_scores[cat_id][item_id] = data['targets_2025'][cat_id_str]

    # Perform gap analysis
    gap_df = scorer.compute_gap_analysis(current_scores, target_scores)

    # Display top 10 priorities
    print(f"\nTop 10 Improvement Priorities:")
    print(f"{'='*70}")
    print(f"{'Cat':<4} {'Item':<5} {'Current':<8} {'Target':<7} {'Gap':<6} {'Priority':<10} {'Status':<10}")
    print(f"{'-'*70}")

    for _, row in gap_df.head(10).iterrows():
        print(f"{row['category']:<4} {row['item']:<5} "
              f"{row['current_score']:<8.1f} {row['target_score']:<7.1f} "
              f"{row['gap']:<6.1f} {row['priority']:<10.2f} {row['status']:<10}")

    print(f"\nGap Analysis Summary:")
    print(f"  Total items analyzed: {len(gap_df)}")
    print(f"  Critical gaps (>20 points): {len(gap_df[gap_df['gap'] > 20])}")
    print(f"  Monitor items (10-20 points): {len(gap_df[(gap_df['gap'] > 10) & (gap_df['gap'] <= 20)])}")
    print(f"  On track (<10 points): {len(gap_df[gap_df['gap'] <= 10])}")

    return gap_df


def demo_visualizations(scorecard, data, adli_breakdown, letci_breakdown, gap_df):
    """Generate all visualizations."""
    print("\n" + "="*70)
    print("DEMO 5: Generating Visualizations (2D & 3D)")
    print("="*70)

    viz = ScoringVisualizer()

    # Extract category scores
    category_scores = scorecard['category_scores']
    target_scores = {int(k): v for k, v in data.get('targets_2025', {}).items()}

    print("\nGenerating visualizations...")

    # 1. Radar chart
    print("  [1/7] Creating radar chart for category scores...")
    fig1 = viz.plot_category_scores_radar(
        category_scores,
        target_scores,
        save_path='outputs/01_radar_chart.png'
    )
    plt.close(fig1)

    # 2. ADLI breakdown
    print("  [2/7] Creating ADLI dimensional breakdown...")
    fig2 = viz.plot_adli_breakdown(
        adli_breakdown,
        save_path='outputs/02_adli_breakdown.png'
    )
    plt.close(fig2)

    # 3. LeTCI breakdown
    print("  [3/7] Creating LeTCI dimensional breakdown...")
    fig3 = viz.plot_letci_breakdown(
        letci_breakdown,
        save_path='outputs/03_letci_breakdown.png'
    )
    plt.close(fig3)

    # 4. Gap analysis heatmap
    print("  [4/7] Creating gap analysis heatmap...")
    fig4 = viz.plot_gap_analysis_heatmap(
        gap_df,
        save_path='outputs/04_gap_heatmap.png'
    )
    plt.close(fig4)

    # 5. Priority matrix
    print("  [5/7] Creating improvement priority matrix...")
    fig5 = viz.plot_priority_matrix(
        gap_df,
        save_path='outputs/05_priority_matrix.png'
    )
    plt.close(fig5)

    # 6. 3D surface plot (if historical data available)
    if 'historical_trends' in data:
        print("  [6/7] Creating 3D category performance evolution...")
        historical = {k: {int(c): v for c, v in cats.items()}
                     for k, cats in data['historical_trends'].items()}
        fig6 = viz.plot_3d_category_surface(
            historical,
            save_path='outputs/06_3d_evolution.png'
        )
        plt.close(fig6)

    # 7. Interactive scorecard (Plotly)
    print("  [7/7] Creating interactive HTML scorecard...")
    fig7 = viz.create_interactive_scorecard(
        scorecard,
        save_path='outputs/07_interactive_scorecard.html'
    )

    print(f"\n[OK] All visualizations saved to 'outputs/' directory")
    print(f"\nGenerated files:")
    print(f"  - 01_radar_chart.png           : Category scores radar chart")
    print(f"  - 02_adli_breakdown.png        : ADLI dimensional breakdown")
    print(f"  - 03_letci_breakdown.png       : LeTCI dimensional breakdown")
    print(f"  - 04_gap_heatmap.png           : Gap analysis heatmap")
    print(f"  - 05_priority_matrix.png       : Priority matrix (2D)")
    print(f"  - 06_3d_evolution.png          : Performance evolution (3D)")
    print(f"  - 07_interactive_scorecard.html: Interactive dashboard")


def print_statistical_validation():
    """Display statistical validation results from research paper."""
    print("\n" + "="*70)
    print("STATISTICAL VALIDATION (Empirical Results)")
    print("="*70)

    print(f"\nDeployment: 24 organizational units")
    print(f"Period: Academic year 2024-2025")
    print(f"\nQuantitative Impact Assessment:")
    print(f"{'='*70}")

    results = [
        ("Assessment Cycle Duration", "6.5 weeks", "2.0 weeks", "-69%", "p<0.001", "d=3.2"),
        ("Document Artifacts", "450 docs", "80 docs", "-82%", "p<0.001", "d=3.8"),
        ("Measurement Consistency (α)", "0.62", "0.88", "+42%", "p<0.001", "d=2.1"),
        ("Review Duration", "4.5 hrs", "2.5 hrs", "-44%", "p<0.001", "d=2.4"),
    ]

    print(f"{'Metric':<28} {'Baseline':<12} {'Post-Impl':<12} {'Change':<8} {'p-value':<10} {'Effect':<6}")
    print(f"{'-'*70}")
    for metric, baseline, post, change, p, d in results:
        print(f"{metric:<28} {baseline:<12} {post:<12} {change:<8} {p:<10} {d:<6}")

    print(f"\nTechnical Performance:")
    print(f"  Category-level aggregation: 47±12ms (mean±SD)")
    print(f"  Institution-level synthesis: 183±31ms")
    print(f"  Query success rate: 99.7%")

    print(f"\nAlgorithm Validation:")
    print(f"  Correlation (automated vs expert): r=0.91, p<0.001")
    print(f"  Mean absolute error: 3.2 points (0-100 scale)")


def main():
    """Run complete demonstration."""
    print("\n" + "="*80)
    print(" "*20 + "EDCELLENCE-EDPEX FRAMEWORK")
    print(" "*15 + "Complete Demonstration & Validation")
    print("="*80)
    print("\nAuthors:")
    print("  Rungtiva Saosing, Chatchai Tritham, Chattabhorn Tritham,")
    print("  Sudasawan Ngammongkolwong")
    print("\nAffiliation:")
    print("  Faculty of Science and Technology")
    print("  Rajamangala University of Technology Krungthep")
    print("\nReference:")
    print("  Saosing et al. (2026). From Excellence Guidelines to Computable")
    print("  Performance Systems. IEEE ACCESS.")
    print("="*80)

    # Create outputs directory
    os.makedirs('outputs', exist_ok=True)

    # Run demonstrations
    adli_breakdown = demo_adli_scoring()
    letci_breakdown = demo_letci_scoring()
    scorecard, data = demo_organizational_scoring()

    # Initialize scorer for gap analysis
    scorer = OrganizationalScorer()
    gap_df = demo_gap_analysis(scorer, data)

    # Generate visualizations
    demo_visualizations(scorecard, data, adli_breakdown, letci_breakdown, gap_df)

    # Display statistical validation
    print_statistical_validation()

    print("\n" + "="*80)
    print("DEMONSTRATION COMPLETE")
    print("="*80)
    print("\nNext steps:")
    print("  1. Review generated visualizations in outputs/ directory")
    print("  2. Open 07_interactive_scorecard.html in web browser")
    print("  3. Explore Jupyter notebooks for interactive analysis")
    print("  4. Customize parameters for your organization")
    print("\n" + "="*80)


if __name__ == "__main__":
    main()
