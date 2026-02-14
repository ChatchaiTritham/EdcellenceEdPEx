"""
Advanced Visualizations Demonstration
======================================

Comprehensive demonstration of advanced statistical and interactive
visualizations for organizational excellence assessment.

Authors:
    Rungtiva Saosing, Chatchai Tritham, Chattabhorn Tritham, Sudasawan Ngammongkolwong
    Faculty of Science and Technology, Rajamangala University of Technology Krungthep

Generates:
    - Statistical distribution plots
    - Correlation matrices
    - Network diagrams
    - Interactive 3D charts
    - Temporal decomposition
    - Hierarchical sunburst charts
    - Flow analysis (Sankey)
    - Parallel coordinates

Usage:
    python examples/advanced_visualizations_demo.py
"""

import sys
import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from visualizations.advanced_visualizer import (
    AdvancedVisualizer,
    create_sample_hierarchical_data
)


def load_sample_data():
    """Load sample organizational data."""
    data_path = os.path.join(
        os.path.dirname(__file__), '..', 'data', 'sample', 'organizational_data.json'
    )
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def demo_distribution_analysis(viz, data):
    """Demonstrate distribution comparison visualizations."""
    print("\n" + "="*70)
    print("DEMO 1: Distribution Analysis (Box + Violin Plots)")
    print("="*70)

    # Prepare score distributions for each category
    score_distributions = {}

    for cat_id_str, cat_data in data['categories'].items():
        cat_name = cat_data['name']
        if 'items' in cat_data:
            scores = [item['score'] for item in cat_data['items'].values()]
            # Add some variation for realistic distribution
            varied_scores = []
            for score in scores:
                variation = np.random.normal(score, 3, 10)  # 10 samples per item
                varied_scores.extend(variation)
            score_distributions[cat_name] = varied_scores

    fig = viz.plot_distribution_comparison(
        score_distributions,
        title="Category Score Distributions",
        save_path='outputs/08_distribution_comparison.png'
    )
    plt.close(fig)

    print("[OK] Generated: outputs/08_distribution_comparison.png")
    print(f"  - Box plots showing quartiles and outliers")
    print(f"  - Violin plots showing density distributions")
    print(f"  - {len(score_distributions)} categories analyzed")


def demo_correlation_analysis(viz, data):
    """Demonstrate correlation matrix visualization."""
    print("\n" + "="*70)
    print("DEMO 2: Correlation Matrix Analysis")
    print("="*70)

    # Create correlation data from historical trends
    if 'historical_trends' in data:
        trends_df = pd.DataFrame(data['historical_trends']).T
        trends_df.columns = [f"Cat{i}" for i in range(1, 8)]

        fig = viz.plot_correlation_matrix(
            trends_df,
            title="Category Score Correlation Matrix (2020-2025)",
            save_path='outputs/09_correlation_matrix.png'
        )
        plt.close(fig)

        print("[OK] Generated: outputs/09_correlation_matrix.png")
        print(f"  - Pearson correlation coefficients")
        print(f"  - Hierarchical clustering of categories")
        print(f"  - 5-year temporal data analyzed")


def demo_network_visualization(viz, data):
    """Demonstrate category dependency network."""
    print("\n" + "="*70)
    print("DEMO 3: Category Dependency Network")
    print("="*70)

    # Extract category scores
    category_scores = {}
    for cat_id_str, cat_data in data['categories'].items():
        cat_id = int(cat_id_str)
        if 'items' in cat_data:
            scores = [item['score'] for item in cat_data['items'].values()]
            category_scores[cat_id] = np.mean(scores)

    # Define dependencies (from BEB-EdPEx framework)
    dependencies = [
        (1, 2),  # Leadership -> Strategy
        (2, 5),  # Strategy -> Workforce
        (2, 6),  # Strategy -> Operations
        (5, 4),  # Workforce -> Measurement
        (6, 4),  # Operations -> Measurement
        (4, 7),  # Measurement -> Results
        (3, 7),  # Customers -> Results
    ]

    category_names = {
        1: 'Leadership', 2: 'Strategy', 3: 'Customers', 4: 'Measurement',
        5: 'Workforce', 6: 'Operations', 7: 'Results'
    }

    fig = viz.plot_category_network(
        category_scores,
        dependencies,
        category_names,
        title="BEB-EdPEx Category Dependency Network",
        save_path='outputs/10_network_diagram.png'
    )
    plt.close(fig)

    print("[OK] Generated: outputs/10_network_diagram.png")
    print(f"  - {len(category_scores)} categories as nodes")
    print(f"  - {len(dependencies)} dependency edges")
    print(f"  - Node size proportional to score")
    print(f"  - Network analysis: Spring layout algorithm")


