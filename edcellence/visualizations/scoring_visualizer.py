"""
Scoring Visualization Module
=============================

Comprehensive visualization suite for ADLI-LeTCI scoring framework with
2D and 3D charts for organizational excellence assessment.

Authors:
    Rungtiva Saosing, Chatchai Tritham, Chattabhorn Tritham, Sudasawan Ngammongkolwong
    Faculty of Science and Technology, Rajamangala University of Technology Krungthep

Reference:
    Saosing et al. (2026). From Excellence Guidelines to Computable Performance Systems.
    IEEE ACCESS.
"""

from typing import Dict, List, Optional, Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Configure visualization defaults
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10


class ScoringVisualizer:
    """
    Comprehensive visualization engine for organizational excellence scoring.

    Provides 2D and 3D visualizations for ADLI-LeTCI scores, gap analysis,
    trends, and organizational scorecards.
    """

    # Color schemes
    CATEGORY_COLORS = {
        1: '#1f77b4',  # Leadership - Blue
        2: '#ff7f0e',  # Strategy - Orange
        3: '#2ca02c',  # Customers - Green
        4: '#d62728',  # Measurement - Red
        5: '#9467bd',  # Workforce - Purple
        6: '#8c564b',  # Operations - Brown
        7: '#e377c2'   # Results - Pink
    }

    CATEGORY_NAMES = {
        1: 'Leadership',
        2: 'Strategy',
        3: 'Customers',
        4: 'Measurement',
        5: 'Workforce',
        6: 'Operations',
        7: 'Results'
    }

    def __init__(self, style: str = 'default'):
        """
        Initialize visualizer.

        Args:
            style: Matplotlib style ('default', 'seaborn', 'ggplot', 'bmh')
        """
        if style != 'default':
            plt.style.use(style)

    def plot_category_scores_radar(
        self,
        category_scores: Dict[int, float],
        target_scores: Optional[Dict[int, float]] = None,
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create radar chart for category scores.

        Args:
            category_scores: Dict of {category: score}
            target_scores: Optional target scores for comparison
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        categories = list(category_scores.keys())
        values = list(category_scores.values())
        labels = [self.CATEGORY_NAMES[c] for c in categories]

        # Number of variables
        N = len(categories)

        # Compute angle for each axis
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        values += values[:1]  # Complete the circle
        angles += angles[:1]

        # Initialize plot
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

        # Plot actual scores
        ax.plot(angles, values, 'o-', linewidth=2, label='Current', color='#2ca02c')
        ax.fill(angles, values, alpha=0.25, color='#2ca02c')

        # Plot target scores if provided
        if target_scores:
            target_vals = [target_scores.get(c, 100) for c in categories]
            target_vals += target_vals[:1]
            ax.plot(angles, target_vals, 'o--', linewidth=2, label='Target', color='#ff7f0e')
            ax.fill(angles, target_vals, alpha=0.10, color='#ff7f0e')

        # Configure plot
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, size=11)
        ax.set_ylim(0, 100)
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.set_yticklabels(['20', '40', '60', '80', '100'])
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

        plt.title('Organizational Excellence - Category Scores', size=14, fontweight='bold', pad=20)

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_adli_breakdown(
        self,
        adli_scores: Dict[str, float],
        title: str = "ADLI Dimensional Breakdown",
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create bar chart for ADLI dimensional breakdown.

        Args:
            adli_scores: Dict with keys 'Approach', 'Deployment', 'Learning', 'Integration'
            title: Plot title
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        dimensions = ['Approach', 'Deployment', 'Learning', 'Integration']
        values = [adli_scores.get(d, 0) for d in dimensions]
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

        fig, ax = plt.subplots(figsize=(10, 6))

        bars = ax.bar(dimensions, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}',
                   ha='center', va='bottom', fontsize=12, fontweight='bold')

        ax.set_ylabel('Score', fontsize=12, fontweight='bold')
        ax.set_ylim(0, 100)
        ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
        ax.grid(axis='y', alpha=0.3, linestyle='--')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_letci_breakdown(
        self,
        letci_scores: Dict[str, float],
        title: str = "LeTCI Dimensional Breakdown",
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create bar chart for LeTCI dimensional breakdown.

        Args:
            letci_scores: Dict with keys 'Levels', 'Trends', 'Comparisons', 'Integration'
            title: Plot title
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        dimensions = ['Levels', 'Trends', 'Comparisons', 'Integration']
        values = [letci_scores.get(d, 0) for d in dimensions]
        colors = ['#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

        fig, ax = plt.subplots(figsize=(10, 6))

        bars = ax.bar(dimensions, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}',
                   ha='center', va='bottom', fontsize=12, fontweight='bold')

        ax.set_ylabel('Score', fontsize=12, fontweight='bold')
        ax.set_ylim(0, 100)
        ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
        ax.grid(axis='y', alpha=0.3, linestyle='--')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_gap_analysis_heatmap(
        self,
        gap_df: pd.DataFrame,
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create heatmap for gap analysis across categories and items.

        Args:
            gap_df: DataFrame with columns ['category', 'item', 'gap']
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        # Pivot data for heatmap
        heatmap_data = gap_df.pivot(index='item', columns='category', values='gap')

        fig, ax = plt.subplots(figsize=(12, 8))

        sns.heatmap(
            heatmap_data,
            annot=True,
            fmt='.1f',
            cmap='RdYlGn_r',
            center=10,
            vmin=0,
            vmax=30,
            cbar_kws={'label': 'Gap (Target - Current)'},
            linewidths=0.5,
            linecolor='gray',
            ax=ax
        )

        ax.set_title('Gap Analysis Heatmap - Categories vs Items', fontsize=14, fontweight='bold', pad=15)
        ax.set_xlabel('Category', fontsize=12, fontweight='bold')
        ax.set_ylabel('Item', fontsize=12, fontweight='bold')

        # Set category names as x-labels
        cat_labels = [self.CATEGORY_NAMES.get(int(c), f'Cat {c}') for c in heatmap_data.columns]
        ax.set_xticklabels(cat_labels, rotation=45, ha='right')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_3d_category_surface(
        self,
        historical_data: Dict[str, Dict[int, float]],
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create 3D surface plot for category scores over time.

        Args:
            historical_data: Dict of {period: {category: score}}
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        # Prepare data
        periods = list(historical_data.keys())
        categories = list(range(1, 8))

        X, Y = np.meshgrid(categories, range(len(periods)))
        Z = np.array([[historical_data[p].get(c, 0) for c in categories] for p in periods])

        # Create 3D plot
        fig = plt.figure(figsize=(14, 10))
        ax = fig.add_subplot(111, projection='3d')

        surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, edgecolor='none')

        ax.set_xlabel('Category', fontsize=11, fontweight='bold', labelpad=10)
        ax.set_ylabel('Period', fontsize=11, fontweight='bold', labelpad=10)
        ax.set_zlabel('Score', fontsize=11, fontweight='bold', labelpad=10)
        ax.set_title('Category Performance Evolution (3D)', fontsize=14, fontweight='bold', pad=20)

        # Set category ticks
        ax.set_xticks(categories)
        ax.set_xticklabels([self.CATEGORY_NAMES[c][:3] for c in categories], rotation=15)

        # Add colorbar
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='Score')

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_priority_matrix(
        self,
        gap_df: pd.DataFrame,
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create priority matrix (Impact vs Gap) scatter plot.

        Args:
            gap_df: DataFrame with columns ['gap', 'priority', 'category', 'item']
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=(12, 8))

        # Create scatter plot
        for category in gap_df['category'].unique():
            cat_data = gap_df[gap_df['category'] == category]
            ax.scatter(
                cat_data['gap'],
                cat_data['priority'],
                s=150,
                alpha=0.7,
                color=self.CATEGORY_COLORS.get(category, '#gray'),
                label=self.CATEGORY_NAMES.get(category, f'Cat {category}'),
                edgecolors='black',
                linewidth=1.5
            )

        # Add quadrant lines
        gap_median = gap_df['gap'].median()
        priority_median = gap_df['priority'].median()

        ax.axvline(gap_median, color='gray', linestyle='--', alpha=0.5, linewidth=1.5)
        ax.axhline(priority_median, color='gray', linestyle='--', alpha=0.5, linewidth=1.5)

        # Quadrant labels
        ax.text(gap_median * 1.5, priority_median * 1.8, 'HIGH\nPRIORITY',
               fontsize=12, ha='center', va='center', alpha=0.3, fontweight='bold')
        ax.text(gap_median * 0.5, priority_median * 1.8, 'MONITOR',
               fontsize=12, ha='center', va='center', alpha=0.3, fontweight='bold')
        ax.text(gap_median * 0.5, priority_median * 0.2, 'LOW\nPRIORITY',
               fontsize=12, ha='center', va='center', alpha=0.3, fontweight='bold')
        ax.text(gap_median * 1.5, priority_median * 0.2, 'QUICK\nWINS',
               fontsize=12, ha='center', va='center', alpha=0.3, fontweight='bold')

        ax.set_xlabel('Gap (Target - Current)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Priority Score', fontsize=12, fontweight='bold')
        ax.set_title('Improvement Priority Matrix', fontsize=14, fontweight='bold', pad=15)
        ax.legend(loc='upper left', frameon=True, shadow=True)
        ax.grid(True, alpha=0.3, linestyle='--')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def create_interactive_scorecard(
        self,
        scorecard_data: Dict,
        save_path: Optional[str] = None
    ) -> go.Figure:
        """
        Create interactive scorecard using Plotly.

        Args:
            scorecard_data: Dict with organizational scorecard data
            save_path: Optional path to save HTML

        Returns:
            Plotly figure
        """
        category_scores = scorecard_data['category_scores']
        categories = list(category_scores.keys())
        scores = list(category_scores.values())
        names = [self.CATEGORY_NAMES[c] for c in categories]

        # Create subplots
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Category Scores', 'Score Distribution'),
            specs=[[{'type': 'bar'}, {'type': 'pie'}]]
        )

        # Bar chart
        fig.add_trace(
            go.Bar(
                x=names,
                y=scores,
                marker=dict(
                    color=scores,
                    colorscale='RdYlGn',
                    line=dict(color='black', width=1.5),
                    showscale=False
                ),
                text=[f'{s:.1f}' for s in scores],
                textposition='outside',
                name='Scores'
            ),
            row=1, col=1
        )

        # Pie chart
        fig.add_trace(
            go.Pie(
                labels=names,
                values=scores,
                marker=dict(
                    colors=[self.CATEGORY_COLORS[c] for c in categories],
                    line=dict(color='white', width=2)
                ),
                textinfo='label+percent',
                name='Distribution'
            ),
            row=1, col=2
        )

        # Update layout
        fig.update_layout(
            title_text=f"Organizational Excellence Scorecard - Score: {scorecard_data.get('organizational_score', 0):.1f}",
            showlegend=False,
            height=500,
            font=dict(size=12)
        )

        fig.update_xaxes(title_text="Category", row=1, col=1)
        fig.update_yaxes(title_text="Score", range=[0, 100], row=1, col=1)

        if save_path:
            fig.write_html(save_path)

        return fig

    def plot_trend_analysis(
        self,
        trend_data: pd.DataFrame,
        category: int,
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create trend line chart for a specific category over time.

        Args:
            trend_data: DataFrame with columns ['period', 'score']
            category: Category number
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=(12, 6))

        ax.plot(
            trend_data['period'],
            trend_data['score'],
            marker='o',
            markersize=8,
            linewidth=2.5,
            color=self.CATEGORY_COLORS.get(category, '#1f77b4'),
            label='Actual Score'
        )

        # Add trend line (linear regression)
        z = np.polyfit(range(len(trend_data)), trend_data['score'], 1)
        p = np.poly1d(z)
        ax.plot(
            trend_data['period'],
            p(range(len(trend_data))),
            linestyle='--',
            linewidth=2,
            color='red',
            alpha=0.7,
            label=f'Trend (slope={z[0]:.2f})'
        )

        ax.set_xlabel('Period', fontsize=12, fontweight='bold')
        ax.set_ylabel('Score', fontsize=12, fontweight='bold')
        ax.set_title(
            f"Performance Trend - {self.CATEGORY_NAMES.get(category, f'Category {category}')}",
            fontsize=14,
            fontweight='bold',
            pad=15
        )
        ax.set_ylim(0, 100)
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.legend(loc='best', frameon=True, shadow=True)

        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig


