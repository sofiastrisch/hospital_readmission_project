# Basic Sepsis Detection Script

A simple Python script that evaluates a set of vital signs and lab values to identify potential sepsis in a patient. The script flags abnormal findings and provides a **sepsis alert** if multiple abnormalities are detected.

## Overview
This project demonstrates a basic sepsis detection algorithm using threshold-based rules on common vital signs and lab values:
- Heart rate
- Systolic blood pressure
- Respiratory rate
- Temperature
- Oxygen saturation (SpO2)
- White blood cell count (WBC)
- Lactate

If 3 or more abnormalities are present, the script prints a sepsis alert and recommends completing the sepsis pathway.

## Python Script
The script is located in the `scripts/` folder:

[View or download `basic_sepsis.py`](scripts/basic_sepsis.py)

## Example Output

```
⚠️ SEPSIS ALERT: Multiple abnormalities detected.
Please complete sepsis pathway: blood cultures, urine cultures, lactate, CBC, CMP, and notify MD.
```

## How to Run
1. Make sure you have **Python 3.6+** installed.
2. Download or clone this repository.
3. Navigate to the `scripts/` folder.
4. Run the script using:

```bash
python basic_sepsis.py
```

## Skills Demonstrated
- Python programming fundamentals
- Conditional statements and threshold logic
- Basic clinical decision support logic
- Clear console output for alerts

## Author
**Sofia Strisch**  
Toronto, Canada  
Registered Nurse | Data & Health Analytics Enthusiast
