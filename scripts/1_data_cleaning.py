import pandas as pd


file_path = "readmission.csv" 
df = pd.read_csv(file_path)


drop_cols = [
    "patient_id", "hospital_name", "Admission_date",
    "patient_first_initial", "patient_last_name",
    "doctor_name", "time_slot", "patient_checkin_date",
    "patient_checkout_date"
]
df = df.drop(columns=[c for c in drop_cols if c in df.columns])


columns_to_keep = [
    "patient_gender", "patient_age", "patient_race",
    "patient_disease", "patient_length_of_stay",
    "discharge_status", "readmission"
]
df = df[[c for c in columns_to_keep if c in df.columns]]


df = df.dropna()


df.to_csv("readmission_clean_simple.csv", index=False)
print("✅ Cleaned dataset saved as readmission_clean_simple.csv")
