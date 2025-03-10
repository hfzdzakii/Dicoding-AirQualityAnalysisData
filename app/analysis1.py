import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_analysis1(df: pd.DataFrame, stationName: str = 'Changping', year: int= 2014):
    st.title("Data Analysis Project")
    st.header(f"How the average monthly pollutant change in {year} at {stationName} Station?")
    
    group_df = df.groupby(by=['station','year','month']).agg({
        'PM2.5' : 'mean',
        'PM10' : 'mean',
        'SO2' : 'mean',
        'NO2' : 'mean',
        'O3' : 'mean'
    })

    monthEncoder = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
    }
    
    st.write("Here are 5 sample data from the Air Quality Dataset \
        that have been grouped by Station Name, Year and \
        Month")
    st.write(group_df.sample(5))
    st.write("\n" * 20)
    
    res_df = group_df.loc[(stationName, year)]
    colors = sns.color_palette("tab10", 6)
    
    st.write("Visualization :")
    plt.figure(figsize=(10,5))
    for ii, i in enumerate(res_df.columns):
        plt.plot(res_df.index.map(monthEncoder), res_df[i], label=i, linewidth=2, color=colors[ii], marker='o', markersize=5)
        plt.xticks(rotation=45)
    plt.title(f'Visualization of Pollutant Changes Throughout the Year \n at Station {stationName} in the Year {year}', fontsize=20, pad=20)
    plt.xlabel('Month')
    plt.ylabel('Quantity of Pollutant')
    plt.legend()
    st.pyplot(plt)
    st.info(f"At Station {stationName}, during the year {year}, we can see \
        visualization of pollutant changes as shown above.")