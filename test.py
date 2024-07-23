from nocodb import *

# Load the JSON data from the file
# data = getTableEntries("mcu569c5t3pofvv")

# print(json.dumps(filterEntriesByMonth("mcu569c5t3pofvv", 7)))
todo = filterEntriesByMonth("mcu569c5t3pofvv", 6)

# df = pd.DataFrame(todo, columns=["Date", "Hours", "Tag", "Description"])

# Display the DataFrame
print(todo)

# for i in todo:
#     createLink("m4k483bsn6sv35z", "crbfkuxfc1zxjxo", 2, i)

# Function to filter IDs of entries with "Date" in July

# data = {"Title": "Buy milk", "Done": True}

# createTableRow("m7wh22a5nh2n1cl", data)

# createLink("m3r09axnajlhb92", "crm80xjvhq0482n", 1, 3)
