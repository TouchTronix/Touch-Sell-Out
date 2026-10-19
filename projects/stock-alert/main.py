import csv
import argparse

def low_stock(path):
    alerts = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sku = row["sku"].strip()
            stock = int(row["stock"])
            minimum = int(row["minimum"])
            if stock < 0 or minimum < 0:
                raise ValueError("Stock and minimum cannot be negative")
            if stock <= minimum:
                alerts.append((sku, stock, minimum))
    return alerts

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("csv_file")
    a = p.parse_args()
    for sku, stock, minimum in low_stock(a.csv_file):
        print(f"RESTOCK: {sku} | left: {stock} | minimum: {minimum}")
