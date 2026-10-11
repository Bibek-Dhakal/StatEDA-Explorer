import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def plot_correlation_heatmap(df: pd.DataFrame, figsize=(10, 8)):
    """
    Plots a seaborn heatmap of the correlation matrix for numerical features.
    """
    num_df = df.select_dtypes(include=[np.number])
    if num_df.empty:
        print("No numerical columns found to plot correlation.")
        return

    corr = num_df.corr()

    plt.figure(figsize=figsize)
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, square=True)
    plt.title("Correlation Matrix Heatmap")
    plt.tight_layout()
    plt.show()


def plot_target_distribution(df: pd.DataFrame, target_col: str, group_col: str = None):
    """
    Plots the KDE distribution of a target numerical variable, optionally segmented by a group.
    """
    plt.figure(figsize=(10, 6))
    if group_col and group_col in df.columns:
        sns.kdeplot(data=df, x=target_col, hue=group_col, fill=True, common_norm=False, alpha=0.5)
        plt.title(f"Distribution of {target_col} Grouped by {group_col}")
    else:
        sns.kdeplot(data=df, x=target_col, fill=True, alpha=0.5)
        plt.title(f"Distribution of {target_col}")

    plt.tight_layout()
    plt.show()
