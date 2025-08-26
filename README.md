# Data Analysis Projects

A collection of Python-based data analysis projects demonstrating skills in data cleaning, preprocessing, visualization, and statistical analysis.
Each project uses Pandas, Matplotlib/Seaborn, and Streamlit to create interactive dashboards and insights.

---

## Projects Included

### 1. Demographic Data Analyzer

**Overview**  
The **Demographic Data Analyzer** project utilizes Pandas to analyze demographic data extracted from the 1994 Census database. The dataset includes various attributes such as age, education, occupation, and salary, which are used to answer several analytical questions. This project aims to provide insights into demographic trends and salary distribution based on educational and occupational factors.

**Dataset**  
The dataset used in this project is sourced from the UCI Machine Learning Repository and includes the following columns:
- `age`
- `workclass`
- `fnlwgt`
- `education`
- `education-num`
- `marital-status`
- `occupation`
- `relationship`
- `race`
- `sex`
- `capital-gain`
- `capital-loss`
- `hours-per-week`
- `native-country`
- `salary`

**Features**
1. **Number of People by Race**: Computes the number of individuals belonging to each race.
2. **Average Age of Men**: Calculates the average age of male individuals.
3. **Percentage of People with a Bachelor's Degree**: Determines the percentage of people holding a Bachelor's degree.
4. **Advanced Education Salary Analysis**: Analyzes the percentage of individuals with advanced education (Bachelors, Masters, Doctorate) earning more than $50K.
5. **Non-Advanced Education Salary Analysis**: Analyzes the percentage of individuals without advanced education earning more than $50K.
6. **Minimum Working Hours**: Identifies the minimum number of hours worked per week.
7. **Minimum Hours & High Income Percentage**: Calculates the percentage of individuals working the minimum number of hours per week who earn more than $50K.
8. **Country with Highest Percentage Earning >$50K**: Finds the country with the highest percentage of people earning more than $50K and its percentage.
9. **Most Popular Occupation for High Earners in India**: Identifies the most common occupation among individuals earning more than $50K in India.

---

### 2. Medical Data Visualizer

**Overview**  
The Medical Data Visualizer project analyzes and visualizes a cardiovascular health dataset.
It highlights relationships between BMI, blood pressure, cholesterol, glucose, lifestyle factors and the risk of cardiovascular disease.


**Dataset**  
The dataset includes medical examination results with the following columns:
- `age`
- `sex`
- `height`
- `weight`
- `ap_hi` (Systolic blood pressure)
- `ap_lo` (Diastolic blood pressure)
- `cholesterol`
- `gluc` (Glucose)
- `smoke`
- `alco` (Alcohol intake)
- `active` (Physical activity)
- `cardio` (Cardiovascular disease)

**Features**
1. **BMI Calculation**: Computes the Body Mass Index (BMI) for each individual in the dataset.
2. **Cholesterol Levels Analysis**: Analyzes cholesterol levels across different age groups.
3. **Blood Pressure Distribution**: Visualizes the distribution of systolic and diastolic blood pressure.
4. **Health Risk Factors**: Identifies and visualizes common risk factors for cardiovascular diseases.
5. **Correlation Matrix**: Generates a correlation matrix to explore relationships between health metrics.

---

## Getting Started

Each project folder contains:
- **Data**: The dataset used in the analysis.
- **Code**: Python scripts and notebooks.
- **Results**: Visualizations and insights.

Feel free to explore, fork, and contribute. For any questions or suggestions, open an issue or reach out.
