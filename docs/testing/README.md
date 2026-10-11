# Testing Documentation

This directory outlines the testing strategies and CI integration workflows.

## Strategy
- **Unit Tests:** Execute granular tests on statistical formulas (e.g., ensuring Cohen's D computes accurately and VIF matches known outputs).
- **Integration Tests:** Verify that the automated normality threshold effectively switches between parametric and non-parametric tests on skewed vs. normal dummy data.

## Execution
Run the full suite using:
```bash
pytest tests/
```

To run with coverage:
```bash
pytest tests/ --cov=stateda
```