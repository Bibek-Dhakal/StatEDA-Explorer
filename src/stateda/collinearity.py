import numpy as np
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant


def compute_vif(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the Variance Inflation Factor (VIF) for all numerical features
    to detect multicollinearity.
    """
    # Select numerical columns and drop missing values for VIF computation
    num_df = df.select_dtypes(include=[np.number]).dropna()

    if num_df.empty or num_df.shape[1] < 2:
        return pd.DataFrame(columns=["Feature", "VIF Score"])

    # Add a constant (intercept) for statsmodels OLS compatibility
    X = add_constant(num_df)

    vif_data = pd.DataFrame()
    vif_data["Feature"] = X.columns
    vif_data["VIF Score"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]

    # Filter out the constant term
    result = vif_data[vif_data["Feature"] != "const"].copy()
    result = result.sort_values(by="VIF Score", ascending=False).reset_index(drop=True)

    return result
