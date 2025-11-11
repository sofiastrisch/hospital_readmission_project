# ======================================================
# 2_eda.py
# Exploratory Data Analysis on Hospital Readmissions
# ======================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("readmission_clean_simple.csv")

# -----------------------------
# Readmission Count
# -----------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x="readmission", data=df, palette="Set2")
plt.title("Readmission Count")
plt.xticks([0, 1], ['Not Readmitted', 'Readmitted'])
plt.show()

# -----------------------------
# Length of Stay by Readmission
# -----------------------------
plt.figure(figsize=(6, 4))
sns.boxplot(x="readmission", y="patient_length_of_stay",
            data=df, palette="Set3")
plt.title("Length of Stay by Readmission Status")
plt.show()

# -----------------------------
# Patient Age by Readmission
# -----------------------------
plt.figure(figsize=(6, 4))
sns.boxplot(x="readmission", y="patient_age", data=df, palette="Pastel1")
plt.title("Age by Readmission Status")
plt.show()

# -----------------------------
# Readmission by Disease
# -----------------------------
if 'patient_disease' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.countplot(x='patient_disease', hue='readmission', data=df)
    plt.xticks(rotation=45)
    plt.title("Readmission by Disease")
    plt.show()

# -----------------------------
# LOS Bins and Readmission Rate
# -----------------------------
max_los = df['patient_length_of_stay'].max()
bins = [0, 1, 3, 5, 7, 10, 14, 21, 30, max_los+1]
labels = ['0-1', '2-3', '4-5', '6-7', '8-10', '11-14', '15-21', '22-30', '31+']
df['LOS_bin'] = pd.cut(df['patient_length_of_stay'],
                       bins=bins, labels=labels, right=False)

readmit_rate = df.groupby('LOS_bin')['readmission'].mean()
plt.figure(figsize=(10, 5))
readmit_rate.plot(kind='bar', color='purple')
plt.ylabel("Readmission Rate")
plt.xlabel("Length of Stay Bin (days)")
plt.title("Readmission Rate by LOS Bin")
plt.show()
