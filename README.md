# Factors Influencing Hospital Readmissions: A Health Data Analysis Project

## Overview
This project analyzes factors influencing hospital readmissions using a patient dataset. It demonstrates data cleaning, exploratory data analysis (EDA), statistical testing, and logistic regression modeling to identify key predictors of readmission.

## Dataset
The dataset contains patient information such as:
- **Demographics:** Age, gender, race  
- **Health factors:** Length of stay, disease, discharge status  
- **Target:** Readmission (0 = not readmitted, 1 = readmitted)

**Files:**
- Raw dataset: `./data/readmission.csv`  
- Cleaned dataset: `./data/readmission_clean_simple.csv`

## Project Workflow

1. **Data Cleaning**  
   - Script: `/scripts/1_data_cleaning.py`  
   - Loads raw dataset  
   - Removes irrelevant columns and missing data  
   - Saves cleaned dataset as `data/readmission_clean_simple.csv`

2. **Exploratory Data Analysis (EDA)**  
   - Script: `./scripts/2_eda.py`  
   - Visualizes readmission counts  
   - Compares length of stay and patient age between readmitted vs. non-readmitted patients  
   - Examines readmission by disease type  
   - Creates LOS bins to analyze readmission rates

3. **Statistical Testing**  
   - Script: `./scripts/3_stat_tests.py`  
   - Performs a t-test comparing length of stay between readmitted and non-readmitted patients  
   - Visualizes differences with annotated boxplots

4. **Logistic Regression Modeling**  
   - Script: `./scripts/4_logistic_regression.py`  
   - One-hot encodes categorical features  
   - Splits data into training and testing sets (70/30)  
   - Fits logistic regression to predict readmission  
   - Evaluates model using accuracy and classification report  
   - Identifies top predictors of readmission  
   - Plots predicted probability of readmission vs. length of stay

## Visualizations
All visualizations are saved in the `visualizations/` folder:

- `age_by_readmission_status.png`: `./visualizations/age_by_readmission_status.png`  
- `los_vs_readmission.png`: `./visualizations/los_vs_readmission.png`  
- `predicted_readmission_probability_vs_los.png`: `./visualizations/predicted_readmission_probability_vs_los.png`  
- `readmission_by_disease.png`: `./visualizations/readmission_by_disease.png`  
- `readmission_count.png`: `./visualizations/readmission_count.png`  
- `readmission_rate_by_los_bin.png`: `./visualizations/readmission_rate_by_los_bin.png`  
- `top_predictors_of_readmission.png`: `./visualizations/top_predictors_of_readmission.png`

## Full Report
Final report (PDF): `./final_report.pdf`

## How to Run
1. Place `readmission.csv` in the `data/` folder  
2. Run each script in order:  
   ```
   python scripts/1_data_cleaning.py  
   python scripts/2_eda.py  
   python scripts/3_stat_tests.py  
   python scripts/4_logistic_regression.py  
   ```
3. Visualizations will display and outputs will print in the console.

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