def demo_visualizations():
    """Demonstrate all visualization capabilities."""
    print("Generating demonstration visualizations...")

    viz = ScoringVisualizer()

    # Sample data
    category_scores = {1: 75, 2: 68, 3: 82, 4: 70, 5: 74, 6: 69, 7: 87}
    target_scores = {1: 85, 2: 80, 3: 90, 4: 80, 5: 85, 6: 80, 7: 95}

    # 1. Radar chart
    print("Creating radar chart...")
    viz.plot_category_scores_radar(category_scores, target_scores)

    # 2. ADLI breakdown
    print("Creating ADLI breakdown...")
    adli_scores = {'Approach': 22.5, 'Deployment': 13.5, 'Learning': 12.0, 'Integration': 11.0}
    viz.plot_adli_breakdown(adli_scores)

    # 3. Gap analysis heatmap
    print("Creating gap analysis heatmap...")
    gap_data = pd.DataFrame({
        'category': [1,1,1,2,2,2,3,3,3],
        'item': [1,2,3,1,2,3,1,2,3],
        'gap': [10, 15, 7, 20, 18, 12, 8, 5, 10]
    })
    viz.plot_gap_analysis_heatmap(gap_data)

    plt.show()
    print("Demonstration complete!")


if __name__ == "__main__":
    demo_visualizations()
