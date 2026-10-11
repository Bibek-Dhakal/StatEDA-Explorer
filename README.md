# StatEDA-Explorer

Automated Exploratory Data Analysis (EDA) and Parametric/Non-Parametric Statistical Hypothesis Testing Engine.

When presented with a new dataset, teams often jump directly into training machine learning models without first evaluating feature distributions, identifying multi-collinearity, or checking if observed pattern differences across cohorts are statistically significant or merely random noise. **StatEDA-Explorer** bridges this gap.

## Features
- **Automated Missing Value & Summary Audit:** Profiles the dataset instantly.
- **Distribution Normality Assessment:** Automatically evaluates normality using Shapiro-Wilk testing to route workflows optimally.
- **Parametric vs. Non-Parametric Routing:** Intelligently switches between Student's T-Test and Mann-Whitney U based on underlying distribution shape.
- **Categorical Association Tests:** Chi-Square tests of independence.
- **Multicollinearity Audits:** VIF (Variance Inflation Factor) score computation.
- **Effect Size Estimation:** Automatically calculates Cohen's $d$ or Cramér's $V$ alongside $p$-values.

## Documentation Index
- [Usage Guide](docs/usage/README.md)
- [Architecture](docs/architecture/README.md)
- [Testing Guidelines](docs/testing/README.md)
- [Roadmap](docs/roadmap/README.md)

## Installation

```bash
git clone https://github.com/username/StatEDA-Explorer.git
cd StatEDA-Explorer
python -m venv venv
source venv/bin/activate
pip install -e .
```

## Quick Start

```python
import pandas as pd
import seaborn as sns
from stateda.pipeline import StatEDAPipeline

# Load dataset
df = sns.load_dataset("tips")

# Initialize Pipeline
pipeline = StatEDAPipeline(df)

# Run Auto-Hypothesis testing (Parametric vs Non-Parametric is auto-selected)
result = pipeline.run_hypothesis_test(target_col='total_bill', group_col='sex', group1='Male', group2='Female')
print(result)

# Check for Multicollinearity
vif = pipeline.run_collinearity_check()
print(vif)
```

## License
MIT License