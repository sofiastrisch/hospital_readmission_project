import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("readmission_clean_simple.csv")


los_readmitted = df[df["readmission"] == 1]["patient_length_of_stay"]
los_not_readmitted = df[df["readmission"] == 0]["patient_length_of_stay"]


t_stat, p_val = stats.ttest_ind(los_readmitted, los_not_readmitted)
print("=== T-Test: LOS by Readmission ===")
print(f"T-statistic = {t_stat:.4f}, p-value = {p_val:.4f}")


plt.figure(figsize=(7, 5))
sns.boxplot(x='readmission', y='patient_length_of_stay', data=df)
plt.xticks([0, 1], ['Not Readmitted', 'Readmitted'])
plt.ylabel("Length of Stay (days)")
plt.title("Length of Stay vs Readmission")
plt.text(0.5, max(df['patient_length_of_stay'])*0.95, f"p-value = {p_val:.4f}",
         horizontalalignment='center', fontsize=12, color='red')
plt.show()
