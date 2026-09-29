# Suspicious Activity Detector

## Overview

The Suspicious Activity Detector is a machine learning-based cybersecurity project that classifies network traffic as either **BENIGN** or **ATTACK**.

The project uses network-flow features from the CIC-IDS2017 dataset and compares three machine learning algorithms:

- Logistic Regression
- Decision Tree
- Random Forest

The purpose of this project is to build a basic foundation for detecting suspicious network activity using machine learning.

---

## Objectives

- Analyze network traffic data.
- Clean and preprocess network-flow data.
- Convert multiple attack categories into a binary classification problem.
- Train different machine learning models.
- Compare model performance using accuracy, precision, recall, and F1-score.
- Handle class imbalance.
- Identify important network traffic features.
- Demonstrate predictions on known benign and attack traffic.

---

## Dataset

The project uses the **CIC-IDS2017** network traffic dataset.

The dataset file used in this project is:

`Tuesday-WorkingHours.pcap_ISCX.csv`

The original dataset contains several types of network traffic. For this project, the labels were converted into two classes:

| Original Label | Target |
|---|---:|
| BENIGN | 0 |
| Any attack | 1 |

After preprocessing:

- Total flows: **421,828**
- Features: **78**
- BENIGN flows: **412,676**
- ATTACK flows: **9,152**

---

## Project Structure

```text
suspicious-activity-detector/
│
├── data/
│   └── Tuesday-WorkingHours.pcap_ISCX.csv
│
├── models/
│   └── random_forest_model.pkl
│
├── notebooks/
│   └── suspicious_activity_detector.ipynb
│
├── results/
│   ├── graphs/
│   └── reports/
│
├── src/
│   └── predict.py
│
├── .gitignore
└── README.md

**### Technologies Used**
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook
- Joblib
- Git
- GitHub

**### Data Preprocessing**
The following preprocessing steps were performed:
1. Loaded the network traffic dataset.
2. Removed duplicate records.
3. Handled missing values.
4. Removed records with negative flow duration.
5. Converted infinite values to missing values.
6. Filled numerical missing values using the median.
7. Converted the original attack labels into a binary target.
8. Split the dataset into training and testing sets using stratification.
9. Standardized features for Logistic Regression.

The dataset was split into:
- 80% training data
- 20% testing data

**### Machine Learning Models**

#### 1. Logistic Regression
Logistic Regression was used as the baseline classification model.
Metric      Score

Accuracy    99.8732%
Precision   97.0508%
Recall      97.1038%
F1-score    97.0773%

#### 2. Decision Tree
A Decision Tree classifier was trained using the original numerical features.
Metric      Score

Accuracy    99.9941%
Precision   99.8907%
Recall      99.8361%
F1-score    99.8634%

#### 3. Random Forest
A Random Forest classifier with 100 trees was trained for the final prediction demonstration.
Metric      Score

Accuracy    99.9953%
Precision   100.0000%
Recall      99.7814%
F1-score    99.8906%

### **Model Comparison**
Model               Accuracy    Precision   Recall      F1-score
Logistic Regression 99.8732%    97.0508%    97.1038%    97.0773%
Decision Tree       99.9941%    99.8907%    99.8361%    99.8634%
Random Forest       99.9953%    100.0000%   99.7814%    99.8906%


### **Class Imbalance**
The dataset contains significantly more benign traffic than attack traffic.
Class     Count       Percentage
BENIGN    412,676     97.83%
ATTACK    9,152       2.17%
A class-weighted Logistic Regression model was also tested to study the effect of class imbalance.

### **Results:**
Metric      Standard Logistic Regression       Class-Weighted Logistic Regression
Accuracy        99.8732%                            99.0209%
Precision       97.0508%                            69.0008%
Recall          97.1038%                            99.6175%
F1-score        97.0773%                            81.5295%
This demonstrates the trade-off between reducing missed attacks and increasing false positives.

**### Feature Importance**
Random Forest feature importance was used to identify influential network traffic features.

Some of the highest-ranked features were:
1. Destination Port
2. Packet Length Std
3. Packet Length Mean
4. Average Packet Size
5. Total Backward Packets
6. Avg Bwd Segment Size
7. Bwd Header Length
8. Packet Length Variance
9. Bwd Packet Length Mean
10. Fwd Packet Length Std

The feature-importance graph is available in:
results/graphs/
random_forest_feature_importance.png

### **Prediction Demonstration**
The trained Random Forest model was tested on known network flows.
Example:
Actual class: ATTACK
Predicted class: ATTACK
BENIGN probability: 0.00%
ATTACK probability: 100.00%

Another example:
Actual class: BENIGN
Predicted class: BENIGN
BENIGN probability: 100.00%
ATTACK probability: 0.00%

The reusable prediction code is available in:
src/predict.py

### **Results**
The project demonstrates that machine learning models can classify network-flow records into benign and attack categories using network traffic features.

The project also demonstrates:
- Network traffic preprocessing
- Binary attack classification
- Model comparison
- Confusion matrix analysis
- Class imbalance analysis
- Feature importance analysis
- Prediction using a saved Random Forest model

### **Limitations**
This project is a dataset-based machine learning detector and is not a real-time intrusion detection system.

The current version:
- Works with network-flow datasets.
- Does not capture live network packets.
- Does not perform real-time monitoring.
- Uses a fixed trained model.
-D oes not yet provide explainable AI explanations for individual predictions.

These limitations will be addressed in the future main Explainable ML-Based Intrusion Detection System project.

### **Future Scope

**The project can be extended by:
- Adding real-time network traffic capture.
- Using live packet analysis.
- Adding more attack categories.
- Testing additional machine learning algorithms.
- Applying explainable AI techniques such as SHAP.
- Creating a web-based monitoring dashboard.
- Generating alerts for suspicious activity.
- Integrating the detector with the main IDS project.


Author
V Rekha 