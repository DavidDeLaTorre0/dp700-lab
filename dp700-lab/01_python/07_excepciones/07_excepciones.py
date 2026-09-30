import csv
from pathlib import Path


def parse_amount(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def validate(row):
    if not row.get("order_id"):
        return False

    if row.get("amount") is None:
        return False

    if row["amount"] < 0:
        return False

    return True


archivo_actual = Path(__file__).parent
ruta_csv = archivo_actual / "sales.csv"

rows = []

with open(ruta_csv, encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:

        print(f"Leyendo línea: {row}")

        row["amount"] = parse_amount(row["amount"])

        if validate(row):
            rows.append(row)
        else:
            print(f"No se guarda: {row}")


print("\nFilas válidas:")
print(rows)
# ---------------------------------------------------------------------- 
print(parse_amount("10"))
print(parse_amount("10.5"))
print(parse_amount(""))
print(parse_amount(None))
print(parse_amount("abc"))