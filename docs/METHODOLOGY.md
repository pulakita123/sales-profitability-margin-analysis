# Analysis Methodology

This document explains the workflow I followed and the checks used to make the analysis easier to reproduce.

## 1. Understand the files

I began by reviewing the two CSV files and identifying what each row represented.

- `Orders.csv` contains order-level information such as date, customer and location.
- `Details.csv` contains the financial and product details associated with each order.

The common field is `Order ID`. The two files should not be appended as if they contained the same type of record; they represent different levels of detail.

## 2. Inspect data quality

I checked the structure, row counts, blank values, duplicate records and key consistency.

The checks on the current files found 500 order rows and 1,500 detail rows. All 500 distinct order IDs in each file matched. No blank values were found in the inspected columns, and no exact duplicate detail rows or duplicate order IDs were detected in the order table.

I also noticed a trailing space in the state value `Kerala `. Text fields should be trimmed before grouping.

## 3. Prepare the data

In Power Query, the preparation should include:
- assigning numeric data types to Amount, Profit and Quantity;
- converting Order Date using the source format `DD-MM-YYYY`;
- trimming text columns such as State, Category, Sub-Category and PaymentMode;
- checking the Order ID relationship; and
- confirming that the model has one order record related to multiple detail records.

## 4. Build the data model

The core relationship is:

```text
Orders (1) ───────── (*) Details
        Order ID
```

The order table supplies date and geographic context. The detail table supplies sales, profit, quantity, category, sub-category and payment information.

A dedicated Date table is useful for month and quarter analysis. It should have a continuous date column, be related to the order date, and be marked as the model's date table.

## 5. Define the measures

The dashboard tracks sales, profit, profit margin, average order value, loss amount, loss-making orders, loss order rate and profit per order.

The key calculation is loss-making orders. Profit must first be aggregated by Order ID. Counting negative-profit detail rows would answer a different question and overstate the number of orders that ended with a net loss.

See [DAX Measures](DAX_MEASURES.md) for the business definitions and calculation logic.

## 6. Explore the data

I reviewed performance across:
- overall sales and profitability;
- categories and sub-categories;
- state and city;
- monthly and quarterly trends; and
- payment methods.

For each breakdown, I compared both sales and profit. High sales do not necessarily mean high profitability.

## 7. Validate the headline numbers

I independently recalculated the headline figures from the CSV files:
- sales = sum of Amount across detail rows;
- profit = sum of Profit across detail rows;
- profit margin = total profit divided by total sales;
- average order value = total sales divided by distinct orders;
- loss-making orders = count of orders whose aggregated profit is below zero; and
- net loss across loss-making orders = sum of the net profit values for those orders.

The recalculated results are ₹4,37,771 sales, ₹36,963 profit, 8.44% profit margin, ₹875.54 average order value, 169 loss-making orders and ₹26,127 combined net loss across those orders.

## 8. Interpret findings carefully

The data shows where negative profitability occurs, but it does not explain why. Without discount, product cost, shipping, return and advertising data, it would be misleading to claim that a particular operational factor caused the losses.

The recommendations should therefore be framed as investigation priorities rather than guaranteed fixes.
