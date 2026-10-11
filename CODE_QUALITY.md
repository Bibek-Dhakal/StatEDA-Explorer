# Code Quality & Formatting Guidelines

**Header Note:** Automated quality checks (linting, formatting, and commit message validation) are strictly enforced and run on `git commit` via pre-commit hooks. If necessary, manual fallback commands exist.

## Environment Setup

To install, register, and activate the required git hooks and developer tools locally:

```bash
# 1. Install development dependencies
pip install -e ".[dev]"

# 2. Install pre-commit hooks to your local git repository
pre-commit install

# 3. Install commit-msg hook for Conventional Commits
pre-commit install --hook-type commit-msg
```

## Manual Execution Commands

### Running quality checks repository-wide on ALL files:
```bash
pre-commit run --all-files
```

### Running checks ONLY on staged files:
```bash
pre-commit run
```

### Running checks against specific files:
```bash
pre-commit run --files src/stateda/stats.py
```

## Isolated Tool Commands

To run individual code quality tools independently without triggering all pre-commit hooks:

```bash
# Run Ruff Linter
ruff check .

# Run Ruff Linter and auto-fix safe issues
ruff check --fix .

# Run Ruff Formatter
ruff format .
```

## Maintenance & Cache

Commands to update hooks/dependencies to their latest versions and clear local tool caches:

```bash
# Update pre-commit hooks to their latest versions
pre-commit autoupdate

# Clear pre-commit cache
pre-commit clean
```

## Emergency Bypassing

**Warning:** Use emergency bypasses responsibly. Bypassing checks may cause CI pipeline failures.

To bypass hooks during an emergency hotfix commit:
```bash
git commit -m "fix: emergency patch" --no-verify
```