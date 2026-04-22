
<div align="center">

# ❤️ Heart Disease Prediction

**Machine Learning-powered early screening for cardiovascular diseases**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-22c55e)](LICENSE)

| Accuracy | Recall | Selected Model |
|:--------:|:------:|:--------------:|
| **83.6%** | **97.0%** | **Random Forest** |

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Dataset](#-dataset)
- [Pipeline](#-pipeline)
- [Model Comparison](#-model-comparison)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Results](#-results)
- [Future Scope](#-future-scope)
- [License](#-license)

---

## 🎯 Overview

> **"Early detection saves lives."**

Cardiovascular diseases (CVDs) are the **#1 cause of death globally**. Manual diagnosis is time-consuming and error-prone. This project delivers an **automated ML system** that predicts heart disease risk from clinical data in real-time.

| Metric | Value |
|--------|-------|
| 🎯 **Accuracy** | **83.6%** |
| 🔍 **Recall** | **97.0%** *(minimizes false negatives)* |
| ⚡ **Inference** | Real-time via Streamlit |
| 🏥 **Use Case** | Clinical early screening |

---

## 📊 Dataset

[![UCI](https://img.shields.io/badge/UCI-Repository-0366d6)](https://archive.ics.uci.edu/ml/datasets/heart+disease)
[![Rows](https://img.shields.io/badge/Rows-303-6b7280)]()
[![Features](https://img.shields.io/badge/Features-14-6b7280)]()

**Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/heart+disease) — Cleveland Heart Disease Dataset

### 🔑 Key Features

| Feature | Description | Type |
|:-------:|:------------|:----:|
| `age` | Age in years | 🔢 |
| `sex` | Sex (1=male, 0=female) | 🔢 |
| `cp` | Chest pain type | 📊 |
| `trestbps` | Resting blood pressure (mm Hg) | 🔢 |
| `chol` | Serum cholesterol (mg/dl) | 🔢 |
| `thalach` | Maximum heart rate achieved | 🔢 |
| `ca` | Major vessels colored by fluoroscopy | 🔢 |
| `slope` | Slope of peak exercise ST segment | 📊 |

**Target**: `target` — `0` = No Disease | `1` = Heart Disease

---

## 🔄 Pipeline

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Raw Data  │ → │ Preprocessing│ → │     EDA     │ → │    Model    │ → │  Dashboard  │
│  (303 rows) │    │  StandardScaler│    │  Heatmaps   │    │   Training  │    │  Streamlit  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### 🔧 Preprocessing Steps

| Step | Action | Status |
|:----:|:-------|:------:|
| 1️⃣ | Missing values check | ✅ None found |
| 2️⃣ | `StandardScaler` normalization | ✅ Applied |
| 3️⃣ | Train/Test split (80/20) | ✅ Completed |

---

## 🤖 Model Comparison

[![Best Model](https://img.shields.io/badge/Best%20Model-Random%20Forest-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white)]()

| Model | Accuracy | Precision | Recall | F1-Score | Status |
|:------|:--------:|:---------:|:------:|:--------:|:------:|
| Logistic Regression | 80.3% | 76.9% | 90.9% | 83.3% | ⚪ Baseline |
| **Random Forest** ⭐ | **83.6%** | **78.0%** | **97.0%** | **86.5%** | 🟢 **Selected** |
| SVM | 82.0% | 77.5% | 93.9% | 84.9% | 🔵 Alternative |

### 🏆 Why Random Forest?

```
┌─────────────────────────────────────────┐
│  ✅ Highest accuracy (83.6%)           │
│  ✅ Exceptional recall (97.0%)           │
│  │   → Catches 97% of sick patients    │
│  │   → Minimizes false negatives        │
│  ✅ Robust to outliers                   │
│  ✅ Captures complex interactions        │
└─────────────────────────────────────────┘
```

---

## 🚀 Installation

```bash
# 1️⃣ Clone repository
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction

# 2️⃣ Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate          # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt
```

### 📦 Requirements

```txt
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
streamlit>=1.0.0
```

---

## 💻 Usage

### 🎓 Train Model
```bash
python train_model.py
```

### 🖥️ Launch Dashboard
```bash
streamlit run app.py
```

[![Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?style=for-the-badge)]()

**Dashboard Features:**
- 📝 Sidebar input for patient vitals
- ⚡ **Real-time prediction**: High Risk vs Low Risk
- 📊 Probability scores with confidence intervals
- 🎨 Clean UI for non-technical medical staff

---

## 📁 Project Structure

```
heart-disease-prediction/
│
├── 📂 data/
│   └── heart.csv                          # Cleveland dataset (303 rows)
│
├── 📂 notebooks/
│   ├── 01_eda.ipynb                       # 🔍 Exploratory analysis
│   ├── 02_preprocessing.ipynb             # 🧹 Data cleaning
│   └── 03_model_training.ipynb            # 🤖 Model comparison
│
├── 📂 src/
│   ├── preprocess.py                      # Preprocessing utilities
│   ├── train.py                           # Training pipeline
│   └── predict.py                         # Inference utilities
│
├── 📂 models/
│   └── random_forest_model.pkl            # 💾 Saved best model
│
├── app.py                                 # 🖥️ Streamlit dashboard
├── requirements.txt                       # 📦 Dependencies
└── README.md                              # 📖 You are here!
```

---

## 📈 Results

### 🔥 Top Predictive Features

| Rank | Feature | Importance | Clinical Meaning |
|:----:|:-------:|:----------:|:-----------------|
| 🥇 | `cp` | **Highest** | Chest pain type |
| 🥈 | `thalach` | **High** | Max heart rate |
| 🥉 | `ca` | **High** | Major vessels |

### ✅ Validation

- 📊 **Confusion Matrix** — Confirms reliability
- 📈 **ROC Curve** — AUC analysis
- 🎯 **97% Recall** — Catches nearly all at-risk patients

---

## 🔮 Future Scope

- [ ] ⌚ **IoT Integration** — Real-time wearable monitors
- [ ] 🌐 **Larger Datasets** — Multi-ethnic generalization
- [ ] 🧠 **Deep Learning** — Neural network experiments
- [ ] 🚬 **Lifestyle Features** — Smoking, diet, exercise tracking

---

## 🙏 Acknowledgments

| Source | Contribution |
|:-------|:-------------|
| [UCI ML Repository](https://archive.ics.uci.edu/) | Cleveland Heart Disease Dataset |
| 🏥 Medical Professionals | Domain expertise & feature guidance |

---

## ⚖️ License

[![MIT](https://img.shields.io/badge/MIT-License-22c55e?style=for-the-badge)]()

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

> ⚠️ **Medical Disclaimer**
> 
> *This tool is designed for **assistance in early screening only** and should **not replace professional medical diagnosis**. Always consult a qualified healthcare provider for medical decisions.*

**Built with ❤️ for better healthcare**

</div>

