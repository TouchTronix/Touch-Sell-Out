# Touch Business Insights 📊

A lightweight Python sales analytics mini-project for phone accessories and electronics businesses. Uses only the Python standard library; no accounts, API keys, or external dependencies.

## Run

From the repository root:

```bash
python projects/touch-business-insights/insights.py projects/touch-business-insights/sample_sales.csv
```

The report displays total sales revenue, estimated gross profit (revenue minus item costs, **not** net profit), units sold, best-selling products by revenue, and daily sales totals. Amounts are displayed in TZS by default.

## Input format

CSV headers: `date,product,quantity,unit_price,unit_cost`.

- Dates use `YYYY-MM-DD`.
- Quantity is a positive whole number.
- Prices and costs must be non-negative numbers.
- Each row represents a product line, not necessarily a unique customer order.
- Use fictional/demo data when sharing screenshots publicly.

## Test

```bash
cd projects/touch-business-insights
python -m unittest -v
```

## Future ideas

Import POS exports, add profit trends, stock alerts, visual dashboards, and CSV exports. This is a demo analytics tool, not a complete POS system.
