Heart Disease Prediction using Machine Learning
    An automated ML-based system to assist medical professionals in early screening of cardiovascular diseases using clinical parameters.

Overview
Cardiovascular diseases (CVDs) are the leading cause of death globally. Early detection is critical for effective treatment and prevention, yet manual diagnosis can be time-consuming and prone to human error. This project develops a predictive model that identifies the presence of heart disease based on clinical parameters, achieving 83.6% accuracy with a 97.0% recall rate to minimize false negatives.
Dataset
Table
Property	Details
Source	UCI Machine Learning Repository — Cleveland Heart Disease Dataset
Size	303 rows × 14 clinical features
Target	target (0 = No Disease, 1 = Heart Disease)
Key Features
Table
Feature	Description
age	Age in years
sex	Sex (1 = male, 0 = female)
cp	Chest pain type
trestbps	Resting blood pressure (mm Hg)
chol	Serum cholesterol (mg/dl)
thalach	Maximum heart rate achieved
ca	Number of major vessels colored by fluoroscopy
slope	Slope of the peak exercise ST segment
Project Pipeline
plain
Copy

Raw Data → Preprocessing → EDA → Model Training → Evaluation → Streamlit Dashboard

1. Data Preprocessing

    Missing Values: Checked for null values (none found in cleaned version)
    Feature Scaling: Applied StandardScaler to normalize numerical features
    Data Splitting: 80% Training / 20% Testing

2. Exploratory Data Analysis (EDA)

    Correlation heatmap to identify feature relationships
    Target distribution analysis (balanced dataset)
    Feature importance ranking

3. Model Comparison
Table
Model	Accuracy	Precision	Recall	F1-Score
Logistic Regression	80.3%	76.9%	90.9%	83.3%
Random Forest ⭐	83.6%	78.0%	97.0%	86.5%
SVM	82.0%	77.5%	93.9%	84.9%
Selected Model: Random Forest Classifier

    Highest overall accuracy (83.6%)
    Exceptional recall (97.0%) — crucial for healthcare to minimize false negatives
    Robustness to outliers and ability to capture complex feature interactions

Installation
bash
Copy

# Clone the repository
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

Requirements
txt
Copy

pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
streamlit>=1.0.0

Usage
Training the Model
bash
Copy

python train_model.py

Launching the Dashboard
bash
Copy

streamlit run app.py

The dashboard features:

    Sidebar for patient data input (Age, BP, Cholesterol, etc.)
    Real-time prediction: High Risk vs Low Risk
    Probability scores for clinical confidence
    Designed for ease of use by non-technical medical staff

Results & Visualizations

    Confusion Matrix and ROC Curve confirm model reliability
    Feature importance analysis identifies cp (chest pain), thalach (max heart rate), and ca (major vessels) as most significant predictors
    Model successfully identifies high-risk patients with high sensitivity

Project Structure
plain
Copy

heart-disease-prediction/
├── data/
│   └── heart.csv                    # Cleveland dataset
├── notebooks/
│   ├── 01_eda.ipynb                 # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb       # Data cleaning & scaling
│   └── 03_model_training.ipynb      # Model comparison & selection
├── src/
│   ├── preprocess.py                # Data preprocessing utilities
│   ├── train.py                     # Model training script
│   └── predict.py                   # Prediction utilities
├── app.py                           # Streamlit dashboard
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
└── models/
    └── random_forest_model.pkl      # Saved best model

Future Scope

    [ ] Integration with real-time wearable health monitors (IoT)
    [ ] Training on larger, more diverse datasets for better generalization
    [ ] Implementing Deep Learning (Neural Networks) for potentially higher accuracy
    [ ] Adding lifestyle features: smoking, diet, exercise habits

License
This project is licensed under the MIT License.
Acknowledgments

    UCI Machine Learning Repository for the Cleveland Heart Disease Dataset
    Medical professionals for domain expertise in feature selection

    Disclaimer: This tool is designed for assistance in early screening only and should not replace professional medical diagnosis. Always consult a qualified healthcare provider for medical decisions.
