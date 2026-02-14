"""
Advanced Visualization Module
==============================

High-quality statistical and interactive visualizations for
organizational excellence assessment and research publication.

Authors:
    Rungtiva Saosing, Chatchai Tritham, Chattabhorn Tritham, Sudasawan Ngammongkolwong
    Faculty of Science and Technology, Rajamangala University of Technology Krungthep

Features:
    - Statistical distribution plots (Box, Violin, Density)
    - Correlation matrices and heatmaps
    - Network diagrams for category dependencies
    - Sunburst charts for hierarchical data
    - Sankey diagrams for flow analysis
    - Time series decomposition
    - 3D interactive scatter plots
    - Animated performance evolution
"""

from typing import Dict, List, Optional, Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from matplotlib.patches import FancyBboxPatch
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import networkx as nx
from matplotlib.patches import Circle, Rectangle, FancyArrow
import matplotlib.patches as mpatches


class AdvancedVisualizer:
    """
    Advanced visualization suite for organizational excellence analytics.

    Provides publication-quality statistical plots, network visualizations,
    and interactive 3D charts for research and commercial applications.
    """

    # Professional color palettes
    PALETTE_QUALITATIVE = px.colors.qualitative.Set3
    PALETTE_SEQUENTIAL = px.colors.sequential.Viridis
    PALETTE_DIVERGING = px.colors.diverging.RdYlGn

    def __init__(self):
        """Initialize advanced visualizer with professional styling."""
        sns.set_palette("husl")
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 300
        plt.rcParams['font.family'] = 'DejaVu Sans'

    def plot_distribution_comparison(
        self,
        data_dict: Dict[str, List[float]],
        title: str = "Score Distribution Comparison",
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create box plots and violin plots for distribution comparison.

        Args:
            data_dict: Dict of {category_name: [scores]}
            title: Plot title
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure with subplots
        """
        fig, axes = plt.subplots(2, 1, figsize=(14, 10))

        # Prepare data
        categories = list(data_dict.keys())
        data_list = list(data_dict.values())

        # Box plot
        bp = axes[0].boxplot(
            data_list,
            labels=categories,
            patch_artist=True,
            notch=True,
            showmeans=True,
            meanprops=dict(marker='D', markerfacecolor='red', markersize=8)
        )

        # Color boxes
        colors = plt.cm.Set3(np.linspace(0, 1, len(categories)))
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)

        axes[0].set_ylabel('Score', fontsize=12, fontweight='bold')
        axes[0].set_title(f'{title} - Box Plot', fontsize=14, fontweight='bold')
        axes[0].grid(axis='y', alpha=0.3, linestyle='--')
        axes[0].set_ylim(0, 100)

        # Violin plot
        positions = np.arange(1, len(categories) + 1)
        parts = axes[1].violinplot(
            data_list,
            positions=positions,
            showmeans=True,
            showmedians=True,
            widths=0.7
        )

        # Color violin plots
        for i, pc in enumerate(parts['bodies']):
            pc.set_facecolor(colors[i])
            pc.set_alpha(0.7)

        axes[1].set_xticks(positions)
        axes[1].set_xticklabels(categories, rotation=45, ha='right')
        axes[1].set_ylabel('Score', fontsize=12, fontweight='bold')
        axes[1].set_title(f'{title} - Violin Plot', fontsize=14, fontweight='bold')
        axes[1].grid(axis='y', alpha=0.3, linestyle='--')
        axes[1].set_ylim(0, 100)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_correlation_matrix(
        self,
        correlation_data: pd.DataFrame,
        title: str = "Category Score Correlation Matrix",
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create annotated correlation matrix heatmap.

        Args:
            correlation_data: DataFrame with correlation values
            title: Plot title
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=(12, 10))

        # Compute correlation matrix
        corr = correlation_data.corr()

        # Mask for upper triangle
        mask = np.triu(np.ones_like(corr, dtype=bool))

        # Create heatmap
        sns.heatmap(
            corr,
            mask=mask,
            annot=True,
            fmt='.2f',
            cmap='RdYlGn',
            center=0,
            square=True,
            linewidths=1,
            cbar_kws={'label': 'Correlation Coefficient'},
            vmin=-1,
            vmax=1,
            ax=ax
        )

        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_category_network(
        self,
        category_scores: Dict[int, float],
        dependencies: List[Tuple[int, int]],
        category_names: Dict[int, str],
        title: str = "Category Dependency Network",
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create network diagram showing category dependencies.

        Args:
            category_scores: Dict of {category: score}
            dependencies: List of (source, target) tuples
            category_names: Dict of {category: name}
            title: Plot title
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=(16, 12))

        # Create directed graph
        G = nx.DiGraph()

        # Add nodes with scores as attributes
        for cat_id, score in category_scores.items():
            G.add_node(cat_id, score=score, name=category_names[cat_id])

        # Add edges
        G.add_edges_from(dependencies)

        # Layout
        pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

        # Draw nodes with size based on score
        node_sizes = [category_scores[node] * 30 for node in G.nodes()]
        node_colors = [category_scores[node] for node in G.nodes()]

        nodes = nx.draw_networkx_nodes(
            G, pos,
            node_size=node_sizes,
            node_color=node_colors,
            cmap='RdYlGn',
            vmin=0,
            vmax=100,
            alpha=0.9,
            edgecolors='black',
            linewidths=2,
            ax=ax
        )

        # Draw edges with arrows
        nx.draw_networkx_edges(
            G, pos,
            edge_color='gray',
            arrows=True,
            arrowsize=20,
            arrowstyle='->',
            width=2,
            alpha=0.6,
            ax=ax
        )

        # Draw labels
        labels = {node: f"{G.nodes[node]['name']}\n{category_scores[node]:.1f}"
                 for node in G.nodes()}
        nx.draw_networkx_labels(
            G, pos,
            labels,
            font_size=10,
            font_weight='bold',
            font_color='black',
            ax=ax
        )

        # Colorbar
        sm = plt.cm.ScalarMappable(cmap='RdYlGn', norm=plt.Normalize(vmin=0, vmax=100))
        sm.set_array([])
        cbar = plt.colorbar(sm, ax=ax, label='Score', shrink=0.8)

        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.axis('off')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def create_sunburst_chart(
        self,
        hierarchical_data: Dict,
        title: str = "Organizational Excellence Hierarchy",
        save_path: Optional[str] = None
    ) -> go.Figure:
        """
        Create interactive sunburst chart for hierarchical data.

        Args:
            hierarchical_data: Dict with 'labels', 'parents', 'values'
            title: Plot title
            save_path: Optional path to save HTML

        Returns:
            Plotly figure
        """
        fig = go.Figure(go.Sunburst(
            labels=hierarchical_data['labels'],
            parents=hierarchical_data['parents'],
            values=hierarchical_data['values'],
            branchvalues='total',
            marker=dict(
                colors=hierarchical_data.get('colors', None),
                colorscale='RdYlGn',
                cmid=50,
                line=dict(color='white', width=2)
            ),
            hovertemplate='<b>%{label}</b><br>Score: %{value:.1f}<extra></extra>',
        ))

        fig.update_layout(
            title=dict(
                text=title,
                font=dict(size=20, family='Arial Black')
            ),
            width=900,
            height=900,
            margin=dict(t=80, b=20, l=20, r=20)
        )

        if save_path:
            fig.write_html(save_path)

        return fig

    def create_sankey_diagram(
        self,
        flow_data: Dict[str, List],
        title: str = "Performance Flow Analysis",
        save_path: Optional[str] = None
    ) -> go.Figure:
        """
        Create Sankey diagram for flow analysis.

        Args:
            flow_data: Dict with 'source', 'target', 'value', 'labels'
            title: Plot title
            save_path: Optional path to save HTML

        Returns:
            Plotly figure
        """
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color='black', width=0.5),
                label=flow_data['labels'],
                color='lightblue'
            ),
            link=dict(
                source=flow_data['source'],
                target=flow_data['target'],
                value=flow_data['value'],
                color='rgba(0,0,0,0.2)'
            )
        )])

        fig.update_layout(
            title=dict(
                text=title,
                font=dict(size=18, family='Arial Black')
            ),
            font=dict(size=12),
            height=600,
            width=1200
        )

        if save_path:
            fig.write_html(save_path)

        return fig

    def plot_temporal_decomposition(
        self,
        time_series: pd.DataFrame,
        category: str,
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create time series decomposition plot.

        Args:
            time_series: DataFrame with 'period' and 'score' columns
            category: Category name
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        from scipy import signal

        fig, axes = plt.subplots(4, 1, figsize=(14, 12))

        # Original series
        axes[0].plot(time_series['period'], time_series['score'],
                    marker='o', linewidth=2, markersize=8, color='#2E86AB')
        axes[0].set_title(f'{category} - Original Series',
                         fontsize=12, fontweight='bold')
        axes[0].set_ylabel('Score', fontweight='bold')
        axes[0].grid(True, alpha=0.3)

        # Trend (moving average)
        window = min(3, len(time_series) // 2)
        if window >= 2:
            trend = time_series['score'].rolling(window=window, center=True).mean()
            axes[1].plot(time_series['period'], trend,
                        linewidth=2, color='#A23B72')
            axes[1].set_title('Trend Component', fontsize=12, fontweight='bold')
            axes[1].set_ylabel('Score', fontweight='bold')
            axes[1].grid(True, alpha=0.3)

            # Detrended
            detrended = time_series['score'] - trend
            axes[2].plot(time_series['period'], detrended,
                        marker='o', linewidth=1, markersize=6, color='#F18F01')
            axes[2].axhline(y=0, color='red', linestyle='--', alpha=0.7)
            axes[2].set_title('Detrended Component', fontsize=12, fontweight='bold')
            axes[2].set_ylabel('Deviation', fontweight='bold')
            axes[2].grid(True, alpha=0.3)

            # Residuals
            residuals = detrended.dropna()
            axes[3].bar(range(len(residuals)), residuals, color='#6A994E', alpha=0.7)
            axes[3].axhline(y=0, color='red', linestyle='--', alpha=0.7)
            axes[3].set_title('Residuals', fontsize=12, fontweight='bold')
            axes[3].set_ylabel('Residual', fontweight='bold')
            axes[3].set_xlabel('Period Index', fontweight='bold')
            axes[3].grid(True, alpha=0.3)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def create_3d_scatter_interactive(
        self,
        data: pd.DataFrame,
        x_col: str,
        y_col: str,
        z_col: str,
        color_col: str,
        title: str = "3D Performance Analysis",
        save_path: Optional[str] = None
    ) -> go.Figure:
        """
        Create interactive 3D scatter plot.

        Args:
            data: DataFrame with data
            x_col, y_col, z_col: Column names for axes
            color_col: Column for color coding
            title: Plot title
            save_path: Optional path to save HTML

        Returns:
            Plotly figure
        """
        fig = go.Figure(data=[go.Scatter3d(
            x=data[x_col],
            y=data[y_col],
            z=data[z_col],
            mode='markers',
            marker=dict(
                size=10,
                color=data[color_col],
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title=color_col),
                line=dict(color='white', width=1)
            ),
            text=data.index,
            hovertemplate=
                f'<b>%{{text}}</b><br>' +
                f'{x_col}: %{{x:.1f}}<br>' +
                f'{y_col}: %{{y:.1f}}<br>' +
                f'{z_col}: %{{z:.1f}}<br>' +
                f'{color_col}: %{{marker.color:.1f}}<extra></extra>'
        )])

        fig.update_layout(
            title=dict(text=title, font=dict(size=18, family='Arial Black')),
            scene=dict(
                xaxis=dict(title=x_col, backgroundcolor='rgb(230, 230,230)'),
                yaxis=dict(title=y_col, backgroundcolor='rgb(230, 230,230)'),
                zaxis=dict(title=z_col, backgroundcolor='rgb(230, 230,230)'),
            ),
            width=1000,
            height=800,
            margin=dict(l=0, r=0, b=0, t=40)
        )

        if save_path:
            fig.write_html(save_path)

        return fig

    def plot_statistical_summary(
        self,
        data_dict: Dict[str, List[float]],
        title: str = "Statistical Summary by Category",
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """
        Create comprehensive statistical summary plot.

        Args:
            data_dict: Dict of {category: [scores]}
            title: Plot title
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))

        categories = list(data_dict.keys())

        # 1. Mean with confidence intervals
        means = [np.mean(data_dict[cat]) for cat in categories]
        stds = [np.std(data_dict[cat]) for cat in categories]
        sems = [stats.sem(data_dict[cat]) for cat in categories]
        ci95 = [1.96 * sem for sem in sems]

        x_pos = np.arange(len(categories))
        axes[0, 0].bar(x_pos, means, yerr=ci95, capsize=5,
                      color='skyblue', edgecolor='black', linewidth=1.5, alpha=0.8)
        axes[0, 0].set_xticks(x_pos)
        axes[0, 0].set_xticklabels(categories, rotation=45, ha='right')
        axes[0, 0].set_ylabel('Mean Score', fontweight='bold')
        axes[0, 0].set_title('Mean Scores with 95% CI', fontweight='bold')
        axes[0, 0].grid(axis='y', alpha=0.3)
        axes[0, 0].set_ylim(0, 100)

        # 2. Coefficient of variation
        cvs = [(std / mean * 100) if mean > 0 else 0
               for mean, std in zip(means, stds)]
        axes[0, 1].bar(x_pos, cvs, color='coral', edgecolor='black',
                      linewidth=1.5, alpha=0.8)
        axes[0, 1].set_xticks(x_pos)
        axes[0, 1].set_xticklabels(categories, rotation=45, ha='right')
        axes[0, 1].set_ylabel('CV (%)', fontweight='bold')
        axes[0, 1].set_title('Coefficient of Variation', fontweight='bold')
        axes[0, 1].grid(axis='y', alpha=0.3)
        axes[0, 1].axhline(y=20, color='red', linestyle='--',
                          label='High Variability (20%)', alpha=0.7)
        axes[0, 1].legend()

        # 3. Min-Max range
        mins = [np.min(data_dict[cat]) for cat in categories]
        maxs = [np.max(data_dict[cat]) for cat in categories]
        ranges = [max_val - min_val for min_val, max_val in zip(mins, maxs)]

        axes[1, 0].bar(x_pos, ranges, color='lightgreen',
                      edgecolor='black', linewidth=1.5, alpha=0.8)
        axes[1, 0].set_xticks(x_pos)
        axes[1, 0].set_xticklabels(categories, rotation=45, ha='right')
        axes[1, 0].set_ylabel('Range', fontweight='bold')
        axes[1, 0].set_title('Score Range (Max - Min)', fontweight='bold')
        axes[1, 0].grid(axis='y', alpha=0.3)

        # 4. Quartile visualization
        q1s = [np.percentile(data_dict[cat], 25) for cat in categories]
        medians = [np.percentile(data_dict[cat], 50) for cat in categories]
        q3s = [np.percentile(data_dict[cat], 75) for cat in categories]

        axes[1, 1].plot(x_pos, q1s, marker='v', label='Q1 (25%)', linewidth=2)
        axes[1, 1].plot(x_pos, medians, marker='o', label='Median', linewidth=2)
        axes[1, 1].plot(x_pos, q3s, marker='^', label='Q3 (75%)', linewidth=2)
        axes[1, 1].fill_between(x_pos, q1s, q3s, alpha=0.3)
        axes[1, 1].set_xticks(x_pos)
        axes[1, 1].set_xticklabels(categories, rotation=45, ha='right')
        axes[1, 1].set_ylabel('Score', fontweight='bold')
        axes[1, 1].set_title('Quartile Distribution', fontweight='bold')
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].legend()
        axes[1, 1].set_ylim(0, 100)

        fig.suptitle(title, fontsize=16, fontweight='bold', y=1.00)
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def create_parallel_coordinates(
        self,
        data: pd.DataFrame,
        dimensions: List[str],
        color_col: str,
        title: str = "Parallel Coordinates Analysis",
        save_path: Optional[str] = None
    ) -> go.Figure:
        """
        Create parallel coordinates plot for multivariate analysis.

        Args:
            data: DataFrame with data
            dimensions: List of column names for dimensions
            color_col: Column for color coding
            title: Plot title
            save_path: Optional path to save HTML

        Returns:
            Plotly figure
        """
        fig = go.Figure(data=
            go.Parcoords(
                line=dict(
                    color=data[color_col],
                    colorscale='Viridis',
                    showscale=True,
                    cmin=data[color_col].min(),
                    cmax=data[color_col].max()
                ),
                dimensions=[
                    dict(
                        label=dim,
                        values=data[dim],
                        range=[0, 100]
                    ) for dim in dimensions
                ]
            )
        )

        fig.update_layout(
            title=dict(text=title, font=dict(size=18, family='Arial Black')),
            width=1200,
            height=600,
            margin=dict(l=100, r=100, b=50, t=80)
        )

        if save_path:
            fig.write_html(save_path)

        return fig


