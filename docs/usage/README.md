# Usage Documentation

This directory contains the operational workflows, usage examples, and configuration references for StatEDA-Explorer.

## Sibling Documents
*(Currently, all usage details are captured in this file. Add dedicated files here as the project grows.)*

## Environment Variables
The application supports the following configurations via `.env` or system environment variables:

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `DATA_DIR` | String | `./data` | Directory where raw datasets are stored. |
| `OUTPUT_DIR` | String | `./outputs` | Directory where rendered plots and HTML tables are saved. |
| `LOG_LEVEL` | String | `INFO` | Standard logging level (e.g., INFO, DEBUG, WARNING). |

## Available Commands
- **Linting:** `ruff check .`
- **Formatting:** `ruff format .`
- **Testing:** `pytest tests/`