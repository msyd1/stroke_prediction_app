# Stroke Prediction App Project 
### Project Description
This project is made for the purpose of  predicting whether there is risk of the stroke.

### Installations
Main file is a Jupyter notebook;

To clone this repository:
```
$ git clone https://github.com/msyd1/stroke_prediction_app.git
```
To install dependencies:
```
$ pip install -r requirements.txt
```
Or install requred libraries:

- pandas
- numpy
- pickle
- sklearn
- plotly
- streamlit

### Overview

**Data Analysis**

Exploring the data we are working with for the project. 

**Data Preprocessing**

Cleaning and transformation the dataset.

**Training Models**

Implementing machine learning mechanisms to make prediction. 

**Deploying the app**

Creating script for the application.

### Instructions:

**Web app**: 

https://stroke-prediction-app-w.herokuapp.com/

To see how the project works *at your local machine*:
Run the following command in the project directory:
```
streamlit run run.py
```
And go to http://localhost:8501.

### Project Structure
```
- healthcare-dataset-stroke-data.csv    # data to process
- model.p                               # saved model
- run.py                                # file that runs the app 
- Stroke Prediction.ipynb               # Jupiter file
- Procfile                              # Heroku deployment file
- setup.sh                              # file for starting the application
- requirements.txt
- README.md
```

### Acknowledgements
Kaggle for providing the dataset.