import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

#import possible models
from sklearn.linear_model import LogisticRegression
from sklearn import svm #svm.SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

def load_data(file_path):
    # Load the data
    data = pd.read_csv(file_path, na_values=[''], delimiter=',')

    return data

def perform_pca(data):
    # Perform PCA
    pca = PCA(n_components=0.93)
    principal_components = pca.fit_transform(data)
    return principal_components

def tune_hyperparameters(X_train, y_train):
    # Define the parameter grid
    param_grid = {
        'hidden_layer_sizes': [(50,50,50), (50,100,50), (100,)],
        'activation': ['tanh', 'relu'],
        'solver': ['sgd', 'adam'],
        'alpha': [0.0001, 0.05],
        'learning_rate': ['constant','adaptive'],
    }

    # Create a MLPClassifier object
    mlp = MLPClassifier(random_state=42)

    # Create a GridSearchCV object
    grid_search = GridSearchCV(mlp, param_grid, cv=5)

    # Fit the GridSearchCV object to the data
    grid_search.fit(X_train, y_train)

    # Get the best parameters
    best_params = grid_search.best_params_

    print(best_params)

    # Return the best model
    return grid_search.best_estimator_
def train_model(X_train, y_train):
    # Fit model
    model = model = MLPClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy}")

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)

    # Classification report
    report = classification_report(y_test, y_pred)
    print("Classification Report:")
    print(report)

def main():
    file_path = '/Users/carinaobermuller/Documents/Statistics_Levamisol/output_files/fuseddata_HP_COC_Total.csv' # change to the path of the merged data file with the variable to predict
    data = load_data(file_path)
    principal_components = perform_pca(data.iloc[:, 1:])
    X = principal_components
    y = data['HP_COC_Total'] # change according to the column name in the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    model = train_model(X_train, y_train)
    # Tune hyperparameters and get the best model
    model = tune_hyperparameters(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
