################################
##   FUNCTION   ################
################################

def convert(path):
    
    # Import necessary dependencies
    import pandas as pd
    import json
    
    # Convert sheet 'Experiment' to json format
    to_json = pd.read_excel(f"{path}", sheet_name= "Experiment")

    key_line = list(to_json.iloc[0]) # Isolate first line
    val_line = list(to_json.iloc[1]) # Isolate secnd line

    final = dict(zip(key_line, val_line))
    with open(f"{path[:-4]}.json", 'w') as file:
        json.dump(final, file)

    # Convert sheet 'Tests' to csv format
    to_csv  = pd.read_excel(f"{path}", sheet_name= "Tests")
    to_csv.to_csv(f"{path[:-4]}.csv", index=False)


################################
##   CORE CODE   ###############
################################

# Import dependency
import glob

# List all files with .xls extension
all_xls = glob.glob('*/*.xls')

# Loop through each, and convert it to csv and json
for path in all_xls:
    convert(path=path)
