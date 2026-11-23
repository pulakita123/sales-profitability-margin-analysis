# Project Report: Profitability Under the Lens — Sales & Margin Analysis

## 1. Introduction

For this project, I wanted to look beyond sales totals and understand how well an e-commerce business was actually performing. Revenue is important, but it does not show whether individual orders are profitable or where losses may be building up.

I used Power BI to explore order-level and product-level performance, with a focus on identifying loss-making orders and areas that deserve further investigation.

## 2. Business problem

The main question was:

**If the business is generating sales and positive overall profit, are there still orders, products or regions that are reducing its profitability?**

To investigate this, I looked at sales, net profit, margin, average order value, loss-making orders, category performance, sub-category performance, regional results and payment methods.

## 3. Data understanding and preparation

The project contains two related files. `Orders.csv` stores order-level information such as order date and delivery location. `Details.csv` contains product-level financial information associated with each order. The common field is `Order ID`.

I reviewed the relationship between the files and treated the detail table and order table as different grains. This distinction matters because one order can contain multiple product rows.

For the loss-making-order KPI, I first aggregated profit across all detail rows belonging to the same order. I then counted orders whose combined profit was negative. Counting negative-profit product rows would answer a different question.

## 4. Key results

| Measure | Result |
|---|---:|
| Distinct orders | 500 |
| Order-detail records | 1,500 |
| Sales | ₹4,37,771 |
| Net profit | ₹36,963 |
| Overall profit margin | 8.44% |
| Average order value | ₹875.54 |
| Loss-making orders | 169 (33.8%) |
| Combined net loss across loss-making orders | ₹26,127 |

The business was profitable overall, but approximately one in three orders ended with negative net profit. This showed why I should not rely on total sales or total profit alone when reviewing performance.

Clothing, Electronics and Furniture all generated positive category-level profit. At sub-category level, Furnishings and Electronic Games recorded negative net profit. Rajasthan and Andhra Pradesh also had small negative state-level totals. These are investigation signals, not proof of the underlying cause.

## 5. Analysis and dashboard

I used Power BI, Power Query and DAX to prepare the data model, define performance measures and build interactive views. The dashboard allows a reviewer to explore sales and profitability across categories, sub-categories, regions, months and payment methods.

I kept order-level loss analysis separate from detail-row analysis so the KPI reflects the business question accurately.

## 6. Business interpretation and recommendations

Based on the results, I would recommend that the business:

1. Review the 169 loss-making orders to identify recurring product combinations or transaction patterns.
2. Investigate negative-profit sub-categories before making pricing or assortment changes.
3. Review the small negative regional totals at order level rather than assuming an entire region is underperforming.
4. Add discount, product-cost, shipping and return information to understand why losses occur.
5. Track loss-making order rate and profit margin alongside revenue in regular reporting.

These recommendations identify where further analysis may be useful. The available fields do not prove that discounts, shipping, payment method or any other factor caused the losses.

## 7. Limitations

The dataset does not include a complete breakdown of product costs, discounts, shipping charges, returns, advertising spend or customer acquisition cost. As a result, the analysis identifies negative-profit patterns in the supplied data but cannot fully explain the operational drivers behind them.

The validation script recalculates the headline metrics from the CSV files. The internal Power BI model and every DAX measure still need to be inspected in Power BI Desktop before the dashboard can be considered independently audited.

## 8. What I would do next

I would add detailed cost and discount data, investigate the largest loss-making orders, and build an order-level drill-through page. I would also compare customer segments and repeat-purchase behaviour to understand whether profitability differs across customer groups.

## 9. Conclusion

This project helped me practise turning transactional data into a business-focused profitability review. The key lesson was that a positive overall profit figure can hide a meaningful number of loss-making orders. By separating order-level and product-level calculations, I could make the analysis more useful and communicate more precise follow-up questions.

---

*This is an independent portfolio analysis. The findings describe the supplied dataset and should not be interpreted as proof of the causes of profit leakage.*