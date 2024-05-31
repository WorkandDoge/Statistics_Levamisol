import pandas as pd
import os
import scipy.stats as stats

def define_groups():
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/data/fuseddata.csv')
    
    # Create Group 1 by filtering rows where 'Group_High_Low_Lev_COC_Ratio' is 0.0 or 1.0
    group1 = data[(data['Group_High_Low_Lev_COC_Ratio'] == 0.0) | (data['Group_High_Low_Lev_COC_Ratio'] == 1.0)]

    # Create Group 2 by filtering rows where 'Group_High_Low_Lev_COC_Ratio' is 2.0
    group2 = data[data['Group_High_Low_Lev_COC_Ratio'] == 2.0]

    # Print the two groups
    print("Group 1:")
    print(group1)
    print("\nGroup 2:")
    print(group2)

    return group1, group2

def calculate_average(group1, group2):
    # Calculate the average of each column in group1
    group1_average = pd.DataFrame(columns=['Column', 'Average'])
    for column in group1.columns:
        try:
            average = group1[column].mean()
            group1_average = pd.concat([group1_average, pd.DataFrame({'Column': [column], 'Average': [average]})], ignore_index=True)
        except TypeError:
            continue

    # Calculate the average of each column in group2
    group2_average = pd.DataFrame(columns=['Column', 'Average'])
    for column in group2.columns:
        try:
            average = group2[column].mean()
            group2_average = pd.concat([group2_average, pd.DataFrame({'Column': [column], 'Average': [average]})], ignore_index=True)
        except TypeError:
            continue

    # Save the averages to a CSV file
    averages = pd.concat([group1_average.set_index('Column'), group2_average.set_index('Column')], axis=1)
    averages.columns = ['Group 1 Average', 'Group 2 Average']
    averages.to_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/results/averages.csv')

    return group1_average, group2_average

def perform_t_test(group1, group2):
    # Create a DataFrame to store the t-test results
    results = pd.DataFrame(columns=['Column', 't-statistic', 'p-value'])

    # Perform t-test for every column in the groups
    for column in group1.columns:
        try:
            t_statistic, p_value = stats.ttest_ind(group1[column], group2[column])
            results = pd.concat([results, pd.DataFrame({'Column': [column], 't-statistic': [t_statistic], 'p-value': [p_value]})], ignore_index=True)
        except TypeError:
            continue

    # Save the results to a CSV file
    results.to_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/results/t_test_results.csv', index=False)

    # Print the results
    print("T-Test Results:")
    print(results)

    return results

def save_results(group1_average, group2_average, results):
    # Combine the group averages and t-test results into a single DataFrame
    combined_results = pd.merge(group1_average, group2_average, on='Column', how='outer')
    combined_results = pd.merge(combined_results, results, on='Column', how='outer')
    
    # Add group labels to the average columns
    combined_results.rename(columns={'Average': 'Group 1 Average'}, inplace=True)
    combined_results.rename(columns={'Average_x': 'Group 1 Average'}, inplace=True)
    combined_results.rename(columns={'Average_y': 'Group 2 Average'}, inplace=True)

    # Save the combined results to a CSV file
    combined_results.to_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/results/combined_results.csv', index=False)

    return combined_results

def filter_significant_results(combined_results):
    # Add a new column 'Significance' to combined_results
    combined_results['Significance'] = ''
    
    # Update the 'Significance' column based on the p-value
    combined_results.loc[combined_results['p-value'] < 0.05, 'Significance'] = 'significant'
    
    # Filter the significant results
    significant_results = combined_results[combined_results['Significance'] == 'significant']
    
    # Save the significant results to a CSV file
    significant_results.to_csv('/Users/carinaobermuller/Documents/Statistics_Levamisol/results/significant_results.csv', index=False)
    
    return significant_results

def main():
    # Call the function with the defined groups
    group1, group2 = define_groups()
    group1_average, group2_average = calculate_average(group1, group2)
    results = perform_t_test(group1, group2)
    combined_results = save_results(group1_average, group2_average, results)
    filter_significant_results(combined_results)

if __name__ == "__main__":
    main()
