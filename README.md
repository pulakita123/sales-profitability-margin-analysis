# E-Commerce Sales & Profit Leakage Analysis | Power BI

## Project Overview

Developed an interactive **Power BI business intelligence dashboard** to analyze e-commerce sales, profitability, loss-making orders, and sources of profit leakage across products, categories, sub-categories, states, payment modes, and time.

The project analyzes **500 e-commerce orders** generating approximately **₹4.38L in sales** and uses DAX-driven KPIs and interactive visualizations to identify areas of negative profitability and support data-driven business decisions.

---

## Business Objective

The primary objective was to move beyond basic sales reporting and investigate:

- Where is profit being lost?
- Which products and sub-categories contribute to negative profitability?
- Which states have weaker profit performance?
- How does profitability change over time?
- Which categories contribute most to overall profit leakage?
- How can loss-making orders be identified and monitored?

---

## Key Business Metrics

| KPI | Value |
|---|---:|
| Total Sales | ₹4.38L |
| Total Profit | ₹36.96K |
| Total Orders | 500 |
| Loss-Making Orders | 169 |
| Profit Leakage / Loss Amount | ₹26.12K |
| Overall Profit Margin | 8.44% |

<img width="1071" height="607" alt="image" src="https://github.com/user-attachments/assets/f6002bf2-fcf6-45ce-b855-c942284c9af0" />

<img width="1054" height="591" alt="image" src="https://github.com/user-attachments/assets/9894f779-77f3-4fcb-80b4-ad032827c02b" />

## Key Insights

### Profit Leakage

- Identified approximately **₹26K in profit leakage across 169 loss-making orders**.
- Loss-making orders represent a significant portion of the analyzed order base, highlighting the need for profitability monitoring rather than relying solely on sales volume.

### Category Performance

- **Electronics** recorded the highest loss amount among the analyzed categories at approximately **₹13.2K**.
- Clothing and Furniture also contributed to overall profit leakage.
- Category-level analysis helps identify where margin improvement initiatives should be prioritized.

### Sub-Category Performance

- **Electronic Games** generated negative profit, indicating a loss-making product segment.
- **Furnishings** also showed negative profitability.
- High-performing sub-categories such as **Printers and Bookcases** contributed substantially to overall profit.

### Regional Performance

- State-level analysis revealed significant differences in profitability.
- **Rajasthan and Andhra Pradesh** recorded negative total profit in the analyzed dataset.
- Maharashtra and Madhya Pradesh generated comparatively stronger absolute profit.

### Time-Based Analysis

- Monthly profit analysis revealed significant fluctuations throughout the year.
- Several months recorded negative profit, highlighting the importance of monitoring profitability trends over time.

---

## Technical Skills Demonstrated

### Power BI
- Interactive dashboard development
- KPI and performance reporting
- Slicers and interactive filtering
- Cross-filtering between visuals
- Time-series analysis
- Category and regional analysis
- Business-focused data visualization

### DAX
Created calculated measures for:

- Profit Margin
- Average Order Value (AOV)
- Total Profit
- Total Sales
- Loss Amount
- Loss-Making Orders
- Loss Order Rate
- Profit per Order

### Data Modeling
- Designed a structured relational data model
- Created a dedicated **Date table** for time intelligence
- Created a dedicated **Measures table** for centralized DAX calculations
- Established relationships to support dynamic filtering and analysis

### Data Analysis
- Exploratory Data Analysis
- Profitability analysis
- Variance and trend analysis
- Loss-making order analysis
- Category and sub-category performance analysis
- State-level performance analysis
- Payment-mode analysis
- Business KPI development

---

## Dashboard Features

The Power BI dashboard provides interactive analysis of:

### Sales & Profitability
- Total Sales
- Total Profit
- Profit Margin
- Average Order Value
- Total Orders

### Profit Leakage
- Loss Amount
- Loss-Making Orders
- Top Sources of Profit Leakage
- Loss-making sub-categories

### Product Analysis
- Category performance
- Sub-category performance
- Sales vs. Profitability

### Geographic Analysis
- State-wise Sales
- State-wise Profit
- Loss-making regions

### Time Analysis
- Monthly Profit Trend
- Monthly performance comparison
- Quarterly filtering

### Payment Analysis
- COD
- Credit Card
- Debit Card
- EMI
- UPI

---

## 📷 Dashboard Preview

### Profit Leakage Investigation

![Profit Leakage Investigation](profit-leakage-investigation.png)

### E-Commerce Sales Dashboard

![E-Commerce Sales Dashboard](ecommerce-sales-dashboard.png)

---

## Tools & Technologies

- **Microsoft Power BI**
- **DAX**
- **Power Query**
- **Data Modeling**
- **Microsoft Excel**

---

## Business Impact

This analysis demonstrates how Power BI can be used to transform transactional e-commerce data into actionable business insights.

The dashboard enables stakeholders to:

- Identify products and categories contributing to profit leakage
- Monitor loss-making orders
- Compare profitability across regions
- Analyze monthly profit trends
- Evaluate payment-mode performance
- Prioritize opportunities for margin improvement

---

## Project Structure

ecommerce-sales-profit-leakage-analysis/
│
├── README.md
├──Ecommerce_Sales_Profit_Leakage.pbix
├── profit-leakage-investigation.png
└── ecommerce-sales-dashboard.png
