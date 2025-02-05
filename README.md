# Titanic-ETL-Pipeline

This repository demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built with Python using the Titanic - Machine Learning from Disaster dataset from Kaggle. The project showcases essential data engineering skills by extracting raw data, cleaning and transforming it , and loading the cleaned data into a SQLite database.

## Overview

The Titanic dataset is split into three primary files:
- **train.csv**: Contains the training data with the `Survived` column
- **test.csv**: Contains the test data (without the `Survived` column) for predictions.
- **gender_submission.csv**: Contains the predicted values for the test data

In this project, we focus on processing the training data by:
- Extracting the data from train CSV file.
- Transforming the data through cleaning and feature engineering (creating a `FamilySize` feature).
- Loading the cleaned data into a SQLite database for further analysis or integration.


## Requirements

- Python 3
- Pandas
- SQLite3
- Logging

## How to Run

To run the ETL pipeline from the command line, navigate to the project directory and execute:
python titanic_etl.py

This script will:
Extract the data from train.csv.
Transform the data by cleaning missing values, dropping unnecessary columns, and creating new features such as 'Family Size'.
Load the transformed data into a SQLite database (titanic.db) under the table name train_cleaned.

