import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set Streamlit page configuration
st.set_page_config(layout="wide")

# Function to load and preprocess the data
@st.cache_data
def load_data():
    try:
        # Load the data from the correct file path
        df = pd.read_csv(r"D:\Personal_Data\Freecodecamp_projects\Medical data visualizer\cardio_train.csv") 
    except FileNotFoundError:
        st.error("Error: 'cardio_train.csv' file not found. Please make sure the file is in the same directory.")
        return None

    # Add 'overweight' column
    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

    # Normalize data by making 0 always good and 1 always bad.
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

    # Convert age from days to years
    df['age_years'] = (df['age'] / 365.25).astype(int)

    # Gender column ko user-friendly banaya gaya hai
    df['gender'] = df['gender'].replace({1: 'Female', 2: 'Male'})

    return df

# Function to draw Categorical Plot
def draw_cat_plot(df):
    st.header("Categorical Plot: Health Factors vs. Cardiovascular Disease")
    st.write("This plot shows the relationship between various health factors (like cholesterol, smoking, and physical activity) and the presence of cardiovascular disease.")
    
    # Create DataFrame for cat plot using `pd.melt` 
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    
    # Group and reformat the data
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x="variable", y="total", hue="value", col="cardio", data=df_cat, kind="bar").fig
    st.pyplot(fig)

# Function to draw Heat Map
# Function to draw Heat Map
def draw_heat_map(df):
    st.header("Correlation Heatmap")
    st.write("This heatmap shows the correlation between different health metrics. A value close to 1 indicates a strong positive correlation, while a value close to -1 indicates a strong negative correlation.")
    
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    # Non-numerical columns ko drop kiya gaya hai
    corr = df_heat.drop(columns=['gender', 'age_years']).corr() 

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        linewidths=.5,
        ax=ax,
        center=0,
        cbar_kws={'shrink': 0.5},
    )
    st.pyplot(fig)

# Main Streamlit app
def main():
    st.title("Medical Data Visualizer")
    st.write("This application visualizes a medical dataset to show the relationship between health factors and cardiovascular disease. You can use the sidebar to filter the data.")
    st.markdown("---")

    df = load_data()
    if df is None:
        return

    # Add filters to a sidebar
    st.sidebar.header("Filter Data")

    age_range = st.sidebar.slider(
        "Age Range (Years)",
        min_value=int(df['age_years'].min()),
        max_value=int(df['age_years'].max()),
        value=(int(df['age_years'].min()), int(df['age_years'].max()))
    )
    
    # sorted(df['gender'].unique().tolist()) yahan se string values lenge
    gender_options = ['All'] + sorted(df['gender'].unique().tolist()) 
    selected_gender = st.sidebar.selectbox("Select Gender", gender_options)

    # Filter the DataFrame based on user selections
    filtered_df = df[(df['age_years'] >= age_range[0]) & (df['age_years'] <= age_range[1])]

    if selected_gender != 'All':
        # Yahan filtered_df ko string values se filter kiya jayega
        filtered_df = filtered_df[filtered_df['gender'] == selected_gender]
    
    if filtered_df.empty:
        st.warning("No data found for the selected filters.")
        return

    # Draw plots if data is available
    draw_cat_plot(filtered_df)
    st.markdown("---")
    draw_heat_map(filtered_df)

if __name__ == "__main__":
    main()