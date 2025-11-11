# ======================================================
# 4_logistic_regression.py
# Logistic Regression for Predicting Hospital Readmissions
# ======================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("readmission_clean_simple.csv")

# Encode categorical features
categorical_cols = ["patient_disease",
                    "discharge_status", "patient_gender", "patient_race"]
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Features & target
X = df_encoded.drop(columns=["readmission"])
X = X.select_dtypes(include=['int64', 'float64'])  # keep only numeric
y = df_encoded["readmission"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Fit logistic regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Print results
print("\n=== Logistic Regression Results ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(
    y_test, y_pred, zero_division=0))

# Feature Importance
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
}).sort_values(by="Coefficient", key=abs, ascending=False).head(10)

print("\n=== Top 10 Predictors of Readmission ===")
print(coefficients)

# Plot top 10 coefficients
plt.figure(figsize=(8, 6))
sns.barplot(x="Coefficient", y="Feature",
            data=coefficients, palette="coolwarm")
plt.title("Top Predictors of Readmission")
plt.show()

# Predicted probability vs LOS (holding other factors constant)
los_range = pd.DataFrame({'patient_length_of_stay': range(df['patient_length_of_stay'].min(),
                                                          df['patient_length_of_stay'].max()+1),
                          'patient_age': df['patient_age'].mean()})
# Add categorical dummy columns with 0
for col in X.columns:
    if col not in los_range.columns:
        los_range[col] = 0
los_range = los_range[X.columns]

# Predict probabilities
probabilities = model.predict_proba(los_range)[:, 1]

plt.figure(figsize=(8, 5))
plt.plot(los_range['patient_length_of_stay'],
         probabilities, color='purple', linewidth=2)
plt.xlabel("Length of Stay (days)")
plt.ylabel("Predicted Probability of Readmission")
plt.title("Predicted Readmission Probability vs LOS")
plt.show()
