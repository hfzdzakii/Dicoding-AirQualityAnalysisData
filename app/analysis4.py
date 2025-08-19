import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_analysis4(df: pd.DataFrame, stationName: str = 'Changping', year: int= 2014):
    st.title("Data Analysis Project")
    st.header(f"How does average pollutant concentration by time of day at Station {stationName} in {year}?")
    
    group_df = df.groupby(by=['station','year', 'time_of_day']).agg({
        'PM2.5' : 'mean',
        'PM10' : 'mean',    # Using manual grouping method by station, year, and wind direction 
        'SO2' : 'mean',    
        'NO2' : 'mean',
        'CO' : 'mean',
        'O3' : 'mean'
    })

    st.write("Here are 5 sample data from the Air Quality Dataset \
        that have been grouped by Station Name, Year and \
        Time of Day")
    st.write(group_df.sample(5))
    st.write("\n" * 20)

    res_df = group_df.loc[(stationName, year)]
    df_T = res_df.T  
    
    df_norm = df_T.sub(df_T.min(axis=1), axis=0)
    df_norm = df_norm.div(df_T.max(axis=1) - df_T.min(axis=1), axis=0)
    
    st.write("Visualization :")
    plt.figure(figsize=(8,5))
    sns.heatmap(df_norm, 
                annot=df_T, fmt=".1f", cmap="YlOrRd", 
                cbar_kws={'label': 'Relative Level (per pollutant)'})
    plt.title(f"Average Pollutant Concentration by Time of Day \n at {stationName} Station in {year}")
    plt.xlabel("Time of Day")
    plt.ylabel("Pollutant")
    st.pyplot(plt)
    st.info(f"It can be seen from the visualization, at Station {stationName} during the \
            {year}, we can see the pollutant distribution changes as shown above.")
