"""Touch Business Insights: CSV sales analytics, standard library only."""
import argparse
import csv
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path


def analyze(path):
    """Return summary for a CSV with date,product,quantity,unit_price,unit_cost."""
    total_revenue = Decimal("0")
    total_cost = Decimal("0")
    units = 0
    orders = 0
    products = defaultdict(lambda: {"units": 0, "revenue": Decimal("0")})
    daily = defaultdict(lambda: Decimal("0"))
    with open(path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = {"date", "product", "quantity", "unit_price", "unit_cost"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("CSV needs columns: " + ", ".join(sorted(required)))
        for line, row in enumerate(reader, start=2):
            try:
                day = datetime.strptime(row["date"].strip(), "%Y-%m-%d").date().isoformat()
                name = row["product"].strip()
                quantity = int(row["quantity"])
                price = Decimal(row["unit_price"])
                cost = Decimal(row["unit_cost"])
                if not name or quantity <= 0 or price < 0 or cost < 0:
                    raise ValueError("invalid product, quantity, or price")
                if not price.is_finite() or not cost.is_finite():
                    raise ValueError("non-finite price")
            except (ValueError, TypeError, InvalidOperation, AttributeError) as exc:
                raise ValueError(f"Invalid CSV row {line}: {exc}") from exc
            revenue = quantity * price
            total_revenue += revenue
            total_cost += quantity * cost
            units += quantity
            orders += 1
            products[name]["units"] += quantity
            products[name]["revenue"] += revenue
            daily[day] += revenue
    return {"orders": orders, "units": units, "revenue": total_revenue,
            "cost": total_cost, "profit": total_revenue - total_cost,
            "products": dict(products), "daily": dict(daily)}


def report(data, currency="TZS"):
    lines = [
        "TOUCH BUSINESS INSIGHTS | SALES REPORT",
        "=" * 42,
        f"Transactions: {data['orders']}",
        f"Units sold:   {data['units']}",
        f"Revenue:      {currency} {data['revenue']:,.2f}",
        f"Gross profit: {currency} {data['profit']:,.2f}",
        "",
        "TOP PRODUCTS (BY REVENUE)",
    ]
    ranked = sorted(data["products"].items(),
                    key=lambda item: (-item[1]["revenue"], item[0]))
    for name, stats in ranked[:5]:
        lines.append(f"- {name}: {stats['units']} units | {currency} {stats['revenue']:,.2f}")
    lines.extend(["", "DAILY REVENUE"])
    for day, amount in sorted(data["daily"].items()):
        lines.append(f"- {day}: {currency} {amount:,.2f}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Sales CSV insights for small businesses")
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--currency", default="TZS")
    args = parser.parse_args()
    try:
        print(report(analyze(args.csv_file), args.currency))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
