# Profitability Under the Lens: Sales & Margin Analysis | Power BI

An interactive Power BI analysis of 500 e-commerce orders, built to understand not only how much the business sells, but where it makes money, where it loses money, and which areas deserve closer attention.

[**View the Power BI dashboard file**](./ecommerce%20sales%20profit%20leakage%20dashboard.pbix)

---

## Project at a glance

| Metric | Result |
|---|---:|
| Orders analysed | 500 |
| Order-detail records | 1,500 |
| Total sales | ₹4,37,771 |
| Net profit | ₹36,963 |
| Overall profit margin | 8.44% |
| Average order value | ₹875.54 |
| Loss-making orders | 169 (33.8%) |
| Net loss across loss-making orders | ₹26,127 |

The figures above were recalculated from the CSV files in this repository. An order can contain multiple product-detail records, so the 1,500 detail rows should not be confused with the 500 distinct orders.

## The business problem

A sales report can make a business look healthy while hiding products and orders that are reducing its profit. I wanted to look beyond total revenue and use the available order data to answer a more useful business question:

**Which parts of this e-commerce business are contributing to profit, and where should management investigate possible profit leakage?**

The analysis focuses on five practical questions:

1. How much revenue and profit did the business generate?
2. How many orders ended with a net loss, and how large were those losses?
3. Which categories and sub-categories show weaker profitability?
4. Are there regions where the business is losing money?
5. How does profitability vary by month and payment method?

The purpose is to help a business team decide where to investigate pricing, discounting, product mix, regional performance and order-level profitability. The dataset does not contain cost, discount, shipping or return details, so the analysis identifies patterns for investigation rather than proving the cause of a loss.

## Dashboard preview

### Sales and profitability overview

<img width="1071" alt="Sales and profitability dashboard" src="https://github.com/user-attachments/assets/f6002bf2-fcf6-45ce-b855-c942284c9af0" />

### Profit leakage investigation

<img width="1054" alt="Profit leakage investigation dashboard" src="https://github.com/user-attachments/assets/9894f779-77f3-4fcb-80b4-ad032827c02b" />

## What I found

### 1. Sales were positive, but one in three orders was loss-making

The business generated ₹4.38 lakh in sales and ₹36,963 in net profit, with an overall margin of 8.44%. However, 169 of the 500 orders (33.8%) had negative net profit. Those loss-making orders together contributed ₹26,127 in negative profit.

This is why I treated order-level profitability as a separate KPI instead of relying on revenue and total profit alone.

### 2. Category performance was closer than sales alone might suggest

Clothing generated ₹13,325 in net profit, Electronics ₹13,162 and Furniture ₹10,476. Electronics did not record a ₹13.2K net loss; that figure is its positive net profit in the detail data. The category results are relatively close, so a useful next step would be to examine the product mix and loss-making orders within each category rather than assuming that the highest-sales category is automatically the healthiest.

### 3. Some sub-categories need closer attention

Furnishings recorded a net loss of ₹806 and Electronic Games recorded a net loss of ₹644. Other sub-categories, including Kurti, Skirt and Leggings, also ended with negative net profit in the supplied detail data.

Printers and Bookcases were among the stronger sub-categories by total net profit, at ₹8,606 and ₹6,516 respectively.

### 4. Two states recorded negative net profit

Rajasthan recorded a net loss of ₹323 and Andhra Pradesh recorded a net loss of ₹280. These are modest negative totals in this dataset, but they are useful flags for a closer review of order mix and transaction-level performance.

Madhya Pradesh and Maharashtra generated the largest total profits in the supplied data, at ₹7,382 and ₹6,963 respectively.

### 5. Payment method is another useful comparison, not a proven cause

Credit Card and COD transactions generated the highest total profits in the supplied detail data, at ₹12,612 and ₹12,547. This is a descriptive comparison only. The available fields do not establish that the payment method caused a difference in profitability.

More detail on the findings and interpretation is available in [Key Findings](docs/KEY_FINDINGS.md).

## How I approached the analysis

I started by understanding the two files and how they relate to each other. `Orders.csv` contains one record per order, including its date and delivery location. `Details.csv` contains the product and financial details associated with each order. The common field is `Order ID`.

I then checked the record counts, missing values, duplicate records and whether every order ID could be matched between the two files. After that, I reviewed the date and category fields, connected the order and detail data for time and regional analysis, and built measures to compare sales with profit.

The most important analytical decision was to calculate loss-making orders at the **order level**. A single order can have several product rows, and one negative-profit product row does not necessarily mean that the entire order lost money. I therefore aggregated profit by Order ID before counting loss-making orders.

The complete workflow and validation notes are in [Methodology](docs/METHODOLOGY.md). The first-person end-to-end business write-up is available in the [Project Report](docs/PROJECT_REPORT.md).

## Tools and skills

- **Power BI:** interactive reporting, visuals, slicers and cross-filtering
- **Power Query:** data inspection and preparation
- **DAX:** KPI calculations and profitability measures
- **Data modelling:** connecting order-level and order-detail data
- **Business analysis:** defining the problem, interpreting patterns and translating findings into investigation priorities

## Repository contents

```text
sales-profitability-margin-analysis/
├── README.md
├── Details.csv
├── Orders.csv
├── ecommerce sales profit leakage dashboard.pbix
├── scripts/
│   └── validate_data.py
└── docs/
    ├── BUSINESS_PROBLEM.md
    ├── DATA_DICTIONARY.md
    ├── DAX_MEASURES.md
    ├── KEY_FINDINGS.md
    ├── METHODOLOGY.md
    ├── PROJECT_REPORT.md
    └── REPRODUCING_ANALYSIS.md
```

## How to explore the project

1. Open the Power BI file linked above using Microsoft Power BI Desktop.
2. If Power BI asks for the source files, point the queries to the included `Orders.csv` and `Details.csv` files.
3. Review the overview page first, then use the profitability and loss analysis visuals to investigate categories, sub-categories, regions, months and payment methods.
4. Read the documentation in the `docs/` folder for the business context, data definitions, calculations and findings.

The PBIX file is included as the interactive deliverable. The CSV files are included so that the data structure can be reviewed. You can also run the independent data checks using the [validation script](scripts/validate_data.py); setup instructions are in [Reproducing the Analysis](docs/REPRODUCING_ANALYSIS.md).

## Limitations and next steps

This is a focused analysis of the fields available in the supplied dataset. It does not include product cost breakdowns, discount details, shipping charges, returns, advertising spend or customer acquisition cost. Those fields would be needed to explain the operational reasons behind losses and to estimate the financial impact of specific interventions.

If I were extending this analysis, I would:
- investigate the individual loss-making orders and their product mix;
- add discount, shipping and return data to explain margin erosion;
- compare profitability by customer segment and repeat-purchase behaviour;
- build a drill-through view for order-level investigation; and
- validate the dashboard measures against an independent calculation.

## About this project

This is a portfolio project demonstrating how I approach a business question with transactional data, use Power BI to investigate performance, and communicate findings in a way that can support further business decisions.

---

*Dataset provenance and usage permissions should be confirmed and credited here before redistribution. The CSV files are included in this repository; no external source or licence is claimed in this README.*
