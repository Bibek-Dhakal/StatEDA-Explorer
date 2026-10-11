from typing import Any, Dict

import pandas as pd

from .collinearity import compute_vif
from .eda import missing_value_audit, summary_statistics
from .stats import run_categorical_test, run_two_sample_test
from .viz import plot_correlation_heatmap, plot_target_distribution


class StatEDAPipeline:
    """
    Unified Pipeline orchestrating the automated EDA and hypothesis testing workflows.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def run_basic_audit(self) -> Dict[str, pd.DataFrame]:
        """Runs missing values check and basic summary statistics."""
        return {"missing_values": missing_value_audit(self.df), "summary_statistics": summary_statistics(self.df)}

    def run_collinearity_check(self) -> pd.DataFrame:
        """Calculates VIF scores for the numerical features."""
        return compute_vif(self.df)

    def run_hypothesis_test(self, target_col: str, group_col: str, group1: Any, group2: Any) -> Dict[str, Any]:
        """
        Executes a two-sample statistical test on a numerical target segmented by two classes.
        Automatically handles normality assessment.
        """
        return run_two_sample_test(self.df, target_col, group_col, group1, group2)

    def run_categorical_association(self, col1: str, col2: str) -> Dict[str, Any]:
        """Executes a Chi-Square test of independence between two categorical variables."""
        return run_categorical_test(self.df, col1, col2)

    def visualize_eda(self, target_dist_col: str = None, group_dist_col: str = None):
        """Renders correlation heatmaps and, optionally, distribution plots."""
        plot_correlation_heatmap(self.df)
        if target_dist_col:
            plot_target_distribution(self.df, target_dist_col, group_dist_col)
