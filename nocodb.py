import requests
import sys
import json
from datetime import datetime
import pandas as pd

# Define the NocoDB URL components
hosturl = "http://10.1.0.170:8080"
port = 8080
api_token = "jkjlH0Jk_3i_p4h5W5tZ7pCtx8RtJv9I76kCNRvR"


def getTableEntries(tableId, viewID=None):
    url = f"{hosturl}/api/v2/tables/{tableId}/records"

    querystring = {
        "viewId": viewID,
    }

    headers = {"xc-token": api_token}

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


def createTableRow(tableId, data):
    url = f"{hosturl}/api/v2/tables/{tableId}/records"

    headers = {"xc-token": api_token}

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        print("Record created successfully.")


def createLink(tableId, linkFieldId, linkRowId, recordRowId):
    url = f"{hosturl}/api/v2/tables/{tableId}/links/{linkFieldId}/records/{linkRowId}"
    """Create a link in row {linkRowId} to {recordRowId}"""
    payload = {
        "Id": recordRowId,
    }

    headers = {"xc-token": api_token}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Record created successfully.")


def filterEntriesByMonth(tableId, month):
    data = json.loads(getTableEntries(tableId))
    july_entries = []
    for entry in data["list"]:
        date_str = entry["Date"]
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj.month == month:  # Check if the month is July
            july_entries.append(entry)
    return july_entries


def idsByMonth(tableId, month):
    data = json.loads(getTableEntries(tableId))

    july_entry_ids = []
    for entry in data["list"]:
        date_str = entry["Date"]
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj.month == month:  # Check the month
            july_entry_ids.append(entry["Id"])
    return july_entry_ids


# Load the JSON data from the file
# data = getTableEntries("mcu569c5t3pofvv")

# print(json.dumps(filterEntriesByMonth("mcu569c5t3pofvv", 7)))
# todo = filterEntriesByMonth("mcu569c5t3pofvv", 6)

# df = pd.DataFrame(todo, columns=["Date", "Hours", "Tag", "Description"])

# Display the DataFrame
# print(df)

# for i in todo:
#     createLink("m4k483bsn6sv35z", "crbfkuxfc1zxjxo", 2, i)

# Function to filter IDs of entries with "Date" in July

# data = {"Title": "Buy milk", "Done": True}

# createTableRow("m7wh22a5nh2n1cl", data)

# createLink("m3r09axnajlhb92", "crm80xjvhq0482n", 1, 3)
