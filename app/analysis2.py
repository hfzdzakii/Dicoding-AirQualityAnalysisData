import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_analysis2(df: pd.DataFrame, stationName: str = 'Changping', year: int= 2014):
    st.title("Data Analysis Project")
    st.header(f"What is the correlation between temperature change and CO pollutant at Station {stationName} in {year}?")
    
    group_df = df.groupby(by=['station','year','month']).agg({
        'CO' : 'mean',
        'TEMP' : 'mean'
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
    fig, ax1 = plt.subplots(figsize=(10, 5))

    st.write("Visualization :")
    ax1.plot(res_df.index.map(monthEncoder), res_df['CO'], color='b', marker='o', label='CO')
    ax1.set_ylabel('Concentration of CO', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2 = ax1.twinx()
    ax2.set_ylabel('Air Temperature', color='r')
    ax2.plot(res_df.index.map(monthEncoder), res_df['TEMP'], color='r', marker='s', label='Temperatur')
    ax2.tick_params(axis='y', labelcolor='r')
    ax1.set_xlabel('Month')
    plt.title(f'Dual Axes Line Plot for CO Pollutant and Air Temperature \n at Station {stationName} in the Year {year}', fontsize=20, pad=20)
    fig.tight_layout()
    st.pyplot(plt)
    st.info(f"It can be seen from the visualization, at Station {stationName} during the \
            {year} the trend of CO and air temperature has a pattern that is \
            always reverse. When the air temperature is high, the CO \
            levels in the air are low. Meanwhile, when the air temperature level is low, the CO \
            then the CO levels in the air are high")
