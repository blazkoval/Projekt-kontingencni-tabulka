import json
# "D:\projekt-kont-tabulka\Projekt-kontingencni-tabulka\Projekt-kontingencni-tabulka\data.json"
f = "data.json"
with open(f, 'r', encoding='utf-8') as file:
    data_json = json.load(file)

# Přetransformování dat
events = data_json["data"]["eventPage"]
for event in events:
    event_type = event.pop("eventType")  # Odstranění původního eventType
    event["eventtype_id"] = event_type["id"]  # Přidání nového klíče eventtype_id
    event["eventtype_name"] = event_type["name"]  # Přidání nového klíče eventtype_name

with open('transformed.json', 'w', encoding='utf-8') as outfile:
    json.dump(data_json, outfile, indent=4, ensure_ascii=False)