# Business Problem

## Background

An e-commerce business can report strong sales and still have profitability issues. Revenue tells us how much value was sold, but it does not tell us whether each order contributed positively to the business.

For this project, I used order and product-detail data to investigate profitability across categories, sub-categories, locations, dates and payment methods.

## Problem statement

The business needs a clearer view of where profit is being generated and where it may be leaking through loss-making orders or weaker product and regional performance.

The analysis is intended to help a sales or operations team prioritise areas for investigation. It is not intended to identify a root cause that the available data cannot prove.

## Business questions

1. What are total sales, total profit, profit margin and average order value?
2. How many orders have negative net profit?
3. What is the combined negative profit of those loss-making orders?
4. Which product categories and sub-categories have the weakest net profitability?
5. Which states are recording negative net profit?
6. How do sales and profit change over time?
7. How do the results differ across payment methods?

## Intended users

- Sales managers monitoring revenue and product performance
- Category managers reviewing product mix
- Operations teams investigating loss-making orders
- Business analysts preparing performance reviews

## Decisions the analysis can support

The dashboard can help a team decide which products, sub-categories, regions or orders deserve a closer review. It can also help establish a regular profitability-monitoring process.

Before changing prices, discounts or payment policies, the business would need more information—especially product costs, discount amounts, shipping charges and return data.

## Scope

**Included:** order-level sales and dates, product/category details, profit, quantity, state/city and payment mode.

**Not included:** cost breakdowns, discount reasons, shipping costs, returns, advertising costs, customer acquisition cost or a causal analysis of payment behaviour.

## Success criteria

The project is successful if a reviewer can:
- understand the business question quickly;
- trace the headline KPIs to the included data;
- distinguish a loss-making product row from a loss-making order;
- identify the main areas flagged by the analysis; and
- understand what additional data would be required before acting on the findings.
