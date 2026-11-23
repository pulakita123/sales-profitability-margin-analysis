#!/usr/bin/env python3
"""Validate the portfolio project's source CSV files and recalculate headline KPIs.

Run from the repository root:
    python scripts/validate_data.py

Uses only the Python standard library.
"""
from __future__ import annotations

import csv
from collections import defaultdict
from datetime import datetime
from decimal import Decimal
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DETAILS_PATH = ROOT / "Details.csv"
ORDERS_PATH = ROOT / "Orders.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path.name}")
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def money(value: Decimal) -> str:
    return f"₹{value:,.2f}"


def main() -> int:
    details = read_csv(DETAILS_PATH)
    orders = read_csv(ORDERS_PATH)

    required_details = {
        "Order ID", "Amount", "Profit", "Quantity",
        "Category", "Sub-Category", "PaymentMode",
    }
    required_orders = {"Order ID", "Order Date", "CustomerName", "State", "City"}

    if not details or not orders:
        raise ValueError("One or both CSV files contain no data rows.")

    missing_detail_columns = required_details - set(details[0])
    missing_order_columns = required_orders - set(orders[0])
    if missing_detail_columns or missing_order_columns:
        raise ValueError(
            f"Missing columns. Details: {sorted(missing_detail_columns)}; "
            f"Orders: {sorted(missing_order_columns)}"
        )

    blank_details = sum(
        1 for row in details for column in required_details
        if not (row.get(column) or "").strip()
    )
    blank_orders = sum(
        1 for row in orders for column in required_orders
        if not (row.get(column) or "").strip()
    )

    detail_order_ids = {row["Order ID"].strip() for row in details}
    order_ids = [row["Order ID"].strip() for row in orders]
    unique_order_ids = set(order_ids)
    duplicate_order_ids = len(order_ids) - len(unique_order_ids)
    unmatched_detail_ids = detail_order_ids - unique_order_ids
    unmatched_order_ids = unique_order_ids - detail_order_ids

    order_profit: dict[str, Decimal] = defaultdict(Decimal)
    total_sales = Decimal("0")
    total_profit = Decimal("0")
    detail_negative_rows = 0
    parsed_dates = []

    for row in details:
        order_id = row["Order ID"].strip()
        amount = Decimal(row["Amount"])
        profit = Decimal(row["Profit"])
        total_sales += amount
        total_profit += profit
        order_profit[order_id] += profit
        if profit < 0:
            detail_negative_rows += 1

    for row in orders:
        parsed_dates.append(datetime.strptime(row["Order Date"].strip(), "%d-%m-%Y").date())

    loss_orders = {order_id: profit for order_id, profit in order_profit.items() if profit < 0}
    loss_amount = -sum(loss_orders.values(), Decimal("0"))
    total_orders = len(unique_order_ids)
    margin = total_profit / total_sales if total_sales else Decimal("0")
    aov = total_sales / total_orders if total_orders else Decimal("0")

    print("DATA QUALITY")
    print(f"  Details rows: {len(details):,}")
    print(f"  Orders rows: {len(orders):,}")
    print(f"  Blank required cells - Details: {blank_details}; Orders: {blank_orders}")
    print(f"  Duplicate Order IDs in Orders.csv: {duplicate_order_ids}")
    print(f"  Unmatched IDs - Details to Orders: {len(unmatched_detail_ids)}")
    print(f"  Unmatched IDs - Orders to Details: {len(unmatched_order_ids)}")
    print(f"  Date range: {min(parsed_dates)} to {max(parsed_dates)}")
    print("  Note: trim text fields such as State in Power Query; source includes 'Kerala '.")

    print("\nRECALCULATED KPIs")
    print(f"  Distinct orders: {total_orders:,}")
    print(f"  Detail rows: {len(details):,}")
    print(f"  Sales: {money(total_sales)}")
    print(f"  Net profit: {money(total_profit)}")
    print(f"  Profit margin: {margin:.2%}")
    print(f"  Average order value: {money(aov)}")
    print(f"  Negative-profit detail rows: {detail_negative_rows:,}")
    print(f"  Loss-making orders (net order profit < 0): {len(loss_orders):,}")
    print(f"  Net loss across loss-making orders: {money(loss_amount)}")

    problems = []
    if blank_details or blank_orders:
        problems.append("blank required cells were found")
    if duplicate_order_ids:
        problems.append("duplicate order IDs were found in Orders.csv")
    if unmatched_detail_ids or unmatched_order_ids:
        problems.append("the two files contain unmatched order IDs")
    if len(order_profit) != total_orders:
        problems.append("order-level profit aggregation does not match distinct order count")

    if problems:
        print("\nVALIDATION: REVIEW REQUIRED")
        for problem in problems:
            print(f"  - {problem}")
        return 1

    print("\nVALIDATION: PASSED (review the text-normalisation note above)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # show a useful message when run by a reviewer
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
