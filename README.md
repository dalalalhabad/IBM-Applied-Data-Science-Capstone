# IBM Applied Data Science Capstone

## SpaceX Falcon 9 First Stage Landing Prediction

**Author:** Dalal F. S. A. Alhabad

This repository contains my completed IBM Applied Data Science Capstone project. The objective of this project is to predict whether the first stage of a SpaceX Falcon 9 rocket will successfully land using historical launch data and machine learning techniques.

---

# Project Overview

The Falcon 9 rocket is partially reusable. Successfully recovering the first-stage booster significantly reduces launch costs.

This project applies an end-to-end data science workflow to analyse historical Falcon 9 launches, identify factors associated with successful landings, and develop predictive machine learning models.

---

# Project Workflow

The project follows the complete data science pipeline:

1. Data Collection using the SpaceX REST API
2. Data Collection using Web Scraping (Wikipedia)
3. Data Wrangling and Cleaning
4. Exploratory Data Analysis (EDA)
5. SQL Analysis
6. Interactive Visual Analytics
   - Folium Maps
   - Plotly Dash Dashboard
7. Predictive Analysis using Machine Learning
8. Final Presentation

---

# Repository Structure

```
IBM-Applied-Data-Science-Capstone/
│
├── 01_SpaceX_Data_Collection_API.ipynb
├── 02_SpaceX_Web_Scraping.ipynb
├── 03_SpaceX_Data_Wrangling.ipynb
├── 04_SpaceX_EDA_Data_Visualization.ipynb
├── 05_SpaceX_EDA_SQL.ipynb
├── 06_SpaceX_Folium_Launch_Site_Analysis.ipynb
├── SpaceX-Machine-Learning-Prediction-Part-5.ipynb
│
├── spacex_dash_app.py
├── spacex_launch_dash.csv
│
├── Data Science Capstone Project Report.pdf
├── Data Science Capstone Project Report.pptx
│
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Dash
- Folium
- BeautifulSoup
- Requests
- SQLite
- Scikit-learn
- Jupyter Notebook

---

# Machine Learning Models

The following supervised learning algorithms were evaluated:

- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- K-Nearest Neighbours (KNN)

Models were optimised using GridSearchCV and evaluated using test accuracy and confusion matrices.

---

# Key Findings

- Landing success has improved considerably over time.
- Launch site influences landing success.
- Payload mass affects landing probability.
- Orbit type is associated with mission success.
- Machine learning models successfully predicted landing outcomes with high accuracy.

---

# Interactive Dashboard

The Plotly Dash application allows users to:

- Select launch sites
- Filter payload ranges
- View launch success rates
- Explore payload versus landing outcome relationships

---

# Folium Interactive Map

The Folium application provides:

- Launch site locations
- Successful and unsuccessful launch markers
- Proximity analysis
- Geographic visualisation of SpaceX launch sites

---

# Data Sources

- SpaceX REST API
  https://github.com/r-spacex/SpaceX-API

- Wikipedia
  https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches

---

# Course

IBM Applied Data Science Capstone

Coursera | IBM Skills Network

---

# Author

**Dalal F. S. A. Alhabad**

PhD Candidate in Bioinformatics  
Department of Computer Science and Information Technology  
La Trobe University, Melbourne, Australia

LinkedIn:
https://www.linkedin.com/in/dalalalhabad

GitHub:
https://github.com/dalalalhabad

---

# Acknowledgements

This project was completed as part of the IBM Applied Data Science Professional Certificate on Coursera.

Special thanks to IBM Skills Network for providing the project datasets, learning materials, and capstone framework.# IBM-Applied-Data-Science-Capstone
IBM Applied Data Science Capstone- SpaceX Falcon 9 First Stage Landing Prediction
