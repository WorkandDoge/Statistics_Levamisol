import pandas as pd
import pyreadstat
import os

# Read the .sav file into a pandas dataframe
df, meta = pyreadstat.read_sav('/Users/carinaobermuller/Documents/Masterfile_Cross_Sectional.sav')

# Write the dataframe to a .csv file in the "data" folder
df.to_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/data/Masterfile_Cross_Sectional.csv', index=False)

# Save variable definitions to a csv file in the "data" folder
variable_definitions = meta.column_names_to_labels
df_definitions = pd.DataFrame(variable_definitions.items(), columns=['Variable', 'Definition'])
df_definitions.to_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/output_files/Variable_Definitions.csv', index=False)

# Export value labels to a csv file in the "data" folder
value_labels = meta.variable_value_labels
df_value_labels = pd.DataFrame(value_labels.items(), columns=['Variable', 'Value Labels'])
df_value_labels.to_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/output_files/Value_Labels.csv', index=False)