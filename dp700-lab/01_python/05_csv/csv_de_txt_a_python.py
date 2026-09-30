import csv
from pathlib import Path

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
        if row["amount"] != "":
            row["amount"] = float(row["amount"])
        else:
            row["amount"] = None

        if validate(row) == True:
            rows.append(row)
        else:
            print(f"No se guarda {row}")            
    print(rows)
    
    
    