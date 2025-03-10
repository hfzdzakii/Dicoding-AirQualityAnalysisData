# Dicoding Final Project - Data Analysis Project

- Created by : Muhammad Hafizh (hfzdzakii) Dzaki
- Last Edited On : March 2025

This project was created to fulfill the completion of the **Learning Data Analysis with Python** course in the **Data Scientist** learning path on [Dicoding](https://www.dicoding.com).

**Data Scientist** learning path can be found [here](https://www.dicoding.com/learningpaths/60)

**Learning Data Analysis with Python** course can be found [here](https://www.dicoding.com/academies/555-belajar-analisis-data-dengan-python)

Dataset that used in this project can be found [here](https://github.com/marceloreis/HTI/tree/master)

## How to Run the Project

### Setup Environment - Anaconda / Miniconda
```
$ conda create --name main-ds python=3.12.9
$ conda activate main-ds
$ git clone https://github.com/hfzdzakii/Dicoding-DataAnalysisProject.git
$ cd Dicoding-DataAnalysisProject
$ pip install -r requirements.txt
```

### Run steamlit app
```
$ streamlit run app.py
```

Tested on python 3.12.9

## Or, You Can See the Deployed Project Here

Streamlit Cloud Community link : [Here](https://hqy32wysstacnedhsridhw.streamlit.app)

Feel free to wake up the project if it deactivated automatically due to inactivity

## Or, You Can Pull The Docker Image
```
$ docker pull hfzdzakii/streamlit-analysis-data:latest
$ docker run --name streamlit-app -p 8501:8501 hfzdzakii/streamlit-analysis-data:latest
```

Type `http://localhost:8501` in your browser to open Streamlit App

To stop Streamlit server, type `Ctr + C` or `Command + C` in the terminal
