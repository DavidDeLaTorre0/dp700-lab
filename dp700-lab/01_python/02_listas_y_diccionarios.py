#un diccionario es una forma natural de representar una fila. Una lista de diccionarios representa varias filas.
#   sale = {"order_id": "A-1", "country": "ES", "amount": 25.5}
#   sales = [
#   sale,
#   {"order_id": "A-2", "country": "PT", "amount": 40.0}
#   ]
#   print(sale["amount"])
#   print(sales[1]["country"])
#sales[1] obtiene el segundo elemento de la lista. Luego ["country"] obtiene el campo country de ese diccionario.

print("3" * 2)
print(int("3") * 2)


sales = [
{"order_id": "A-1", "country": "ES", "amount": 25.5},
{"order_id": "A-2", "country": "USA", "amount": 80.0},
{"order_id": "A-3", "country": "LIT", "amount": 30.0},
{"order_id": "A-4", "country": "EST", "amount": 76.0},
{"order_id": "A-5", "country": "FR", "amount": 27.0},
{"order_id": "A-6", "country": "SP", "amount": -5.0}
]

sum = 0
sumES = 0

for row in sales:
    if row["country"] == "ES":
        sumES += row["amount"]

print(f"suma total ES: {sumES}")

# Solo los de ES
for row in sales:
    #sumar amount en total
    sum += row["amount"]

print(f"suma total: {sum}")



## if/for reglas de calidad
rejected = []
clean = []

for row in sales:
    if row['amount']<0:
        rejected.append(row)
    else:
        clean.append(row)

print(len(clean))
print(len(rejected))


