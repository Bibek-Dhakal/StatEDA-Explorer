import numpy as np
import pandas as pd
from stateda.collinearity import compute_vif


def test_compute_vif_high_collinearity():
    # Create dataset with perfect collinearity
    x1 = np.random.rand(100)
    x2 = x1 * 2 + 0.001 * np.random.rand(100)
    x3 = np.random.rand(100)

    df = pd.DataFrame({"x1": x1, "x2": x2, "x3": x3})

    vif = compute_vif(df)

    # Features x1 and x2 should have very high VIF (> 10)
    vif_x1 = vif.loc[vif["Feature"] == "x1", "VIF Score"].values[0]
    vif_x2 = vif.loc[vif["Feature"] == "x2", "VIF Score"].values[0]

    assert vif_x1 > 10.0
    assert vif_x2 > 10.0

    # Feature x3 is random, should have low VIF
    vif_x3 = vif.loc[vif["Feature"] == "x3", "VIF Score"].values[0]
    assert vif_x3 < 5.0
