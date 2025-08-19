import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_general(df):
    temp_df1 = df['year'].value_counts().reset_index().sort_values('year')
    
    st.title("Data Analysis Project")
    st.header("Exploratory Data Analysis!")
    
    st.write("Below 5 sample data from Air Quality Dataset")
    st.write(df.sample(5))
    st.write("\n" * 20)
    
    st.write("1. Data Distribution of Station Name")
    plt.figure(figsize=(15,5))
    df['station'].value_counts().plot(kind='bar');   
    plt.title('Data Distribution of Station Name', fontsize=30, pad=20)
    plt.xlabel('Station Name')
    plt.ylabel('Number of Recorded Data')
    st.pyplot(plt)
    st.info("From the Visualization above, it is \
        clear that Shunyi Station has the least number of data \
        records. While Nongzhanguan Station has the highest number \
        of data records.")
    st.write("\n" * 20)
    
    st.write("2. Data Distribution of the Year Data")
    plt.figure(figsize=(15,5))
    plt.bar(temp_df1['year'], temp_df1['count']) 
    plt.plot(temp_df1['year'], temp_df1['count'], linewidth=2, color='red', marker='o', markersize=5)
    plt.title('Data Distribution of the Year Data', fontsize=30, pad=20)
    plt.xlabel('Year')
    plt.ylabel('Number of Recorded Data')
    st.pyplot(plt)
    st.info("From the Visualization above, data \
        recording has increased from 2013 to 2015. Then, data recording \
        stable until 2016 and decreased significantly in 2017.")
    st.write("\n" * 20)
    
    st.write("3. Wind Direction Ratio")
    plt.figure(figsize=(5,5))
    df['wd'].value_counts().plot(kind='bar')
    plt.title('The Distribution of Wind Directions')
    plt.ylabel('Number of Recorded Data')
    plt.xlabel('Wind Direction')
    st.pyplot(plt)
    st.info("In the 5-year period, the wind blowing from the NorthEast \
        is the most frequent wind.")
    st.write("\n" * 20)