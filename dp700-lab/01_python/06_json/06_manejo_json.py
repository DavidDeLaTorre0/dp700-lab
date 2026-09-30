import json
clean = [
{"order_id": "A-1", "amount": 25.5, "country": "ES"},
{"order_id": "A-2", "amount": 40.0, "country": "PT"},
]
rejected = [
{"order_id": "A-3", "amount": -5.0, "country": "ES"}
]
with open("clean.json", "w", encoding="utf-8") as f:
    json.dump(clean, f, indent=2, ensure_ascii=False)
with open("rejected.json", "w", encoding="utf-8") as f:
    json.dump(rejected, f, indent=2, ensure_ascii=False)
with open("clean.json", "r", encoding="utf-8") as f:
    clean_again = json.load(f)
with open("rejected.json", "r", encoding="utf-8") as f:
    rejected_again = json.load(f)
    
print("Válidas:", len(clean_again))
print("Rechazadas:", len(rejected_again))
