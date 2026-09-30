def validate(row):
    if not row.get("order_id"):
        return False
    if row.get("amount") is None:
        return False
    if row["amount"] < 0:
        return False
    return True
sales = [
{"order_id": "A-1", "country": "ES", "amount": 25.5},
{"order_id": "A-2", "country": "USA", "amount": 80.0},
{"order_id": "A-3", "country": "LIT", "amount": 30.0},
{"order_id": "A-4", "country": "EST", "amount": 76.0},
{"order_id": "A-5", "country": "FR", "amount": 27.0},
{"order_id": "A-6", "country": "SP", "amount": -5.0},
{"order_id": "", "country": "FR", "amount": 27.0},
{"order_id": "A-8", "country": "POR", "amount": None},
{"order_id": "A-9", "country": "ALE", "amount": -1},
]
#validar

for row in sales:
    if validate(row)==True:
        print(f"FILA VALIDA: {row}")
    else:
        None
        
        