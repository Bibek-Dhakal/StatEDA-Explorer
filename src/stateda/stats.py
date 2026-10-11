from typing import Any, Dict

import numpy as np
import pandas as pd
from scipy import stats


def check_normality(series: pd.Series, alpha: float = 0.05) -> bool:
    """
    Check if a distribution is normal using the Shapiro-Wilk test.
    Returns True if normal (p > alpha), False otherwise.
    """
    data = series.dropna()
    if len(data) < 3:
        return False

    # Shapiro-Wilk can fail on n > 5000; scipy truncates it, so it's generally safe.
    stat, p_value = stats.shapiro(data)
    return p_value > alpha


def calculate_cohens_d(group1: pd.Series, group2: pd.Series) -> float:
    """
    Calculates Cohen's d for effect size.
    """
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)

    pooled_var = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)
    d = (np.mean(group1) - np.mean(group2)) / np.sqrt(pooled_var)
    return abs(d)


def calculate_cramers_v(confusion_matrix: pd.DataFrame) -> float:
    """
    Calculates Cramér's V statistic for categorical-categorical association.
    """
    chi2 = stats.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    rcorr = r - ((r - 1) ** 2) / (n - 1)
    kcorr = k - ((k - 1) ** 2) / (n - 1)
    return np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))


def run_two_sample_test(df: pd.DataFrame, target_col: str, group_col: str, group1: Any, group2: Any) -> Dict[str, Any]:
    """
    Automatically selects and runs the appropriate two-sample test (Parametric vs Non-Parametric)
    based on the normality of the distributions.
    """
    g1_data = df[df[group_col] == group1][target_col].dropna()
    g2_data = df[df[group_col] == group2][target_col].dropna()

    is_normal = check_normality(g1_data) and check_normality(g2_data)

    if is_normal:
        # Parametric: Welch's T-Test (does not assume equal variance)
        stat, p_val = stats.ttest_ind(g1_data, g2_data, equal_var=False)
        test_name = "Welch's T-Test"
    else:
        # Non-Parametric: Mann-Whitney U Test
        stat, p_val = stats.mannwhitneyu(g1_data, g2_data, alternative="two-sided")
        test_name = "Mann-Whitney U Test"

    effect_size = calculate_cohens_d(g1_data, g2_data)

    return {
        "Target": target_col,
        "Groups": f"{group1} vs {group2}",
        "Distributions Normal": is_normal,
        "Test Applied": test_name,
        "Statistic": round(stat, 4),
        "P-Value": round(p_val, 4),
        "Effect Size (Cohen's d)": round(effect_size, 4),
        "Significant (alpha=0.05)": p_val < 0.05,
    }


def run_categorical_test(df: pd.DataFrame, col1: str, col2: str) -> Dict[str, Any]:
    """
    Runs a Chi-Square test of independence between two categorical columns.
    """
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)

    effect_size = calculate_cramers_v(contingency_table)

    return {
        "Columns": f"{col1} vs {col2}",
        "Test Applied": "Chi-Square Test of Independence",
        "Statistic": round(chi2, 4),
        "P-Value": round(p_val, 4),
        "Degrees of Freedom": dof,
        "Effect Size (Cramér's V)": round(effect_size, 4),
        "Significant (alpha=0.05)": p_val < 0.05,
    }
