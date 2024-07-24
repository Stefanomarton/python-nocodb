from nocodb import NocoDB
import json
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime as dt


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

        records = [Record.from_dict(record) for record in data["list"]]

        page_info = PageInfo.from_dict(data["pageInfo"])

        return cls(list=records, pageInfo=page_info)


###############################################################################

# Define the NocoDB URL components
# hosturl = "http://10.1.0.170:8080"
# port = 8080
# api_token = "jkjlH0Jk_3i_p4h5W5tZ7pCtx8RtJv9I76kCNRvR"


# client = NocoDB(hosturl, port, api_token)

# # Fetch table entries
# entries = client.getTableEntries(
#     "mcu569c5t3pofvv",
# )

# print(entries)

# root = Root.from_json(entries)

# print(root.list)

# filter by tag
# for record in root.list:
#     if record.Tag == "ECOCHIMICA":
#         print(record)

# filter by date
# for record in root.list:
#     if record.Date.month == 7:
#         print(record.Id)

# print pageInfo
# print(root.pageInfo)

# print(root.list[0].Report.Title)
