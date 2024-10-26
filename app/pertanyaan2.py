import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_pertanyaan2(df: pd.DataFrame, namaStasiun: str = 'Changping', tahun: int= 2014):
    st.title("Proyek Analisis Data")
    st.header(f"Bagaimama korelasi perubahan temperatur dengan polutan CO pada Stasiun {namaStasiun} di tahun {tahun}?")
    
    group_df = df.groupby(by=['station','year','month']).agg({
        'CO' : 'mean',
        'TEMP' : 'mean'
    })

    monthEncoder = {
        1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni",
        7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }
    
    st.write("Berikut adalah 5 sample data dari Air Quality Dataset \
        yang telah dikelompokkan berdasarkan Nama Stasiun, Tahun dan \
        Bulan")
    st.write(group_df.sample(5))
    st.write("\n" * 20)

    res_df = group_df.loc[(namaStasiun, tahun)]
    fig, ax1 = plt.subplots(figsize=(10, 5))

    st.write("Visualisasi :")
    ax1.plot(res_df.index.map(monthEncoder), res_df['CO'], color='b', marker='o', label='CO')
    ax1.set_ylabel('Konsentrasi CO', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2 = ax1.twinx()
    ax2.set_ylabel('Temperatur Udara', color='r')
    ax2.plot(res_df.index.map(monthEncoder), res_df['TEMP'], color='r', marker='s', label='Temperatur')
    ax2.tick_params(axis='y', labelcolor='r')
    ax1.set_xlabel('Bulan')
    plt.title(f'Dual Axes Line Plot Kadar CO dan Temperatur Udara \n di Stasiun {namaStasiun} pada Tahun {tahun}', fontsize=20, pad=20)
    fig.tight_layout()
    st.pyplot(plt)
    st.info(f"Dapat dilihat dari visualisasi, di Stasiun {namaStasiun} selama \
            tahun {tahun} trend dari CO dan suhu udara memiliki pola yang \
            selalu terbalik. Ketika suhu udara tinggi, maka kadar CO \
            di udara rendah. Sedangkan, ketika kadar suhu udara rendah, \
            maka kadar CO di udara tinggi")
