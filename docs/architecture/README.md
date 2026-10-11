# Architecture Documentation

This directory describes the technical design, system components, and data flow of StatEDA-Explorer.

## System Flow

```mermaid
flowchart TD
    A[Raw Dataset Ingestion & Schema Parsing] --> B[Missing Value & Summary Statistics Audit]
    B --> C{Distribution Normality Assessment}
    C -->|Normal (Shapiro p > 0.05)| D[Parametric Tests: Welch's T-Test / ANOVA]
    C -->|Non-Normal (Shapiro p <= 0.05)| E[Non-Parametric Tests: Mann-Whitney U]
    B --> F[Categorical Feature Association: Chi-Square]
    B --> G[Correlation & Multicollinearity: VIF Score]
    D --> H[Export Summary & Render Dashboard]
    E --> H
    F --> H
    G --> H
```

## Components
- **`eda.py`**: Handles missing value computation and basic descriptive profiling.
- **`stats.py`**: The core inference engine wrapping `scipy.stats`. Handles automated decision-making on which tests to execute.
- **`collinearity.py`**: Computes Variance Inflation Factors via `statsmodels` to detect multicollinearity.
- **`viz.py`**: Wraps `seaborn` and `matplotlib` to produce presentation-ready visualizations.
- **`pipeline.py`**: The orchestrator binding all modules together into a unified API.