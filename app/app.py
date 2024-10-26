import streamlit as st
from general import show_general
from pertanyaan1 import show_pertanyaan1
from pertanyaan2 import show_pertanyaan2
from pertanyaan3 import show_pertanyaan3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_list_stasiun(df):
    stasiun = st.sidebar.selectbox("Pilih Nama Stasiun", [namaStasiun for namaStasiun in df['station'].unique()])
    return stasiun
    
def show_list_tahun(df):
    tahun = st.sidebar.selectbox("Pilih Tahun Data", [tahunnya for tahunnya in df['year'].unique()])
    return tahun

def show_list_polutan(df):
    polutans = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    polutan = st.sidebar.selectbox("Pilih Polutan", [pol for pol in polutans])
    return polutan


df = pd.read_csv('dataset\cleanMainDataset.csv')

st.sidebar.title("Navigation Sidebar")
page = st.sidebar.selectbox("Pilih Halaman", ["General", "Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3"])

stasiun = show_list_stasiun(df) if page != "General" else None
tahun = show_list_tahun(df) if page != "General" else None
polutan = show_list_polutan(df) if page == "Pertanyaan 3" else None

# Page content based on selection
if page == "General":
    show_general(df)
elif page == "Pertanyaan 1":
    show_pertanyaan1(df, stasiun, tahun)
elif page == "Pertanyaan 2":
    show_pertanyaan2(df, stasiun, tahun)
elif page == "Pertanyaan 3":
    show_pertanyaan3(df, stasiun, tahun, polutan)

