# Data Dictionary

The project uses two CSV files connected through `Order ID`.

## 1. Orders.csv

One row represents one order.

| Column | Meaning | Type / notes |
|---|---|---|
| Order ID | Unique identifier for an order | Text key |
| Order Date | Date the order was placed | Text in `DD-MM-YYYY` format in the source file |
| CustomerName | Customer name supplied in the dataset | Text |
| State | State associated with the order | Text; trim whitespace before grouping |
| City | City associated with the order | Text |

## 2. Details.csv

One row represents an order-detail/product record. An order can appear on multiple rows.

| Column | Meaning | Type / notes |
|---|---|---|
| Order ID | Identifier linking the detail row to Orders.csv | Text; many rows can share an ID |
| Amount | Sales amount recorded for the detail row | Numeric |
| Profit | Profit recorded for the detail row | Numeric; can be positive, zero or negative |
| Quantity | Quantity recorded for the detail row | Numeric |
| Category | Broad product category | Text |
| Sub-Category | More specific product grouping | Text |
| PaymentMode | Payment method recorded for the order-detail row | Text |

## Relationship

Use `Orders[Order ID]` as the one-side key and `Details[Order ID]` as the many-side key. The expected relationship is one-to-many from Orders to Details.

Do not count rows in Details.csv as orders. Use distinct Order ID values or an order-level aggregation when calculating order counts.

## Data observations

The current files contain:
- 500 order records in Orders.csv;
- 1,500 detail records in Details.csv;
- 500 distinct Order IDs in each file;
- no blank fields in the columns inspected;
- no exact duplicate rows in the detail file;
- no duplicate Order IDs in the order file; and
- matching Order IDs between the two files.

One state value is stored as `Kerala ` with a trailing space. Trim text fields before grouping so it is not treated as a separate state from `Kerala`.

## Important interpretation notes

- A negative `Profit` on a detail row is not automatically a loss-making order.
- To identify loss-making orders, sum Profit for all detail rows with the same Order ID, then count orders whose net profit is below zero.
- The source date strings use day-month-year order. Set the locale/date format explicitly during import to avoid interpreting dates incorrectly.
- Confirm the original dataset source and its reuse terms before redistributing the CSV files.
