# IBM Applied Data Science Capstone

## 🚀 SpaceX Falcon 9 First Stage Landing Prediction

**Author:** Dalal F. S. A. Alhabad

---

## Project Description

This repository contains my completed **IBM Applied Data Science Capstone**, the final project of the **IBM Data Science Professional Certificate** offered through **Coursera**.

The objective of this project is to develop a predictive machine learning model capable of determining whether the **SpaceX Falcon 9 first-stage booster** will successfully land following launch. Accurate prediction of landing success is important because Falcon 9 is a partially reusable launch vehicle, and successful booster recovery significantly reduces the cost of space missions.

The project follows a complete end-to-end data science workflow, beginning with data acquisition from the **SpaceX REST API** and **Wikipedia**, followed by data cleaning, exploratory data analysis (EDA), SQL analysis, interactive visualisation, and predictive modelling. Multiple supervised machine learning algorithms were trained and evaluated to identify the factors that most strongly influence landing success.

Interactive dashboards were developed using **Plotly Dash**, while **Folium** was used to visualise launch sites geographically. Together, these analyses demonstrate how data science techniques can be applied to solve real-world aerospace problems.

This project demonstrates practical experience in:

* Data Collection using APIs and Web Scraping
* Data Wrangling and Feature Engineering
* Exploratory Data Analysis (EDA)
* SQL Data Analysis
* Interactive Data Visualisation
* Machine Learning Classification
* Model Evaluation and Performance Comparison
* Scientific Reporting and Data Storytelling

---

## Project Overview


The Falcon 9 rocket is partially reusable. Successfully recovering the first-stage booster significantly reduces launch costs.

This project applies an end-to-end data science workflow to analyse historical Falcon 9 launches, identify factors associated with successful landings, and develop predictive machine learning models.

---

## Project Workflow

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

## Repository Structure

```
IBM-Applied-Data-Science-Capstone/
│
├── 01_SpaceX_Data_Collection_API.ipynb
├── 02_SpaceX_Web_Scraping.ipynb
├── 03_SpaceX_Data_Wrangling.ipynb
├── 04_SpaceX_EDA_Data_Visualization.ipynb
├── 05_SpaceX_EDA_SQL.ipynb
├── 06_SpaceX_Folium_Launch_Site_Analysis.ipynb
├── 07_SpaceX-Machine-Learning-Prediction.ipynb
|── 08_Spacex_Dash_Application.py
│
|
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

## Machine Learning Models

The following supervised learning algorithms were evaluated:

- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- K-Nearest Neighbours (KNN)

Models were optimised using GridSearchCV and evaluated using test accuracy and confusion matrices.

---

## Key Findings

- Landing success has improved considerably over time.
- Launch site influences landing success.
- Payload mass affects landing probability.
- Orbit type is associated with mission success.
- Machine learning models successfully predicted landing outcomes with high accuracy.

---

## Interactive Dashboard

The Plotly Dash application allows users to:

- Select launch sites
- Filter payload ranges
- View launch success rates
- Explore payload versus landing outcome relationships

---

## Folium Interactive Map

The Folium application provides:

- Launch site locations
- Successful and unsuccessful launch markers
- Proximity analysis
- Geographic visualisation of SpaceX launch sites

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/dalalalhabad/IBM-Applied-Data-Science-Capstone.git
cd IBM-Applied-Data-Science-Capstone


---

## Data Sources

- SpaceX REST API
  https://github.com/r-spacex/SpaceX-API

- Wikipedia
  https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches

---

## Course

IBM Applied Data Science Capstone

Coursera | IBM Skills Network

---

## Author

**Dalal F. S. A. Alhabad**

PhD Candidate in Bioinformatics  
Department of Computer Science and Information Technology  
La Trobe University, Melbourne, Australia

LinkedIn:
https://www.linkedin.com/in/dalalalhabad

GitHub:
https://github.com/dalalalhabad

---

## Acknowledgements

This project was completed as part of the IBM Applied Data Science Professional Certificate on Coursera.

Special thanks to IBM Skills Network for providing the project datasets, learning materials, and capstone framework.