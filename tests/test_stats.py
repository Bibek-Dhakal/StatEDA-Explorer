import numpy as np
import pandas as pd
from stateda.stats import calculate_cohens_d, check_normality, run_two_sample_test


def test_normality_check():
    np.random.seed(42)
    # Generate a normal distribution
    normal_data = pd.Series(np.random.normal(loc=0, scale=1, size=100))
    # Generate a skewed/non-normal distribution
    skewed_data = pd.Series(np.random.exponential(scale=2, size=100))

    assert check_normality(normal_data), "Failed to identify normal distribution"
    assert not check_normality(skewed_data), "Failed to identify non-normal distribution"


def test_auto_test_selection():
    np.random.seed(42)

    # 1. Normal data for both groups -> Welch's T-Test
    df_normal = pd.DataFrame(
        {
            "target": np.concatenate([np.random.normal(0, 1, 50), np.random.normal(1, 1, 50)]),
            "group": ["A"] * 50 + ["B"] * 50,
        }
    )

    res_normal = run_two_sample_test(df_normal, "target", "group", "A", "B")
    assert res_normal["Test Applied"] == "Welch's T-Test"

    # 2. Skewed data for at least one group -> Mann-Whitney U
    df_skewed = pd.DataFrame(
        {
            "target": np.concatenate([np.random.exponential(1, 50), np.random.exponential(2, 50)]),
            "group": ["A"] * 50 + ["B"] * 50,
        }
    )

    res_skewed = run_two_sample_test(df_skewed, "target", "group", "A", "B")
    assert res_skewed["Test Applied"] == "Mann-Whitney U Test"


def test_cohens_d_computation():
    g1 = pd.Series([1, 2, 3, 4, 5])
    g2 = pd.Series([2, 3, 4, 5, 6])

    # Manually computed Cohen's d for these simple identical-variance sets is 0.6324
    d = calculate_cohens_d(g1, g2)
    assert np.isclose(d, 0.63245, atol=1e-4)
