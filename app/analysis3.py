import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_analysis3(df: pd.DataFrame, stationName: str = 'Changping', year: int= 2014, pollutant: str= 'PM2.5'):
    st.title("Data Analysis Project")
    st.header(f"How does wind direction affect pollutants at Station {stationName} in year {year}?")
    
    wind_degrees_dict = {
        'N': 0, 'NNE': 22.5, 'NE': 45, 'ENE': 67.5, 'E': 90, 'ESE': 112.5, 'SE': 135, 'SSE': 157.5,
        'S': 180, 'SSW': 202.5, 'SW': 225, 'WSW': 247.5, 'W': 270, 'WNW': 292.5, 'NW': 315, 'NNW': 337.5
    }

    desired_order = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']

    group_df = df.groupby(by=['station','year', 'wd']).agg({
        'PM2.5' : 'mean',
        'PM10' : 'mean',
        'SO2' : 'mean',
        'NO2' : 'mean',
        'CO' : 'mean',
        'O3' : 'mean'
    })
    
    st.write("Here are 5 sample data from the Air Quality Dataset \
        that have been categorized by Station Name, year and \
        Wind Direction")
    st.write(group_df.sample(5))
    st.write("\n" * 20)

    st.write("Visualization :")
    series = group_df.loc[(stationName, year)][pollutant]
    pm25_concentrations = series[desired_order].values
    wind_directions = series.index.map(wind_degrees_dict)
    wind_directions_rad = np.deg2rad(wind_directions)
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    bars = ax.bar(wind_directions_rad, pm25_concentrations, width=np.pi/8, color=plt.cm.viridis(pm25_concentrations / 100))
    ax.set_title(f"Visualization of Wind Direction \n with Pollutant {pollutant} at Station {stationName} in Year {year}", fontsize=20, pad=20)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    st.pyplot(plt)
    st.info(f"0&#176; signifies North. 90&#176; signifies East. 180&#176; \
        signifies South. 270&#170; signifies West. The longer the diagram \
        the more often the wind blows from that direction.")
    st.info(f"It can be seen that particles of {pollutant} at **{stationName}**, \
        in the year **{year}** were on average carried more often by winds \
        coming from the corresponding direction in the visualization.")