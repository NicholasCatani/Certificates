##### Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve, auc
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier

##### CSV

df = pd.read_csv(r"C:\Users\Nicho\Desktop\Data.csv")

##### EDA

print(df.head())
print(df.describe())
print(df.info())

##### Preprocessing

categorical_cols = df.select_dtypes(include=["object", "bool"]).columns.tolist()
numerical_cols = df.select_dtypes(include=["float64"]).columns.tolist()

numerical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numerical_transformer, numerical_cols),
        ("cat", categorical_transformer, categorical_cols[:-1])
])

X = df.drop(["Made_Purchase"], axis=1)
y = df["Made_Purchase"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

X_train_preprocessed = preprocessor.fit_transform(X_train)
X_test_preprocessed = preprocessor.transform(X_test)

print(X_train_preprocessed.shape, X_test_preprocessed.shape)

##### Visualization

plt.figure(figsize=(8, 5))
sns.countplot(x="Made_Purchase", data=df)
plt.title("Distribution of Target Variable")
plt.xlabel("Purchase")
plt.ylabel("Total # of Purchases")
plt.show()

plt.figure(figsize=(8, 5))
corr_matrix = df[numerical_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix of Numerical Features")
plt.show()

plt.figure(figsize=(15, 5))
for i, col in enumerate(['HomePage_Duration', 'ProductDescriptionPage_Duration', 'GoogleMetric:Page Values'], start=1):
    plt.subplot(1, 3, i)
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

##### Modeling "Logistic Regression"

model = LogisticRegression(random_state=0, max_iter=1000)
model.fit(X_train_preprocessed, y_train)
y_pred = model.predict(X_test_preprocessed)
y_pred_proba = model.predict_proba(X_test_preprocessed)[:,1]

##### Evaluation

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, label="Logistic Regression (area = %0.2f" % roc_auc)
plt.plot([0, 1], [0, 1], "k--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend(loc="lower right")
plt.show()

print(round(accuracy, 3))
print(round(precision, 3))
print(round(recall, 3))
print(round(f1, 3))
print(round(roc_auc, 3))

##### Continue...

RF = RandomForestClassifier(random_state=0)
GB = GradientBoostingClassifier(random_state=0)
SVM = SVC(probability=True, random_state=0)

classifiers = {
    "Random Forest": RF,
    "Gradient Boosting": GB,
    "SVM": SVM
}

model_results = {}

for model_name, model in classifiers.items():
    model.fit(X_train_preprocessed, y_train)

    y_pred = model.predict(X_test_preprocessed)
    y_pred_proba = model.predict_proba(X_test_preprocessed)[:, 1] if model_name != "SVM" else model.predict_proba(X_test_preprocessed)[:, 1]

    model_accuracy = accuracy_score(y_test, y_pred)
    model_precision = precision_score(y_test, y_pred)
    model_recall = recall_score(y_test, y_pred)
    model_f1 = f1_score(y_test, y_pred)
    model_roc_auc = roc_auc_score(y_test, y_pred_proba)

    model_results[model_name] = {
        "Accuracy": model_accuracy,
        "Precision": model_precision,
        "Recall": model_recall,
        "F1-Score": model_f1,
        "ROC-AUC": model_roc_auc
    }

print(model_results)

##### XGBoost

XGB = XGBClassifier(use_label_encoder=False, eval_metric="logloss", random_state=0)
XGB.fit(X_train_preprocessed, y_train)
y_pred_xgb = XGB.predict(X_test_preprocessed)
y_pred_proba_xgb = XGB.predict_proba(X_test_preprocessed)[:, 1]

accuracy_xgb = accuracy_score(y_test, y_pred_xgb)
precision_xgb = precision_score(y_test, y_pred_xgb)
recall_xgb = recall_score(y_test, y_pred_xgb)
f1_xgb = f1_score(y_test, y_pred_xgb)
roc_auc_xgb = roc_auc_score(y_test, y_pred_proba_xgb)

xgb_results = {
    "Accuracy": accuracy_xgb,
    "Precision": precision_xgb,
    "Recall": recall_xgb,
    "F1-Score": f1_xgb,
    "ROC-AUC": roc_auc_xgb
}

print(xgb_results)










