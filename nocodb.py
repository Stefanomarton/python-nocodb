import requests
import json
from datetime import datetime

# Define the NocoDB URL components
hosturl = "http://10.1.0.170:8080"
port = 8080
api_token = "jkjlH0Jk_3i_p4h5W5tZ7pCtx8RtJv9I76kCNRvR"


def getTableEntries(tableId: str, viewID: str = "") -> str:
    """
    Get entries for table with {tableId}, optionally use a view with {viewID}
    """
    url = f"{hosturl}/api/v2/tables/{tableId}/records"

    querystring = {
        "viewId": viewID,
    }

    headers = {"xc-token": api_token}

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


def createTableRow(tableId: str, data: dict[str, str]):
    """
    Create entry for table with {tableId}
    """
    url = f"{hosturl}/api/v2/tables/{tableId}/records"

    headers = {"xc-token": api_token}

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        return "New Row created successfully."
    else:
        return response.raise_for_status()


def createLink(tableId: str, linkFieldId: str, linkRowId: int, recordRowId: int):
    """Create a link in row {linkRowId} to {recordRowId}"""

    url = f"{hosturl}/api/v2/tables/{tableId}/links/{linkFieldId}/records/{linkRowId}"

    payload = {
        "Id": recordRowId,
    }

    headers = {"xc-token": api_token}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return "Link created successfully."
    else:
        return response.raise_for_status()


def filterEntriesByMonth(tableId: str, month: int) -> list:
    """
    Return entry in table in with date in {month}
    """
    data = json.loads(getTableEntries(tableId))
    july_entries = []
    for entry in data["list"]:
        date_str = entry["Date"]
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj.month == month:  # Check if the month is July
            july_entries.append(entry)
    return july_entries


def idsByMonth(tableId: str, month: int) -> list:
    """
    Return IDs of entry in table in {month}

    Parameters:
    tableId (str): Table ID
    Month (int): Month to filter
    """
    data = json.loads(getTableEntries(tableId))

    july_entry_ids = []
    for entry in data["list"]:
        date_str = entry["Date"]
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj.month == month:  # Check the month
            july_entry_ids.append(entry["Id"])
    return july_entry_ids
