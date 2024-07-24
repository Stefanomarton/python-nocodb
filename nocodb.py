import requests
import json
from datetime import datetime


class NocoDB:
    def __init__(self, hosturl: str, port: int, api_token: str):
        self.hosturl = hosturl
        self.port = port
        self.api_token = api_token
        self.headers = {"xc-token": api_token}
        self.baseUrl = f"{self.hosturl}/api/v2"

    def getTableEntries(self, tableId: str, viewID: str = "") -> str:
        """
        Get entries for table with {tableId}, optionally use a view with {viewID}
        """
        url = f"{self.baseUrl}/tables/{tableId}/records"

        querystring = {
            "viewId": viewID,
        }

        headers = {"xc-token": self.api_token}

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.text

    def createTableRow(self, tableId: str, data: dict[str, str]):
        """
        Create entry for table with {tableId}
        """
        url = f"{self.baseUrl}/tables/{tableId}/records"

        headers = {"xc-token": self.api_token}

        response = requests.post(url, data=data, headers=headers)

        if response.status_code == 200:
            return "New Row created successfully."
        else:
            return response.raise_for_status()

    def createLink(
        self, tableId: str, linkFieldId: str, linkRowId: int, recordRowId: int
    ):
        """Create a link in row {linkRowId} to {recordRowId}"""

        url = f"{self.baseUrl}/tables/{tableId}/links/{linkFieldId}/records/{linkRowId}"

        payload = {
            "Id": recordRowId,
        }

        headers = {"xc-token": self.api_token}

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return "Link created successfully."
        else:
            return response.raise_for_status()
