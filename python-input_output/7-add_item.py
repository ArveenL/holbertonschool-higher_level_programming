#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
and then save them to a file
-----------------------------------------------------

-> Step by step in plain English:

1. Check the file :- See if add_item.json already exists.

2. Load the list :- If it exists, read the current list from it;
otherwise, start with an empty list.

3. Get your inputs :- Take everything you type after the script name
in the terminal

4. Add inputs to the list :- Put these new items at the end of the list.

5. Save the list :- Write the updated list back to add_item.json so it’s
stored for next time.

6. Basically: keep a list in a file and keep adding new items to it
every time you run the script.
"""


import sys
from pathlib import Path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, else start with empty list
if Path(filename).exists():
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add all command line arguments (excluding script name)
my_list.extend(sys.argv[1:])

# Save updated list back to JSON file
save_to_json_file(my_list, filename)
