from nocodb import NocoDB
import json
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime as dt
import calendar


@dataclass
class tsReport:
    Id: int
    Month: str


@dataclass
class rRecord:
    Id: int
    Date: Optional[dt]
    CreatedAt: Optional[dt]
    UpdatedAt: Optional[dt]
    Hours: Optional[float]
    Mese: Optional[str]
    Year: int

    def from_dict(data):
        # Handle UpdatedAt properly
        updated_at = data.get("UpdatedAt")
        if isinstance(updated_at, str):
            updated_at = dt.fromisoformat(updated_at)
        else:
            updated_at = None

        return rRecord(
            Id=data["Id"],
            Date=dt.strptime(data["Month"], "%Y-%m-%d"),
            CreatedAt=dt.fromisoformat(data["CreatedAt"]),
            UpdatedAt=updated_at,
            Hours=data["Hours"],
            Mese=data["Month-2"],
            Year=data["Year"],
        )


@dataclass
class tsRecord:
    Id: int
    Date: dt
    CreatedAt: dt
    UpdatedAt: Optional[dt]
    Hours: float
    nc_c4dl___Report_id: Optional[int]
    Company: str
    Description: Optional[str]
    Report: Optional[tsReport]

    @staticmethod
    def from_dict(data: dict):

        if not data.get("Date"):
            return

        updated_at = data.get("UpdatedAt")
        if isinstance(updated_at, str):
            updated_at = dt.fromisoformat(updated_at)
        else:
            updated_at = None

        return tsRecord(
            Id=data["Id"],
            Date=dt.strptime(data["Date"], "%Y-%m-%d"),
            CreatedAt=dt.fromisoformat(data["CreatedAt"]),
            UpdatedAt=updated_at,
            Hours=data["Hours"],
            nc_c4dl___Report_id=data.get("nc_c4dl___Report_id"),
            Company=data["Company"],
            Description=data.get("Description"),
            Report=tsReport(**data["Report"]) if data.get("Report") else None,
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
class rRoot:
    list: List[rRecord]
    pageInfo: PageInfo

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)

        records = [rRecord.from_dict(record) for record in data["list"]]

        page_info = PageInfo.from_dict(data["pageInfo"])

        return cls(list=records, pageInfo=page_info)


@dataclass
class tsRoot:
    list: List[tsRecord]
    pageInfo: PageInfo

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)

        records = [tsRecord.from_dict(record) for record in data["list"]]

        page_info = PageInfo.from_dict(data["pageInfo"])

        return cls(list=records, pageInfo=page_info)


###############################################################################

# Define the NocoDB URL components
hosturl = "http://10.1.0.170:8080"
port = 8080
api_token = "jkjlH0Jk_3i_p4h5W5tZ7pCtx8RtJv9I76kCNRvR"

client = NocoDB(hosturl, port, api_token)

timesheet = tsRoot.from_json(client.getTableEntries("msxaagv1ckx1gy1"))

# for record in timesheet.list:
#     id = record.Id
#     date = record.Date
#     month = calendar.month_name[record.Date.month]
#     year = record.Date.year
#     client.updateTableRow("msxaagv1ckx1gy1", {"Id": id, "Month": month, "Year": year})

import calendar
from collections import defaultdict

# Initialize a nested dictionary to accumulate total hours
hours_accumulated = defaultdict(lambda: defaultdict(float))

# List of companies to process
companies = ["ERGON", "BORSINI", "ECOCHIMICA", "ARCHIMEDE-FIBRE"]

# First pass: Accumulate total hours for each company, month, and year
for record in timesheet.list:
    if record.Company in companies:
        year = record.Date.year
        month = record.Date.month
        company = record.Company
        hours_accumulated[company][(year, month)] += float(
            record.Hours
        )  # Convert Hours to float


# # Second pass: Create a single new entry for each company, month, and year combination
for company, monthly_data in hours_accumulated.items():
    for (year, month), total_hours in monthly_data.items():
        month_name = calendar.month_name[month]
        total = total_hours * 12.5

        # Create a single entry for the accumulated hours
        client.createTableRow(
            "muaye44fwmd7zi7",
            {
                "Company": company,
                "Year": year,
                "Month": month_name,
                "Total Hours": total_hours,
                "Total": total,
            },
        )


# for record in report.list:
#     id = record.Id
#     month = record.Date
#     month = calendar.month_name[record.Date.month]
#     year = record.Date.year
#     client.updateTableRow("m4k483bsn6sv35z", {"Id": id, "Month-2": month, "Year": year})

# print(report.list)
# def getReportID(month: int):
#     reportId = None
#     for record in report.list:
#         if record is not None and record.Date.month == month:
#             reportId = record.Id
#             break
#     return reportId


# def getTimesheetID(month: int):
#     timesheetId = []
#     for record in timesheet.list:
#         if record is not None and record.Date.month == month:
#             timesheetId.append(record.Id)
#     return timesheetId


# for i in range(1, 13):
#     # Step 1: Get the list of timesheet IDs
#     timesheet_ids = getTimesheetID(i)

#     # Step 2: Get the report ID
#     report_id = getReportID(i)

#     if not timesheet_ids or not report_id:
#         continue  # Skip to the next iteration if either is empty

#     # Step 3: Loop through each timesheet ID and create the link
#     for b in timesheet_ids:
#         client.createLink(
#             "m4k483bsn6sv35z",
#             "crbfkuxfc1zxjxo",
#             report_id,
#             b,
#         )

# # Define the year
# year = 2025

# # Iterate over each month of the year
# for month in range(1, 13):  # 1 through 12
#     # Format the month and year
#     formatted_date = f"{year}-{month}-1"

#     # Prepare data dictionary
#     data = {"Month": formatted_date}

#     # Create a table row
#     client.createTableRow("m4k483bsn6sv35z", data)

#     # Print or log to confirm the operation
#     print(f"Created table row for: {formatted_date}")

# totale = 0
# for record in timesheet.list:
#     if record.Tag == "ECOCHIMICA":
#         if record.Date.month == 7:
#             totale = totale + record.Hours

# print(totale * 12.5)