def create_sample_hierarchical_data():
    """Create sample data for sunburst chart."""
    return {
        'labels': [
            'Organization',
            'Leadership', 'Strategy', 'Customers', 'Measurement',
            'Workforce', 'Operations', 'Results',
            'L1', 'L2', 'L3', 'S1', 'S2', 'S3',
            'C1', 'C2', 'C3', 'M1', 'M2', 'M3',
            'W1', 'W2', 'W3', 'O1', 'O2', 'O3',
            'R1', 'R2', 'R3'
        ],
        'parents': [
            '',
            'Organization', 'Organization', 'Organization', 'Organization',
            'Organization', 'Organization', 'Organization',
            'Leadership', 'Leadership', 'Leadership',
            'Strategy', 'Strategy', 'Strategy',
            'Customers', 'Customers', 'Customers',
            'Measurement', 'Measurement', 'Measurement',
            'Workforce', 'Workforce', 'Workforce',
            'Operations', 'Operations', 'Operations',
            'Results', 'Results', 'Results'
        ],
        'values': [
            0,  # Organization (parent, no value)
            75, 68, 82, 70, 74, 69, 87,  # Categories
            75, 72, 78, 65, 59, 70,  # L, S items
            80, 85, 82, 68, 72, 70,  # C, M items
            74, 76, 75, 69, 71, 68,  # W, O items
            88, 85, 90  # R items
        ]
    }


if __name__ == "__main__":
    print("Advanced Visualization Module Loaded")
    print("=" * 60)
    print("\nAvailable visualizations:")
    print("  1. Distribution comparison (Box + Violin plots)")
    print("  2. Correlation matrix heatmap")
    print("  3. Category dependency network")
    print("  4. Sunburst chart (hierarchical)")
    print("  5. Sankey diagram (flow analysis)")
    print("  6. Temporal decomposition")
    print("  7. 3D scatter (interactive)")
    print("  8. Statistical summary panel")
    print("  9. Parallel coordinates")
