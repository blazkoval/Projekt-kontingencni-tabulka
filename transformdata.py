import json
from datetime import datetime

f = "data.json"
with open(f, 'r', encoding='utf-8') as file:
    data_json = json.load(file)

# Přetransformování dat
events = data_json["data"]["eventPage"]

# zabalit do funkce, aby byla pure, udelat kopii event, aby se nemodifikoval vstup
for event in events:
    event_type = event.pop("eventType")  # Odstranění původního eventType
    event["eventtype_id"] = event_type["id"]  # Přidání nového klíče eventtype_id
    event["eventtype_name"] = event_type["name"]  # Přidání nového klíče eventtype_name

    start_date = datetime.fromisoformat(event["startdate"])
    end_date = datetime.fromisoformat(event["enddate"])
    duration = end_date - start_date
    event["duration"] = str(duration) #bez str - nejde s tim pracovat

    # Odstranění původních atributů "startdate" a "enddate"
    del event["startdate"]
    del event["enddate"]

with open('transformed.json', 'w', encoding='utf-8') as outfile:
    json.dump(data_json, outfile, indent=4, ensure_ascii=False)