import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def load_data(file_path):
    # Load the data
    data = pd.read_csv(file_path)
    return data

def create_group1(data):
    # Create Group 1 by filtering rows where 'Group_High_Low_Lev_COC_Ratio' is 0.0 or 1.0
    group1 = data[(data['Group_High_Low_Lev_COC_Ratio'] == 0.0) | (data['Group_High_Low_Lev_COC_Ratio'] == 1.0)]
    return group1

def create_group2(data):
    # Create Group 2 by filtering rows where 'Group_High_Low_Lev_COC_Ratio' is 2.0
    group2 = data[data['Group_High_Low_Lev_COC_Ratio'] == 2.0]
    return group2

def filter_numerical_columns(data):
    # Filter out non-numerical columns
    numerical_columns = data.select_dtypes(include='number').columns
    data = data[numerical_columns]
    return data

def perform_pca(data):
    # Perform PCA
    pca = PCA(n_components=0.95)
    principal_components = pca.fit_transform(data)
    return principal_components

def perform_clustering(principal_components):
    # Perform hierarchical clustering
    clustering = AgglomerativeClustering(n_clusters=5)
    cluster_labels = clustering.fit_predict(principal_components)
    return cluster_labels

def combine_clusters_with_data(data, cluster_labels):
    # Combine the cluster labels with the original data
    data_with_clusters = pd.concat([data, pd.DataFrame(cluster_labels, columns=['Cluster'])], axis=1)
    return data_with_clusters

def split_data(data_with_clusters, groups):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data_with_clusters, groups, test_size=0.2)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    # Fit a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy}")

def main():
    file_path = '/Users/carinaobermuller/Documents/Statistics_Levamisol/scripts/fusedata.py'
    data = load_data(file_path)
    group1 = create_group1(data)
    group2 = create_group2(data)
    data = filter_numerical_columns(data)
    principal_components = perform_pca(data)
    cluster_labels = perform_clustering(principal_components)
    data_with_clusters = combine_clusters_with_data(data, cluster_labels)
    X_train, X_test, y_train, y_test = split_data(data_with_clusters, groups)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
