# KUDET: İkinci El Araç Değerleme Sistemi

# KUDET: Second-Hand Vehicle Valuation System

## Summary
In this study, the price estimation problem in Turkey's second-hand vehicle market is addressed. Using data collected via web scraping, a price prediction model based on vehicle features was developed by applying machine learning techniques.

## 👥 AUTHORS
- Binnur Soztutar 

##  Methodology
### Dataset
- Data Source: arabam.com
- Raw Sample Size: 1565 vehicle records
- Cleaned Sample Size: 1396 vehicle records
- Features: 12 different vehicle features:
  - model
  - model_detail
  - model_year
  - price
  - city
  - district
  - ad_type
  - type
  - brand
  - engine_volume
  - engine_type
  - equipment

### Model Performance
1. Linear Regression
   - R² Score: 0.91
   - RMSE: 118,771.59
   - MSE: 14,106,689,691.00
   - Tolerance R² (±10,000 TL): 0.91
   - Tolerance % R² (±50% difference): 0.97

   > 💡 Tolerance values indicate the model's performance at different error tolerance levels:
   > - R² = 0.91 at ±10,000 TL tolerance → The model makes consistent predictions within this range
   > - R² = 0.97 at ±50% tolerance → The model is more successful in wide price ranges

2. Classification (Random Forest)
   - accuracy: 0.79
   - F1-Score: 0.84
   - Precision: 0.86
   - Recall: 0.83
   - Macro avg: 0.80

### 📈 Error Analysis
- Mean Error: 7,880 TL
- Median Error: 4.06 TL
- Std Deviation: 118,722 TL
- Min Error: -903,950 TL
- Max Error: 419,178 TL

### 🔍 Model Features
- Number of features: 11 (1 numerical, 10 categorical)
- Dataset size: 1396 vehicles
- Train/Test split: 80/20
- Pipeline usage: StandardScaler and OneHotEncoder

### 📊 Visualizations
- Actual vs Predicted comparison
- Error distribution histogram
- Box plot analysis
- Performance graphs by price ranges

### 🔄 Data Preprocessing
1. Outlier Analysis
   - Outlier detection with IQR method
   - Statistical analysis and cleaning
2. Categorical Variable Transformations
   - One-Hot Encoding
   - Label Encoding
3. Feature Engineering
   - Feature selection
   - Feature scaling

## Technical Requirements
### Software Requirements
- Python 3.8.7
- Jupyter Notebook
- Required libraries:
```bash
numpy>=1.24.3
pandas>=2.0.3
matplotlib>=3.7.1
seaborn>=0.12.2
scikit-learn>=1.3.0
jupyter>=1.0.0
```

## Installation and Running
1. Clone the repository:
```bash
git clone https://github.com/kudetx/kudet-arac-degerleme.git
cd kudet-arac-degerleme
```

2. Install the required libraries:
```bash
pip install -r requirements.txt
```

3. Run the Jupyter Notebooks:
```bash
jupyter notebook
```

### Comparative Analysis
#### Model Comparison
1. **Linear Regression**
   - ✅ High R² score (0.88)
   - ✅ Low RMSE value (144,789.99 TL)
   - ✅ Consistent performance in wide price ranges
   - ⚠️ May be affected by outliers

2. **Random Forest**
   - ✅ High accuracy rate (0.82)
   - ✅ Balanced F1-Score (0.81)
   - ✅ Resistant to outliers
   - ⚠️ Higher computational cost

#### Usage Scenarios
- **Linear Regression:**
  - General price estimation
  - When fast results are required
  - If the dataset is clean and outliers are removed

- **Random Forest:**
  - Price range classification
  - When outliers cannot be fully cleaned
  - For cases requiring higher accuracy

#### Performance Comparison
| Metric                | Linear Regression     | Random Forest      |
|-----------------------|----------------------|--------------------|
| R² / Accuracy         | 0.91                 | 0.79               |
| RMSE                  | 118,771.59 TL        | -                  |
| MSE                   | 14,106,689,691.00    | -                  |
| Tolerance (±10k TL)   | 0.91                 | -                  |
| Tolerance (±%50)      | 0.97                 | -                  |
| F1-Score              | -                    | 0.84               |
| Precision             | -                    | 0.86               |
| Recall                | -                    | 0.83               |
| Macro Avg             | -                    | 0.80               |
> 💡 **About Tolerance Metrics:**
> - R² with ±10,000 TL tolerance = 0.88: The model makes consistent predictions within a 10,000 TL error margin
> - R² with ±50% tolerance = 0.95: The model performs better in wide price ranges
> - These values indicate the model's reliability at different error tolerance levels

#### Model Selection Criteria
- **If Speed is a Priority:** Linear Regression
- **If Accuracy is a Priority:** Random Forest
- **For Balanced Performance:** Use ensemble of models

###  Updates and Version Info
- Version: 1.0.0
- Last Update: June 2023
- Python Version: 3.8.7+

## 📝 License
This project is licensed under the MIT License.