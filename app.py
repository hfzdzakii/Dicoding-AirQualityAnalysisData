import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append("app")
sys.path.append("dataset")
from general import show_general
from analysis1 import show_analysis1
from analysis2 import show_analysis2
from analysis3 import show_analysis3
from analysis4 import show_analysis4

def show_list_station(df):
    station = st.sidebar.selectbox("Choose Station Name", [stationName for stationName in df['station'].unique()])
    return station
    
def show_list_year(df):
    year = st.sidebar.selectbox("Choose Year Data", [theYear for theYear in df['year'].unique()])
    return year

def show_list_pollutant(df):
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    pollutant = st.sidebar.selectbox("Choose Pollutant", [pol for pol in pollutants])
    return pollutant


df = pd.read_csv('./dataset/cleanBinnedMainDataset.csv')

st.sidebar.title("Navigation Sidebar")
page = st.sidebar.selectbox("Choose Pages", ["General", "Analysis 1", "Analysis 2", "Analysis 3", "Analysis 4"])

station = show_list_station(df) if page != "General" else None
year = show_list_year(df) if page != "General" else None
pollutant = show_list_pollutant(df) if page == "Analysis 3" else None

# Page content based on selection
if page == "General":
    show_general(df)
elif page == "Analysis 1":
    show_analysis1(df, station, year)
elif page == "Analysis 2":
    show_analysis2(df, station, year)
elif page == "Analysis 3":
    show_analysis3(df, station, year, pollutant)
elif page == "Analysis 4":
    show_analysis4(df, station, year)

