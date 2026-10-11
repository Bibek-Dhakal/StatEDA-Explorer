# Contributing to StatEDA-Explorer

First off, thank you for considering contributing to StatEDA-Explorer! 

## Code Style & Testing
- We use `Ruff` for code linting and formatting.
- Ensure all tests pass by running `pytest tests/` before submitting a PR.
- Add unit tests for any new statistical or utility functions.

## Commit Message Guidelines (Strict Enforcement)

This repository strictly enforces **Conventional Commits**. All commit messages (and PR titles) drive automated versioning and `CHANGELOG.md` generation via `release-please` automated Release PRs. 

### Commit Format
```text
<type>(<optional scope>): <description>
```

### Allowed Types
* **feat**: A new feature (triggers a Minor release).
* **fix**: A bug fix (triggers a Patch release).
* **feat!** or **fix!**: Includes a breaking change (triggers a Major release).
* **docs**: Documentation only changes.
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, etc.).
* **refactor**: A code change that neither fixes a bug nor adds a feature.
* **test**: Adding missing tests or correcting existing tests.
* **chore**: Changes to the build process or auxiliary tools and libraries.

### Release Workflow
By default, `release-please` aggregates all incoming changes on `main` into a long-running, managed Release PR (`chore: release x.y.z`). Modifying `main` updates this Release PR without immediately publishing a release tag. A new release, version bump, and official `CHANGELOG.md` update are finalized **only when the Release PR is merged into main**.