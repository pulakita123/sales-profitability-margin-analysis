# Reproducing and Validating the Analysis

## Requirements

- Python 3.9 or later (the validation script uses only the standard library)
- Microsoft Power BI Desktop to open and interact with the PBIX dashboard

## Recalculate the headline KPIs

From the repository root, run:

```bash
python scripts/validate_data.py
```

The script reads `Details.csv` and `Orders.csv`, checks required columns, blank values, duplicate order IDs and key matching, then independently recalculates the headline sales and profitability metrics.

The most important check is the loss-making-order calculation: the script first adds profit across all detail rows for each Order ID, then counts orders whose combined profit is negative. This is intentionally different from counting negative-profit detail rows.

## Open the Power BI report

1. Download or clone this repository.
2. Open `ecommerce sales profit leakage dashboard.pbix` in Power BI Desktop.
3. If Power BI prompts for data-source locations, point it to the two CSV files in the repository.
4. Refresh the model and compare the report's headline cards with the validation script output.

Power BI Desktop may store local source paths in the PBIX. A reviewer may need to update those paths after downloading the repository.

## Reproducibility note

The validation script checks the source CSV data. It does not inspect the internal Power BI model or prove that every visual and DAX measure in the PBIX is configured correctly. The dashboard measures still need to be checked in Power BI Desktop.