def demo_sunburst_chart(viz, data):
    """Demonstrate hierarchical sunburst visualization."""
    print("\n" + "="*70)
    print("DEMO 4: Hierarchical Sunburst Chart (Interactive)")
    print("="*70)

    hierarchical_data = create_sample_hierarchical_data()

    fig = viz.create_sunburst_chart(
        hierarchical_data,
        title="Organizational Excellence Hierarchy - Interactive Sunburst",
        save_path='outputs/11_sunburst_hierarchy.html'
    )

    print("[OK] Generated: outputs/11_sunburst_hierarchy.html")
    print(f"  - 3-level hierarchy (Organization -> Categories -> Items)")
    print(f"  - Interactive drill-down capability")
    print(f"  - Color-coded by score")
    print(f"  - Open in browser for interactive exploration")


def demo_sankey_diagram(viz, data):
    """Demonstrate flow analysis with Sankey diagram."""
    print("\n" + "="*70)
    print("DEMO 5: Performance Flow Analysis (Sankey Diagram)")
    print("="*70)

    # Create flow data showing score contributions
    flow_data = {
        'labels': [
            'Leadership (75)', 'Strategy (68)', 'Customers (82)',
            'Measurement (70)', 'Workforce (74)', 'Operations (69)',
            'Results (87)', 'Overall Excellence'
        ],
        'source': [0, 1, 2, 3, 4, 5, 6],  # Category indices
        'target': [7, 7, 7, 7, 7, 7, 7],  # All flow to overall
        'value': [75, 68, 82, 70, 74, 69, 87]  # Contribution values
    }

    fig = viz.create_sankey_diagram(
        flow_data,
        title="Category Contributions to Overall Excellence",
        save_path='outputs/12_sankey_flow.html'
    )

    print("[OK] Generated: outputs/12_sankey_flow.html")
    print(f"  - 7 categories flowing to overall score")
    print(f"  - Flow width proportional to contribution")
    print(f"  - Interactive hover for details")


def demo_temporal_decomposition(viz, data):
    """Demonstrate time series decomposition."""
    print("\n" + "="*70)
    print("DEMO 6: Temporal Decomposition Analysis")
    print("="*70)

    if 'historical_trends' in data:
        # Extract trends for each category
        for cat_id in range(1, 4):  # Demo with first 3 categories
            trend_data = []
            for period, scores in data['historical_trends'].items():
                trend_data.append({
                    'period': period,
                    'score': scores[str(cat_id)]
                })

            df = pd.DataFrame(trend_data)
            cat_name = data['categories'][str(cat_id)]['name']

            fig = viz.plot_temporal_decomposition(
                df,
                cat_name,
                save_path=f'outputs/13_decomposition_cat{cat_id}.png'
            )
            plt.close(fig)

        print("[OK] Generated: outputs/13_decomposition_cat[1-3].png")
        print(f"  - Original series + Trend + Seasonal + Residuals")
        print(f"  - Moving average trend estimation")
        print(f"  - 3 categories analyzed (5-year data)")


