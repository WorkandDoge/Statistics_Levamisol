import os
import pandas as pd

folder_path = '/Users/carinaobermuller/Documents/Statistics_Levamisol/data'
output_file = '/Users/carinaobermuller/Documents/Statistics_Levamisol/data/fuseddata.csv'

# Get a list of all the files in the folder
file_list = os.listdir(folder_path)

# Ensure that Masterfile_Cross_Sectional.csv is the first file in the list
master_file = 'Masterfile_Cross_Sectional.csv'
if master_file in file_list:
    file_list.remove(master_file)
    file_list.insert(0, master_file)

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Iterate over each file in the folder
for file_name in file_list:
    # Exclude specific files
    if file_name in ['fuseddata.csv', 'Value_Labels.csv', 'Variable_Definitions.csv']:
        continue
    
    # Check if the file is a CSV file or a text/ASCII table
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file_name)[1]
        if file_extension == '.csv':
            # Read the CSV file into a DataFrame if it is not empty
            if os.path.getsize(file_path) > 0:
                data = pd.read_csv(file_path)
            else:
                continue
        else:
            # Read the text/ASCII table into a DataFrame with specified encoding if it is not empty
            if os.path.getsize(file_path) > 0:
                data = pd.read_table(file_path, encoding='utf-8')
            else:
                continue
        
        # Remove the first column from the data
        data = data.iloc[:, 1:]
        
        
        # Add suffix to column headers based on origin file
        origin_suffix = ''
        if '_T1' in file_name:
            origin_suffix = '_T1'
        elif '_T2' in file_name:
            origin_suffix = '_T2'
        
        data.columns = [col + origin_suffix for col in data.columns]
        
        # Merge the data horizontally with the existing merged data
        merged_data = pd.concat([merged_data, data], axis=1)

# Save the merged data to a new CSV file
merged_data.to_csv(output_file, index=False)

