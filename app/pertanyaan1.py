import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_pertanyaan1(df: pd.DataFrame, namaStasiun: str = 'Changping', tahun: int= 2014):
    st.title("Proyek Analisis Data")
    st.header(f"Bagaimana perubahan rata-rata polutan setiap bulan di tahun {tahun} pada Stasiun {namaStasiun}?")
    
    group_df = df.groupby(by=['station','year','month']).agg({
        'PM2.5' : 'mean',
        'PM10' : 'mean',
        'SO2' : 'mean',
        'NO2' : 'mean',
        'O3' : 'mean'
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
    colors = sns.color_palette("tab10", 6)
    
    st.write("Visualisasi :")
    plt.figure(figsize=(10,5))
    for ii, i in enumerate(res_df.columns):
        plt.plot(res_df.index.map(monthEncoder), res_df[i], label=i, linewidth=2, color=colors[ii], marker='o', markersize=5)
        plt.xticks(rotation=45)
    plt.title(f'Visualisasi Perubahan Polutan Sepanjang Tahun \n di Stasiun {namaStasiun} pada Tahun {tahun}', fontsize=20, pad=20)
    plt.xlabel('Bulan')
    plt.ylabel('Kuantitas Polutan')
    plt.legend()
    st.pyplot(plt)
    st.info(f"Di Stasiun {namaStasiun}, sepanjang tahun {tahun} terlihat \
        visualisasi perubahan polutan sesuai gambar diatas.")