def demo_3d_scatter(viz, data):
    """Demonstrate interactive 3D scatter plot."""
    print("\n" + "="*70)
    print("DEMO 7: Interactive 3D Performance Analysis")
    print("="*70)

    # Create 3D data: ADLI dimensions for each category
    scatter_data = []

    for cat_id_str, cat_data in data['categories'].items():
        if int(cat_id_str) <= 6:  # Process categories only
            cat_name = cat_data['name']
            if 'items' in cat_data:
                for item_id, item_data in cat_data['items'].items():
                    if 'indicators' in item_data:
                        ind = item_data['indicators']
                        scatter_data.append({
                            'Category': cat_name,
                            'Approach': ind.get('P_A', 0) * 100,
                            'Deployment': ind.get('P_D', 0) * 100,
                            'Learning': ind.get('P_L', 0) * 100,
                            'Score': item_data['score']
                        })

    df = pd.DataFrame(scatter_data)

    fig = viz.create_3d_scatter_interactive(
        df,
        x_col='Approach',
        y_col='Deployment',
        z_col='Learning',
        color_col='Score',
        title="3D ADLI Dimensional Analysis (Interactive)",
        save_path='outputs/14_3d_scatter_adli.html'
    )

    print("[OK] Generated: outputs/14_3d_scatter_adli.html")
    print(f"  - {len(df)} data points (category items)")
    print(f"  - 3D coordinates: Approach, Deployment, Learning")
    print(f"  - Color-coded by overall score")
    print(f"  - Fully interactive (rotate, zoom, hover)")


def demo_statistical_summary(viz, data):
    """Demonstrate comprehensive statistical summary."""
    print("\n" + "="*70)
    print("DEMO 8: Statistical Summary Panel")
    print("="*70)

    # Generate score distributions with realistic variation
    score_distributions = {}

    for cat_id_str, cat_data in data['categories'].items():
        cat_name = cat_data['name']
        if 'items' in cat_data:
            scores = [item['score'] for item in cat_data['items'].values()]
            # Add variation for statistical analysis
            varied_scores = []
            for score in scores:
                variation = np.random.normal(score, 4, 15)
                varied_scores.extend(np.clip(variation, 0, 100))
            score_distributions[cat_name] = varied_scores

    fig = viz.plot_statistical_summary(
        score_distributions,
        title="Comprehensive Statistical Summary by Category",
        save_path='outputs/15_statistical_summary.png'
    )
    plt.close(fig)

    print("[OK] Generated: outputs/15_statistical_summary.png")
    print(f"  - Mean scores with 95% confidence intervals")
    print(f"  - Coefficient of variation analysis")
    print(f"  - Min-Max ranges")
    print(f"  - Quartile distributions (Q1, Median, Q3)")


def demo_parallel_coordinates(viz, data):
    """Demonstrate parallel coordinates plot."""
    print("\n" + "="*70)
    print("DEMO 9: Parallel Coordinates Analysis (Interactive)")
    print("="*70)

    # Create multivariate data
    parallel_data = []

    for cat_id_str, cat_data in data['categories'].items():
        cat_name = cat_data['name']
        if 'items' in cat_data:
            avg_score = np.mean([item['score'] for item in cat_data['items'].values()])
            parallel_data.append({
                'Category': cat_name,
                'Leadership': data['categories']['1']['items']['1']['score'],
                'Strategy': data['categories']['2']['items']['1']['score'],
                'Customers': data['categories']['3']['items']['1']['score'],
                'Measurement': data['categories']['4']['items']['1']['score'],
                'Workforce': data['categories']['5']['items']['1']['score'],
                'Operations': data['categories']['6']['items']['1']['score'],
                'Results': data['categories']['7']['items']['1']['score'],
                'Overall': avg_score
            })

    df = pd.DataFrame(parallel_data)
    dimensions = ['Leadership', 'Strategy', 'Customers', 'Measurement',
                  'Workforce', 'Operations', 'Results']

    fig = viz.create_parallel_coordinates(
        df,
        dimensions,
        color_col='Overall',
        title="Multi-dimensional Category Analysis - Parallel Coordinates",
        save_path='outputs/16_parallel_coordinates.html'
    )

    print("[OK] Generated: outputs/16_parallel_coordinates.html")
    print(f"  - 7 dimensions visualized simultaneously")
    print(f"  - Interactive filtering and selection")
    print(f"  - Color-coded by overall performance")
    print(f"  - Pattern analysis for correlations")


