import pandas as pd
import pyreadstat
import os

# Read the .sav file into a pandas dataframe
df, meta = pyreadstat.read_sav('/Users/carinaobermuller/Documents/Masterfile_Cross_Sectional.sav')

# Create the "data" folder if it doesn't exist
if not os.path.exists('/Users/carinaobermuller/Documents/Statistics_Levamisol/data'):
    os.makedirs('/Users/carinaobermuller/Documents/Statistics_Levamisol/data')

# Write the dataframe to a .csv file in the "data" folder
df.to_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/data/Masterfile_Cross_Sectional.csv', index=False)

# Move the existing fused data file to a temporary location
if os.path.exists('/Users/carinaobermuller/Documents/Statistics_Levamisol/data/Fused_Data.csv'):
    os.rename('/Users/carinaobermuller/Documents/Statistics_Levamisol/data/Fused_Data.csv', '/Users/carinaobermuller/Documents/Statistics_Levamisol/data/Fused_Data_temp.csv')

# Create a new fused data file and append the Masterfile_Cross_Sectional.csv to it
fused_data = pd.DataFrame()
fused_data = fused_data.append(pd.read_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/data/Masterfile_Cross_Sectional.csv'))

# Append the contents of the temporary fused data file to the new fused data file
if os.path.exists('/Users/carinaobermuller/Documents/Statistics_Levamisol/data/Fused_Data_temp.csv'):
    fused_data = fused_data.append(pd.read_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/data/Fused_Data_temp.csv'))

# Write the fused data file
fused_data.to_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/data/Fused_Data.csv', index=False)

# Save variable definitions to a csv file in the "data" folder
variable_definitions = meta.column_names_to_labels
df_definitions = pd.DataFrame(variable_definitions.items(), columns=['Variable', 'Definition'])
df_definitions.to_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/data/Variable_Definitions.csv', index=False)

# Export value labels to a csv file in the "data" folder
value_labels = meta.variable_value_labels
df_value_labels = pd.DataFrame(value_labels.items(), columns=['Variable', 'Value Labels'])
df_value_labels.to_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/data/Value_Labels.csv', index=False)