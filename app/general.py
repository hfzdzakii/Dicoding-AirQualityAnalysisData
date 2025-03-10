import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_general(df):
    temp_df1 = df['year'].value_counts().reset_index().sort_values('year')
    temp_df2 = df['wd'].value_counts().reset_index().sort_values('wd')
    explode = [0 for _ in range(16)]
    explode[4] = 0.3
    
    st.title("Proyek Analisis Data")
    st.header("Exploratory Data Analysis!")
    
    st.write("Berikut adalah 5 sample data dari Air Quality Dataset")
    st.write(df.sample(5))
    st.write("\n" * 20)
    
    st.write("1. Persebaran Data Nama Stasiun")
    plt.figure(figsize=(15,5))
    df['station'].value_counts().plot(kind='bar');    # Persebaran data station
    plt.title('Persebaran Data Nama Stasiun')
    plt.xlabel('Nama Stasiun')
    plt.ylabel('Jumlah Data Tercatat')
    st.pyplot(plt)
    st.info("Dari Persebaran Data Nama Stasiun, terlihat lebih jelas \
        Stasiun Shunyi memiliki jumlah catatan data paling sedikit. \
        Sedangkan Stasiun Nongzhanguan memiliki jumlah catatan data \
        paling banyak")
    st.write("\n" * 20)
    
    st.write("2. Persebaran Tahun dicatatnya Data")
    plt.figure(figsize=(15,5))
    plt.bar(temp_df1['year'], temp_df1['count']) 
    plt.plot(temp_df1['year'], temp_df1['count'], linewidth=2, color='red', marker='o', markersize=5)
    plt.title('Persebaran Data Tahun Dicatatnya Data')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Data Tercatat')
    st.pyplot(plt)
    st.info("Dari Visualisasi Persebaran Data Tahun, pencatatan data \
        mengalami kenaikan dari tahun 2013 hingga 2015. Lalu, \
        pencatatan data mengalami penurunan pada pada tahun 2016 \
        dan menurun signifikan pada tahun 2017")
    st.write("\n" * 20)
    
    st.write("3. Rasio Arah Datangnya Angin")
    plt.figure(figsize=(5,5))
    plt.pie(temp_df2['count'], labels=temp_df2['wd'], autopct='%1.1f%%', pctdistance=0.8, startangle=90, explode=explode)
    plt.title('Rasio Arah Datangnya Angin')
    st.pyplot(plt)
    st.info("Dalam kurun waktu 5 tahun, Angin yang berhembus dari Timur \
        Laut (North-East) adalah angin yang paling sering berhembus")
    st.write("\n" * 20)