def print_summary():
    """Print summary of all generated visualizations."""
    print("\n" + "="*70)
    print("VISUALIZATION GENERATION COMPLETE")
    print("="*70)

    visualizations = [
        ("08_distribution_comparison.png", "Box + Violin plots", "Statistical distributions"),
        ("09_correlation_matrix.png", "Correlation heatmap", "Category relationships"),
        ("10_network_diagram.png", "Dependency network", "Category connections"),
        ("11_sunburst_hierarchy.html", "Sunburst chart", "Hierarchical structure"),
        ("12_sankey_flow.html", "Sankey diagram", "Flow analysis"),
        ("13_decomposition_cat1.png", "Time series (Cat 1)", "Temporal patterns"),
        ("13_decomposition_cat2.png", "Time series (Cat 2)", "Temporal patterns"),
        ("13_decomposition_cat3.png", "Time series (Cat 3)", "Temporal patterns"),
        ("14_3d_scatter_adli.html", "3D scatter (ADLI)", "Dimensional analysis"),
        ("15_statistical_summary.png", "Statistical panel", "Comprehensive stats"),
        ("16_parallel_coordinates.html", "Parallel coords", "Multivariate analysis"),
    ]

    print("\nGenerated Files:")
    print("-" * 70)
    for filename, viz_type, description in visualizations:
        file_type = "PNG (300 DPI)" if filename.endswith('.png') else "HTML (Interactive)"
        print(f"  {filename:35s} {viz_type:20s} [{file_type}]")

    print("\n" + "="*70)
    print("Total: 11 high-quality visualizations")
    print("\nVisualization Types:")
    print("  - Static plots (PNG): 6 files")
    print("  - Interactive charts (HTML): 5 files")
    print("\nAll files saved to: outputs/")
    print("="*70)


def main():
    """Run all advanced visualization demonstrations."""
    print("\n" + "="*80)
    print(" "*20 + "ADVANCED VISUALIZATIONS DEMO")
    print(" "*15 + "Publication-Quality Scientific Charts")
    print("="*80)
    print("\nAuthors: Saosing et al. (2026)")
    print("Framework: BEB-EdPEx Computational Assessment")
    print("="*80)

    # Create outputs directory
    os.makedirs('outputs', exist_ok=True)

    # Load data
    print("\nLoading sample data...")
    data = load_sample_data()
    print(f"[OK] Loaded data for {data['organization']['name']}")

    # Initialize visualizer
    viz = AdvancedVisualizer()
    print("[OK] Advanced visualizer initialized")

    # Run demonstrations
    demo_distribution_analysis(viz, data)
    demo_correlation_analysis(viz, data)
    demo_network_visualization(viz, data)
    demo_sunburst_chart(viz, data)
    demo_sankey_diagram(viz, data)
    demo_temporal_decomposition(viz, data)
    demo_3d_scatter(viz, data)
    demo_statistical_summary(viz, data)
    demo_parallel_coordinates(viz, data)

    # Print summary
    print_summary()

    print("\n" + "="*80)
    print("NEXT STEPS")
    print("="*80)
    print("\n1. View static plots:")
    print("   - Open PNG files in outputs/ directory")
    print("   - Publication-ready at 300 DPI")
    print("\n2. Explore interactive charts:")
    print("   - Open HTML files in web browser")
    print("   - Full interactivity (zoom, pan, hover, filter)")
    print("\n3. Integrate into publication:")
    print("   - Static plots for IEEE ACCESS paper")
    print("   - Interactive charts for supplementary materials")
    print("\n" + "="*80)


if __name__ == "__main__":
    main()
