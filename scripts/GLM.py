import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def load_data(file_path):
    # Load the data
    try:
        data = pd.read_csv(file_path, na_values=[''], delimiter=',')
    except pd.errors.ParserError:
        print("Error parsing file, switching to Python engine")
        data = pd.read_csv(file_path, na_values=[''], delimiter=',', engine='python')
    
    return data

def perform_pca(data):
    # Perform PCA
    pca = PCA(n_components=0.95)
    principal_components = pca.fit_transform(data)
    return principal_components

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
    
    # Select columns from column 404 onwards
    X = data.iloc[:, 404:]
    y = data['Group_High_Low_Lev_COC_Ratio']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
