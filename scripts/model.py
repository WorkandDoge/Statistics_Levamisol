import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

#models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

def load_data(file_path):
    # Load the data
    data = pd.read_csv(file_path, na_values=[''], delimiter=',')

    return data

def perform_pca(data):
    # Perform PCA
    pca = PCA(n_components=0.95)
    principal_components = pca.fit_transform(data)
    return principal_components

def train_model(X_train, y_train):
    # Fit model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy}")

def main():
    file_path = '/Users/carinaobermuller/Documents/Statistics_Levamisol/data/fuseddata_selectedcolumn.csv'
    data = load_data(file_path)
    
    # Select columns from column 404 onwards
    X = data.iloc[:, 1:]
    y = data['Group_High_Low_Lev_COC_Ratio']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
