# athlete-fatigue-ml

## Overview
This project explores how machine learning can be used to analyze fitness-tracking data
and predict athlete performance indicators such as workload, fatigue, or potential risk
factors.

The goal of this project is not only to build predictive models, but to demonstrate a
clear, well-structured ML workflow and strong reasoning behind each step of the process.

This repository is intended as a personal project to showcase applied machine learning,
data analysis, and software engineering best practices.

---

## Motivation
As a computer science student specializing in Artificial Intelligence and an active
athlete, I am interested in how data collected during training sessions can be turned
into meaningful, actionable insights.

Wearables and fitness trackers generate large volumes of data, yet much of it is
underutilized. This project aims to explore how features such as heart rate, sleep,
activity duration, and steps can be leveraged to better understand athletic performance.

---

## Dataset
- **Type:** Synthetic fitness tracker dataset
- **Records:** 200
- **Features:** 12

### Key Features
- Age
- Gender
- Activity type
- Duration (minutes)
- Calories burned
- Average heart rate
- Steps
- Sleep hours
- Weight

The dataset is used as a stand-in for real-world wearable data and allows experimentation
with realistic preprocessing and modeling decisions.

---

## Project Structure

src/
├── 1_load_and_inspect.py # Load data and inspect structure
├── 2_clean_and_preprocess.py # Data cleaning and preprocessing
├── 3_eda.py # Exploratory data analysis
├── 4_feature_engineering.py # Feature creation and transformation
├── 5_model_training.py # Model training and experimentation
└── 6_evaluation.py # Model evaluation and metrics


---

## Approach
1. Load and inspect the raw dataset
2. Clean missing, inconsistent, or noisy values
3. Perform exploratory data analysis to identify trends and relationships
4. Engineer features relevant to athletic performance
5. Train baseline machine learning models
6. Evaluate models using appropriate metrics
7. Iterate and improve based on results

---

## Models
- Linear Regression (baseline)
- Random Forest (planned)
- Gradient Boosting (planned)

---

## Evaluation
Model performance is evaluated using metrics such as:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

Further evaluation techniques such as cross-validation will be added as the project
progresses.
