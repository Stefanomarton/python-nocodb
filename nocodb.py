import requests

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


print(getTableEntries("mcu569c5t3pofvv"))

# data = {"Title": "Buy milk", "Done": True}

# createTableRow("m7wh22a5nh2n1cl", data)

# createLink("m3r09axnajlhb92", "crm80xjvhq0482n", 1, 3)
