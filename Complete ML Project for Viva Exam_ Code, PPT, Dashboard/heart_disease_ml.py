import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import pickle

# 1. DATA LOADING
def load_data(path='heart.csv'):
    """Load the heart disease dataset."""
    df = pd.read_csv(path)
    print(f"Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

# 2. DATA PREPROCESSING
def preprocess_data(df):
    """Handle missing values, scaling, and splitting."""
    # Check for missing values
    if df.isnull().sum().sum() > 0:
        df = df.fillna(df.mean())
    
    # Features and Target
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Splitting
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, X.columns

# 3. EXPLORATORY DATA ANALYSIS (EDA)
def perform_eda(df):
    """Generate visualizations for the project."""
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.savefig('correlation_heatmap.png')
    plt.close()
    
    plt.figure(figsize=(8, 6))
    sns.countplot(x='target', data=df, palette='viridis')
    plt.title('Distribution of Heart Disease (Target)')
    plt.savefig('target_distribution.png')
    plt.close()

# 4. MODEL TRAINING & EVALUATION
def train_and_evaluate(X_train, X_test, y_train, y_test):
    """Train 3 models and compare them."""
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "SVM": SVC(probability=True, random_state=42)
    }
    
    results = []
    trained_models = {}
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        metrics = {
            "Model": name,
            "Accuracy": accuracy_score(y_test, y_pred),
            "Precision": precision_score(y_test, y_pred),
            "Recall": recall_score(y_test, y_pred),
            "F1-Score": f1_score(y_test, y_pred)
        }
        results.append(metrics)
        trained_models[name] = model
        
    return pd.DataFrame(results), trained_models

# MAIN EXECUTION
if __name__ == "__main__":
    # Load
    df = load_data()
    
    # EDA
    perform_eda(df)
    
    # Preprocess
    X_train, X_test, y_train, y_test, scaler, feature_names = preprocess_data(df)
    
    # Train & Evaluate
    comparison_df, models = train_and_evaluate(X_train, X_test, y_train, y_test)
    
    print("\nModel Comparison Table:")
    print(comparison_df)
    
    # Feature Importance for Random Forest
    rf_model = models["Random Forest"]
    importances = rf_model.feature_importances_
    feat_importances = pd.Series(importances, index=feature_names)
    
    plt.figure(figsize=(10, 6))
    feat_importances.nlargest(10).plot(kind='barh')
    plt.title('Top 10 Feature Importances (Random Forest)')
    plt.savefig('feature_importance.png')
    plt.close()
    
    # Save the best model (Random Forest usually performs well here)
    import pickle
    with open('best_model.pkl', 'wb') as f:
        pickle.dump(models["Random Forest"], f)
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    print("\nProject files generated: correlation_heatmap.png, target_distribution.png, feature_importance.png, best_model.pkl, scaler.pkl")
