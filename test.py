from nocodb import NocoDB
import json
from dataclasses import dataclass
from typing import List, Optional

from datetime import datetime as dt


# Define the NocoDB URL components
hosturl = "http://10.1.0.170:8080"
port = 8080
api_token = "jkjlH0Jk_3i_p4h5W5tZ7pCtx8RtJv9I76kCNRvR"


@dataclass
class Report:
    Id: int
    Title: str


@dataclass
class Record:
    Id: int
    Date: dt
    CreatedAt: str
    UpdatedAt: str
    Hours: float
    nc_c4dl___Report_id: Optional[int]
    Tag: str
    Description: Optional[str]
    Report: Optional[Report]

    @staticmethod
    def from_dict(data):
        return Record(
            Id=data["Id"],
            Date=dt.strptime(data["Date"], "%Y-%m-%d"),
            CreatedAt=(data["CreatedAt"]),
            UpdatedAt=(data["UpdatedAt"]),
            Hours=data["Hours"],
            nc_c4dl___Report_id=data.get("nc_c4dl___Report_id"),
            Tag=data["Tag"],
            Description=data.get("Description"),
            Report=Report(**data["Report"]) if data.get("Report") else None,
        )


@dataclass
class PageInfo:
    totalRows: int
    page: int
    pageSize: int
    isFirstPage: bool
    isLastPage: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
class Root:
    list: List[Record]
    pageInfo: PageInfo

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)

        records = [Record(**record) for record in data["list"]]

        page_info = PageInfo(**data["pageInfo"])

        return cls(list=records, pageInfo=page_info)


# client = NocoDB(hosturl, port, api_token)

# # Fetch table entries
# entries = client.getTableEntries(
#     "mcu569c5t3pofvv",
# )

# print(entries)

# Deserialize JSON data into the Root object

# root = Root.from_json(entries)

# print(root.list)

# filter by tag
# for record in root.list:
#     if record.Tag == "ECOCHIMICA":
#         print(record)

#     def filterEntriesByMonth(self, tableId: str, month: int) -> list:
# """Return entry in table in with date in {month}."""
# data = json.loads(self.getTableEntries(tableId))
# july_entries = []
# for entry in data["list"]:
#     date_str = entry["Date"]
#     date_obj = datetime.strptime(date_str, "%Y-%m-%d")
#     if date_obj.month == month:  # Check if the month is July
#         july_entries.append(entry)
# return july_entries

for record in root.list:
    print(record.Date.month)

    # filter by date
# for record in root.list:
#     if record.Date.month == 7:
#         print(record)
# records = [Record.from_dict(record) for record in root.list]

# test = [record for record in records if record.Id == 1]

# print(test)

# print(records[1].Id)

# test = []
# for record in records:
#     if record.Id == 1:
#         test.append(record)


# # Print each record in root.list
# for record in root.list:
#     print(record)

# # Print the Id of each record
# for record in root.list:
#     print(record.Id)


# Load the JSON data from the file
# data = getTableEntries("mcu569c5t3pofvv")

# print(json.dumps(filterEntriesByMonth("mcu569c5t3pofvv", 7)))
# todo = filterEntriesByMonth("mcu569c5t3pofvv", 6)

# df = pd.DataFrame(todo, columns=["Date", "Hours", "Tag", "Description"])


# for i in todo:
#     createLink("m4k483bsn6sv35z", "crbfkuxfc1zxjxo", 2, i)

# Function to filter IDs of entries with "Date" in July

# data = {"Title": "Buy milk", "Done": True}

# createTableRow("m7wh22a5nh2n1cl", data)

# createLink("m3r09axnajlhb92", "crm80xjvhq0482n", 1, 3)
