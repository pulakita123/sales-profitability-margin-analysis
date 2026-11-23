# Key Findings & Business Interpretation

The figures in this document were recalculated from the CSV files currently stored in this repository.

## 1. Overall performance

| Metric | Result |
|---|---:|
| Distinct orders | 500 |
| Detail records | 1,500 |
| Sales | ₹4,37,771 |
| Net profit | ₹36,963 |
| Profit margin | 8.44% |
| Average order value | ₹875.54 |
| Loss-making orders | 169 |
| Loss-making order rate | 33.8% |
| Combined net loss across loss-making orders | ₹26,127 |

### What this means

The business is profitable overall, but the overall result hides a sizeable group of orders that ended with negative net profit. Around one-third of the orders were loss-making, so total profit alone does not provide a complete picture of performance.

## 2. Category performance

| Category | Net profit |
|---|---:|
| Clothing | ₹13,325 |
| Electronics | ₹13,162 |
| Furniture | ₹10,476 |

### What this means

The three categories generated positive net profit, with relatively close results. Electronics should not be described as having a ₹13.2K net loss—the recalculated category total is a positive ₹13,162. The better question is which products and individual orders within each category are reducing the overall result.

## 3. Sub-category performance

| Sub-category | Net profit |
|---|---:|
| Furnishings | -₹806 |
| Electronic Games | -₹644 |
| Kurti | -₹401 |
| Skirt | -₹315 |
| Leggings | -₹130 |
| Printers | ₹8,606 |
| Bookcases | ₹6,516 |

### What this means

Furnishings and Electronic Games are the weakest sub-categories by net profit in this dataset. Printers and Bookcases are among the strongest. These results are useful starting points for a deeper review of pricing, product cost, discounting and order composition.

## 4. Regional performance

| State | Net profit |
|---|---:|
| Rajasthan | -₹323 |
| Andhra Pradesh | -₹280 |
| Madhya Pradesh | ₹7,382 |
| Maharashtra | ₹6,963 |

### What this means

Rajasthan and Andhra Pradesh are the two states with negative total profit in the supplied data. Their losses are relatively small, so they should be treated as signals for further investigation rather than proof of a broad regional problem.

## 5. Payment method comparison

| Payment method | Net profit |
|---|---:|
| Credit Card | ₹12,612 |
| COD | ₹12,547 |
| UPI | ₹3,286 |
| Debit Card | ₹3,694 |
| EMI | ₹4,824 |

### What this means

Credit Card and COD transactions have the highest total profit in this dataset. This is a descriptive comparison; the available data does not show that payment method causes profitability differences. A fairer comparison could also examine order counts, average order value and profit margin for each payment method.

## 6. Recommended business follow-up

1. Review the 169 loss-making orders and identify the product combinations that contribute most to their negative net profit.
2. Investigate Furnishings and Electronic Games, while comparing their order volumes and sales values with their profit.
3. Review the small negative totals in Rajasthan and Andhra Pradesh at the individual order level.
4. Add discount, cost, shipping and return fields before recommending pricing or fulfilment changes.
5. Monitor loss-making order rate and profit margin alongside sales in regular performance reviews.

## Important calculation distinction

There are 529 detail rows with negative Profit values, but only 169 orders have negative net profit after all their detail rows are added together. These numbers answer different questions. The dashboard's loss-making-order KPI should use the order-level calculation.
