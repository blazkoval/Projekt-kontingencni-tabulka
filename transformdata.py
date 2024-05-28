# cd D:\projekt-kont-tabulka\Projekt-kontingencni-tabulka\
# py transformData.py

import json
from datetime import datetime
import copy
import pandas as pd
from collections import defaultdict


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

def aggregate_events(events):
    aggregated_data = defaultdict(lambda: defaultdict(lambda: {"total_duration": 0.0}))

    for event in events:
        group_name = event["group_name"]
        name = event["eventtype_name"]
        duration = event["duration"]
        
        aggregated_data[group_name][name]["total_duration"] += duration
    
    # Konverze na list dict pro výstup
    output_data = []
    for group_name, events in aggregated_data.items():
        for name, details in events.items():
            output_data.append({
                "group_name": group_name,
                "eventtype_name": name,
                "total_duration": details["total_duration"]
            })
    
    return output_data

f = "data.json"
with open(f, 'r', encoding='utf-8') as file:
    data_json = json.load(file)


transformed_data = transform_events(data_json)
aggregated_data = aggregate_events(transformed_data)

## ====== transformovana data do JSONu a excelu ==========
with open('transformed.json', 'w', encoding='utf-8') as outfile:
     json.dump(transformed_data, outfile, indent=4, ensure_ascii=False)

df = pd.DataFrame(transformed_data)
df.to_excel('tranformed.xlsx', index=False)

# ====== agregovana data do JSONu a excelu ==============
# with open('aggregated.json', 'w', encoding='utf-8') as outfile:
#     json.dump(aggregated_data, outfile, indent=4, ensure_ascii=False)

# df = pd.DataFrame(aggregated_data)
# df.to_excel('aggregated.xlsx', index=False)