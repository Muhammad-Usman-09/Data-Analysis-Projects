import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt 

# Function to load data and strip whitespace from string columns
@st.cache_data
def load_data():
    df = pd.read_csv('D:\Personal_Data\Freecodecamp_projects\Demographic Data Analyzer\data.csv') #if you want to use a different file, change the path here
    for col in df.select_dtypes(['object']).columns:
        df[col] = df[col].str.strip()
    return df

# Function to perform analysis based on iea filtered DataFrame
def analyze_data(df):
    
    # 1. Number of People of Each Race Represented in the Dataset
    st.header("1. Number of People of Each Race")
    race_counts = df['race'].value_counts()
    st.bar_chart(race_counts)
    st.markdown("---") 

    # 2. Average Age of Men
    st.header("2. Average Age of Men")
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    st.metric(label="Average Age of Men", value=f"{round(average_age_men, 1)} years")
    st.markdown("---")
    
    # 3. Percentage of People with a Bachelor's Degree
    st.header("3. Percentage with a Bachelor's Degree")
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
    st.metric(label="Percentage with a Bachelor's Degree", value=f"{round(percentage_bachelors, 1)}%")
    st.markdown("---")

    # 4. Percentage of People with Advanced Education Who Make More Than 50K
    st.header("4. Percentage with Advanced Education and High Income")
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    percentage_advanced_high_income = (df[advanced_education]['salary'] == '>50K').mean() * 100
    st.metric(label="High-Income Earners with Advanced Education", value=f"{round(percentage_advanced_high_income, 1)}%")
    st.markdown("---")

    # 5. Percentage of People Without Advanced Education Who Make More Than 50K
    st.header("5. Percentage Without Advanced Education and High Income")
    no_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    percentage_no_advanced_high_income = (df[no_advanced_education]['salary'] == '>50K').mean() * 100
    st.metric(label="High-Income Earners without Advanced Education", value=f"{round(percentage_no_advanced_high_income, 1)}%")
    st.markdown("---")
    
    # 6. Minimum Number of Hours a Person Works Per Week
    st.header("6. Minimum Hours Worked Per Week")
    min_hours_per_week = df['hours-per-week'].min()
    st.metric(label="Minimum Hours per Week", value=f"{min_hours_per_week} hours")
    st.markdown("---")
    
    # 7. Percentage of People Who Work the Minimum Number of Hours and Have a Salary of More Than 50K
    st.header("7. High-Income Earners with Minimum Hours")
    min_hours_high_income_percentage = (df[df['hours-per-week'] == min_hours_per_week]['salary'] == '>50K').mean() * 100
    st.metric(label="Percentage of High-Income Earners at Min Hours", value=f"{round(min_hours_high_income_percentage, 1)}%")
    st.markdown("---")
    
    # 8. Country with the Highest Percentage of People Earning >50K
    st.header("8. Country with Highest Percentage of High-Income Earners")
    country_salary_percentage = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
    if not country_salary_percentage.empty:
        highest_percentage_country = country_salary_percentage.idxmax()
        highest_percentage = country_salary_percentage.max()
        st.write(f"The country with the highest percentage is **{highest_percentage_country}** at **{round(highest_percentage, 1)}%**.")
    else:
        st.write("No data for high-income earners in the selected filters.")
    st.markdown("---")
    
    # 9. Most Popular Occupation for Those Who Earn >50K in India
    st.header("9. Most Popular Occupation in India with High Income")
    india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    if not india_high_income.empty:
        india_high_income_occupation = india_high_income['occupation'].mode()[0]
        st.write(f"The most popular occupation is: **{india_high_income_occupation}**.")
    else:
        st.write("No data for high-income earners in India with the current filters.")
    st.markdown("---")
    
    # Corrected Visualization: Age Distribution
    st.header("Age Distribution")
    fig, ax = plt.subplots()
    ax.hist(df['age'], bins=20)
    ax.set_title('Age Distribution')
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    st.pyplot(fig) 
    st.markdown("---")

# Main Streamlit app
def main():
    st.title("Demographic Data Analyzer")
    st.write("This application analyzes the Census Income Dataset with interactive filters.")
    st.markdown("---")

    # Load data
    try:
        df = load_data()
    except FileNotFoundError:
        st.error("Error: 'data.csv' file not found. Please make sure the file is in the same directory.")
        return

    # Add filters to a sidebar
    st.sidebar.header("Filter Data")

    age_range = st.sidebar.slider(
        "Select Age Range",
        min_value=int(df['age'].min()),
        max_value=int(df['age'].max()),
        value=(int(df['age'].min()), int(df['age'].max()))
    )
    
    hours_range = st.sidebar.slider(
        "Select Weekly Hours Range",
        min_value=int(df['hours-per-week'].min()),
        max_value=int(df['hours-per-week'].max()),
        value=(int(df['hours-per-week'].min()), int(df['hours-per-week'].max()))
    )

    countries = ['All'] + sorted(df['native-country'].unique().tolist())
    selected_country = st.sidebar.selectbox("Select Native Country", countries)
    
    # Filter the DataFrame based on user selections
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[(filtered_df['hours-per-week'] >= hours_range[0]) & (filtered_df['hours-per-week'] <= hours_range[1])]

    if selected_country != 'All':
        filtered_df = filtered_df[filtered_df['native-country'] == selected_country]

    if filtered_df.empty:
        st.warning("No data found for the selected filters.")
    else:
        analyze_data(filtered_df)

if __name__ == "__main__":
    main()