# Factors Influencing Hospital Readmissions: A Health Data Analysis Project

## Overview
This project analyzes factors influencing hospital readmissions using a patient dataset. It demonstrates data cleaning, exploratory data analysis (EDA), statistical testing, and logistic regression modeling to identify key predictors of readmission.

## Dataset
The dataset contains patient information such as:
- **Demographics:** Age, gender, race  
- **Health factors:** Length of stay, disease, discharge status  
- **Target:** Readmission (0 = not readmitted, 1 = readmitted)

**Files:**
- [Raw dataset](data/readmission.csv)  
- [Cleaned dataset](data/readmission_clean_simple.csv)

## Project Workflow

1. **Data Cleaning**  
   - [Script: `1_data_cleaning.py`](scripts/1_data_cleaning.py)  
   - Loads raw dataset  
   - Removes irrelevant columns and missing data  
   - Saves cleaned dataset as `data/readmission_clean_simple.csv`

2. **Exploratory Data Analysis (EDA)**  
   - [Script: `2_eda.py`](scripts/2_eda.py)  
   - Visualizes readmission counts  
   - Compares length of stay and patient age between readmitted vs. non-readmitted patients  
   - Examines readmission by disease type  
   - Creates LOS bins to analyze readmission rates

3. **Statistical Testing**  
   - [Script: `3_stat_tests.py`](scripts/3_stat_tests.py)  
   - Performs a t-test comparing length of stay between readmitted and non-readmitted patients  
   - Visualizes differences with annotated boxplots

4. **Logistic Regression Modeling**  
   - [Script: `4_logistic_regression.py`](scripts/4_logistic_regression.py)  
   - One-hot encodes categorical features  
   - Splits data into training and testing sets (70/30)  
   - Fits logistic regression to predict readmission  
   - Evaluates model using accuracy and classification report  
   - Identifies top predictors of readmission  
   - Plots predicted probability of readmission vs. length of stay

## Visualizations
All visualizations are saved in the [`visualizations/`](visualizations) folder:

- [Age by Readmission Status](visualizations/age_by_readmission_status.png)  
- [LOS vs Readmission](visualizations/los_vs_readmission.png)  
- [Predicted Readmission Probability vs LOS](visualizations/predicted_readmission_probability_vs_los.png)  
- [Readmission by Disease](visualizations/readmission_by_disease.png)  
- [Readmission Count](visualizations/readmission_count.png)  
- [Readmission Rate by LOS Bin](visualizations/readmission_rate_by_los_bin.png)  
- [Top Predictors of Readmission](visualizations/top_predictors_of_readmission.png)

## Full Report
- [Final Report (PDF)](final_report.pdf)

## How to Run
1. Place `readmission.csv` in the `data/` folder  
2. Run each script in order:
   ```bash
   python scripts/1_data_cleaning.py
   python scripts/2_eda.py
   python scripts/3_stat_tests.py
   python scripts/4_logistic_regression.py
   ```
3. Visualizations will display, and outputs will print in the console

## Tools and Libraries
- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- SciPy  
- Scikit-learn  

## Key Takeaways
- Length of stay alone does not strongly predict readmission  
- Patient-specific factors such as age and disease type are stronger predictors  
- Logistic regression modeling identifies asthma, influenza, and older age as high-risk indicators  
- Predictive analytics can guide individualized discharge planning and improve patient outcomes  

## Author
**Sofia Strisch**  
