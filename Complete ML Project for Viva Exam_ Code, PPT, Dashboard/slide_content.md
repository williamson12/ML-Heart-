# Heart Disease Prediction using Machine Learning

## 1. Title Slide
- **Project Title**: Heart Disease Prediction using Machine Learning
- **Presented by**: [Your Name]
- **Objective**: To develop a predictive model that identifies the presence of heart disease based on clinical parameters.

## 2. Objective
- To analyze patient medical data and identify key risk factors for heart disease.
- To build and compare multiple machine learning models (Logistic Regression, Random Forest, SVM).
- To select the most accurate model for real-time prediction via a user-friendly dashboard.

## 3. Problem Statement
- Cardiovascular diseases (CVDs) are the leading cause of death globally.
- Early detection is critical for effective treatment and prevention.
- Manual diagnosis can be time-consuming and prone to human error.
- **Solution**: An automated ML-based system to assist medical professionals in early screening.

## 4. Dataset Description
- **Source**: UCI Machine Learning Repository (Cleveland Heart Disease Dataset).
- **Size**: 303 rows and 14 clinical features.
- **Target Variable**: `target` (0 = No Disease, 1 = Heart Disease).
- **Key Features**: Age, Sex, Chest Pain Type (cp), Resting Blood Pressure (trestbps), Serum Cholesterol (chol), Maximum Heart Rate (thalach), etc.

## 5. Data Preprocessing
- **Missing Values**: Checked for null values (none found in this cleaned version).
- **Feature Scaling**: Applied `StandardScaler` to normalize numerical features like age, cholesterol, and blood pressure.
- **Data Splitting**: 80% Training set and 20% Testing set to evaluate model performance on unseen data.

## 6. Exploratory Data Analysis (EDA)
- **Correlation Heatmap**: Identified relationships between features (e.g., `cp`, `thalach`, and `slope` show positive correlation with the target).
- **Target Distribution**: Balanced dataset with a slight majority of heart disease cases.
- **Feature Importance**: `cp` (chest pain), `thalach` (max heart rate), and `ca` (major vessels) were found to be the most significant predictors.

## 7. Algorithms Used & Why
- **Logistic Regression**: A baseline model for binary classification; simple and interpretable.
- **Random Forest**: An ensemble method that handles non-linear relationships and reduces overfitting.
- **Support Vector Machine (SVM)**: Effective in high-dimensional spaces and robust against outliers.

## 8. Model Comparison
| Model | Accuracy | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- |
| Logistic Regression | 80.3% | 76.9% | 90.9% | 83.3% |
| **Random Forest** | **83.6%** | **78.0%** | **97.0%** | **86.5%** |
| SVM | 82.0% | 77.5% | 93.9% | 84.9% |

## 9. Final Model Selection
- **Selected Model**: Random Forest Classifier.
- **Justification**:
  - Highest overall accuracy (83.6%).
  - Exceptional Recall (97.0%), which is crucial in healthcare to minimize "False Negatives" (missing a sick patient).
  - Robustness to outliers and ability to capture complex feature interactions.

## 10. Results & Visualization
- The model successfully identifies high-risk patients with high sensitivity.
- Visualizations like the Confusion Matrix and ROC Curve (discussed in viva) confirm the model's reliability.
- Feature importance analysis provides clinical insights into risk factors.

## 11. UI/Dashboard Preview
- Built using **Streamlit**.
- Features a sidebar for patient data input (Age, BP, Cholesterol, etc.).
- Provides real-time prediction (High Risk vs. Low Risk) with probability scores.
- Designed for ease of use by non-technical medical staff.

## 12. Conclusion
- Machine learning can significantly aid in the early detection of heart disease.
- The Random Forest model proved to be the most effective for this dataset.
- Automation of risk assessment can save lives by enabling early intervention.

## 13. Future Scope
- Integration with real-time wearable health monitors (IoT).
- Training on larger, more diverse datasets for better generalization.
- Implementing Deep Learning (Neural Networks) for potentially higher accuracy.
- Adding more features like lifestyle habits (smoking, diet, exercise).
