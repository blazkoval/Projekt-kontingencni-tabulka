import json
from datetime import datetime
import copy
import pandas as pd

def transform_events(data):
    transformed_events = []
    
    for event in data["data"]["eventPage"]:
        event_type = event.pop("eventType")  # Odstranění původního eventType
        event["eventtype_id"] = event_type["id"]  # Přidání nového klíče eventtype_id
        event["eventtype_name"] = event_type["name"]  # Přidání nového klíče eventtype_name

        start_date = datetime.fromisoformat(event["startdate"])
        end_date = datetime.fromisoformat(event["enddate"])
        duration = end_date - start_date
        event["duration"] = duration.total_seconds() / 60  # Převod na minuty

        # Odstranění původních atributů "startdate" a "enddate"
        del event["startdate"]
        del event["enddate"]

        for group in event["groups"]:
            event_copy = copy.deepcopy(event)
            event_copy["group_id"] = group["id"]
            event_copy["group_name"] = group["name"]
            transformed_events.append(event_copy)

    for event in transformed_events:
        if "groups" in event:
            del event["groups"]

    return transformed_events

f = "data.json"
with open(f, 'r', encoding='utf-8') as file:
    data_json = json.load(file)

# Transformace dat
transformed_data = transform_events(data_json)

with open('transformed.json', 'w', encoding='utf-8') as outfile:
    json.dump(transformed_data, outfile, indent=4, ensure_ascii=False)

df = pd.DataFrame(transformed_data)
df.to_excel('transformed.xlsx', index=False)