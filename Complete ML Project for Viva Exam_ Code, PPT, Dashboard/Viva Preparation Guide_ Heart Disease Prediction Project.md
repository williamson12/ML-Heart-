# Viva Preparation Guide: Heart Disease Prediction Project

This guide contains likely questions and answers for your viva-based practical exam, along with code explanation highlights.

## 1. Likely Questions & Answers

### Q1: Why did you choose this specific dataset?
**Answer:** I chose the UCI Cleveland Heart Disease dataset because it is a well-established, peer-reviewed dataset in the medical ML community. It contains 14 critical clinical features (like chest pain type, cholesterol, and max heart rate) that are medically recognized as significant risk factors for cardiovascular disease, making it ideal for a real-world predictive modeling project.

### Q2: Why did you use these three specific models (Logistic Regression, Random Forest, SVM)?
**Answer:** I used these models to represent different approaches to classification:
- **Logistic Regression**: A baseline linear model that is highly interpretable.
- **Random Forest**: An ensemble method that handles non-linear relationships and is robust to outliers.
- **SVM**: A powerful model for high-dimensional data that finds the optimal decision boundary.
Comparing them allows us to justify why a more complex model (Random Forest) is better than a simple one for this specific problem.

### Q3: What is Correlation, and why is it important in EDA?
**Answer:** Correlation measures the linear relationship between two variables. In EDA, a correlation heatmap helps us identify which features (like `cp` or `thalach`) have a strong relationship with the target variable (`heart disease`). It also helps detect **multicollinearity**, where two features are highly correlated with each other, which can sometimes negatively affect model performance.

### Q4: Explain Bias vs. Variance in the context of your models.
**Answer:** 
- **Bias** is the error from overly simple assumptions (underfitting). Logistic Regression might have higher bias if the data is non-linear.
- **Variance** is the error from sensitivity to small fluctuations in the training set (overfitting). 
Random Forest balances this by using multiple trees (bagging) to reduce variance while maintaining low bias.

### Q5: What is Overfitting, and how did you prevent it?
**Answer:** Overfitting occurs when a model learns the noise in the training data rather than the actual pattern, leading to poor performance on new data. I prevented it by:
1. Using **Random Forest**, which naturally reduces overfitting through ensemble averaging.
2. Using **Train-Test Split (80:20)** to evaluate the model on unseen data.
3. Using **StandardScaler** to ensure all features are on the same scale.

### Q6: Why is 'Recall' more important than 'Accuracy' in this project?
**Answer:** In medical diagnosis, a **False Negative** (telling a sick person they are healthy) is much more dangerous than a **False Positive** (telling a healthy person they might be sick). **Recall** measures our ability to find all positive cases. Our Random Forest model has a high recall (97%), meaning it rarely misses a patient with heart disease.

---

## 2. Code Explanation Highlights

### Data Preprocessing
- **StandardScaler**: "I used `StandardScaler` to normalize the numerical features. This is important because features like `chol` (200+) and `oldpeak` (0-6) have different scales, and scaling ensures the model treats them fairly."

### Model Training
- **Random Forest**: "I chose `n_estimators=100`, meaning the model builds 100 different decision trees and takes a majority vote for the final prediction. This makes the model more stable and accurate."

### Streamlit Dashboard
- **st.cache_resource**: "I used Streamlit's caching to load the model and scaler only once. This makes the app much faster because it doesn't have to reload the heavy model file every time a user moves a slider."
- **scaler.transform(input_df)**: "It's crucial to scale the user's input using the *same* scaler we used during training, otherwise the model will receive data in a format it doesn't understand."

### Evaluation Metrics
- **Classification Report**: "I used `classification_report` to see the Precision, Recall, and F1-Score for both classes (0 and 1), ensuring the model performs well for both healthy and diseased patients."
