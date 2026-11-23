# DAX Measures — Business Definitions

This file documents what the dashboard measures should mean from a business perspective. The exact DAX expressions and table/column names should be checked against the PBIX model before treating this as a code reference.

| Measure | Business definition | Calculation logic |
|---|---|---|
| Total Sales | Total sales value represented by the detail records | Sum of Details[Amount] |
| Total Profit | Net profit represented by the detail records | Sum of Details[Profit] |
| Profit Margin | Profit earned for each rupee of sales | Total Profit divided by Total Sales |
| Total Orders | Number of distinct orders | Distinct count of Orders[Order ID] |
| Average Order Value (AOV) | Average sales value per order | Total Sales divided by Total Orders |
| Profit per Order | Average net profit per order | Total Profit divided by Total Orders |
| Loss-Making Orders | Orders whose combined detail-row profit is below zero | Aggregate Profit by Order ID, then count orders with net profit below zero |
| Loss Order Rate | Share of all orders that ended with negative net profit | Loss-Making Orders divided by Total Orders |
| Loss Amount | Magnitude of the combined net loss from loss-making orders | Absolute value of the sum of order-level profit for orders with net profit below zero |

## Why order-level aggregation matters

An order may contain multiple detail rows. One row can have negative profit while another row in the same order has positive profit. Therefore, counting negative detail rows does not give the number of loss-making orders.

For this project, the order-level result is:
- 169 orders with net profit below zero;
- ₹26,127 combined net loss across those orders.

## Validation

Before publishing exact DAX formulas, compare each measure in Power BI with an independent calculation from the CSV files. In particular, confirm that Loss-Making Orders is calculated after grouping by Order ID and not by counting negative-profit detail rows.
