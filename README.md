# <p align = "center"> MEDICAL INSURANCE COST PREDICTION</p>

# PROJECT OVERVIEW
Health insurance costs have risen dramatically over the past decade in response to the rising cost of health care services and are determined by a multitude of factors. Let's look at the cost of healthcare for a sample of the population given age, sex, bmi, number of children, smoking habits, and region.

The purpose of this project is to determine the contributing factors and predict health insurance cost by performing exploratory data analysis using Tableau and predictive modeling on the Health Insurance dataset. This project makes use of Numpy, Pandas, Sci-kit learn, and Data Visualization libraries.

**Overview:**
* Seek insight from the dataset with Exploratory Data Analysis using Tableau
* Performed Data Processing, Data Engineering and Feature Transformation to prepare data before modeling
* Built a model to predict Insurance Cost based on the features
* Evaluated the model using various Performance Metrics like MSE, MAE, RMSE, RMSLE and R2

# DATA DESCRIPTION
1. age: age of primary beneficiary
2. sex: insurance contractor gender, female, male
3. bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height,
objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9
4. children: Number of children covered by health insurance / Number of dependents
5. smoker: Smoking
6. region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest
7. charges: Individual medical costs billed by health insurance

Data source : https://www.kaggle.com/mirichoi0218/insurance

# INSIGHTS
The insights drawn by performing `Data Analysis Using Tableau` are:

* Features like Sex and Region has an almost balanced distribution.
* Majority of the policyholders fall in Overweight and Obese category.
* Most of the policyholders are Non-Smokers.
* Highest number of policyholders are in the range of 18 to 22 years old.
* A person who smokes and have a BMI above 30 (Obese) tends to have a higher medical cost.
* Older people who smoke have more expensive charges.
* Most of the policyholders have 1 to 2 children as dependencies.

# DATA PROCESSING 
1. Check missing value - there are none <br>
2. Check duplicate value - there are 1 duplicate, will be remove <br>
3. Feature engineering - make a new column `weight_status` based on BMI score <br>
4. Feature transformation: <br>
 A) Encoding `sex`, `region`, & `weight_status` attributes <br>
 B) Ordinal encoding `smoker` attribute <br>
5. Modeling: <br>
 A) Separating target & features <br>
 B) Splitting train & test data <br>
 C) Modeling using Linear Regression, Decision Tree, Random Forest, Ridge Regression and Lasso Regression <br>
 D) Feature Importance Ranking <br>
 E) Find the best algorithm <br>
 
## CONCLUSION
Based on the predictive modeling, Linear Regression (Fitted Polynomial Regression of Degree 2) algorithm has the best score compared to others. <br>
Therefore, Linear Regression algorithm is the best fitted model.