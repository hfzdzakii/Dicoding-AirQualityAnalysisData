import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_pertanyaan3(df: pd.DataFrame, namaStasiun: str = 'Changping', tahun: int= 2014, polutan: str= 'PM2.5'):
    st.title("Proyek Analisis Data")
    st.header(f"Bagaimana pengaruh arah mata angin dengan polutan di stasiun {namaStasiun} pada tahun {tahun}?")
    
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
    
    st.write("Berikut adalah 5 sample data dari Air Quality Dataset \
        yang telah dikelompokkan berdasarkan Nama Stasiun, Tahun dan \
        Arah Mata Angin")
    st.write(group_df.sample(5))
    st.write("\n" * 20)

    st.write("Visualisasi :")
    series = group_df.loc[(namaStasiun, tahun)][polutan]
    pm25_concentrations = series[desired_order].values
    wind_directions = series.index.map(wind_degrees_dict)
    wind_directions_rad = np.deg2rad(wind_directions)
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    bars = ax.bar(wind_directions_rad, pm25_concentrations, width=np.pi/8, color=plt.cm.viridis(pm25_concentrations / 100))
    ax.set_title(f"Visualisasi Arah Mata Angin Zat Polusi PM2.5 \n di Stasiun {namaStasiun} pada Tahun {tahun}", fontsize=20, pad=20)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    st.pyplot(plt)
    st.info(f"0&#176; menandakan Utara. 90&#176; menandakan Timur. 180&#176; \
        menandakan Selatan. 270&#170; menandakan Barat. Semakin panjang diagram \
        semakin sering angin yang berhembus dari arah yang bersangkutan.")
    st.info(f"Terlihat kalau partikel {polutan} di **{namaStasiun}**, \
        pada tahun **{tahun}** rata-rata lebih sering terbawa oleh angin \
        yang berasal dari arah sesuai pada visualisasi.")