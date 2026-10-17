<img width="1272" height="875" alt="Screenshot 2026-10-17 215801" src="https://github.com/user-attachments/assets/09c9fde3-d0b8-4a63-981a-58a53276b081" />
<img width="1272" height="875" alt="Screenshot 2026-10-17 215801" src="https://github.com/user-attachments/assets/759d368b-9280-437e-9723-2f69f9bc6083" />
# CoinPlus-AI
cryptocurrency price estimation. CoinPulse AI is a machine learning project that predicts Bitcoin’s closing price using USDT and BNB market data. Built with Python, Scikit-learn, and Streamlit, it uses Random Forest Regression and an interactive web interface.

 CoinPulse AI

### Cryptocurrency Market Analytics & Bitcoin Price Prediction System

CoinPulse AI is a machine-learning project designed to analyze historical cryptocurrency market data and estimate Bitcoin's closing price using selected market indicators from Tether (USDT) and Binance Coin (BNB). The project combines data analysis, feature selection, regression modelling, and an interactive Streamlit web application.

## 📌 Table of Contents
- Overview
- Project Objectives
- Problem Statement
- Key Features
- Technologies Used
- Dataset Description
- Machine Learning Workflow
- Model and Evaluation
- Project Structure
- Installation and Setup
- Running the Application
- How to Use
- Limitations
- Future Improvements
- Author

## 📖 Project Overview

Cryptocurrency prices fluctuate based on market activity, trading volume, and other factors. CoinPulse AI explores historical cryptocurrency data and demonstrates how machine-learning regression can estimate Bitcoin's closing price from selected market features.

The project includes a Jupyter Notebook for data exploration and model development, a saved Random Forest regression model, and a Streamlit interface where users can enter USDT and BNB market values and obtain an estimated BTC closing price in USD.

**Project type:** Machine Learning / Data Science

**Application:** Interactive cryptocurrency price estimation

**Prediction target:** Bitcoin closing price (USD)

## 🎯 Project Objectives

- Collect and analyze historical cryptocurrency market data.
- Explore price movements, trading volumes, distributions, and correlations.
- Select relevant input features for regression modelling.
- Train and compare machine-learning regression algorithms.
- Evaluate model performance using Mean Squared Error (MSE) and R-squared (R²).
- Integrate the trained model into a Streamlit web application.
- Provide a simple interface for entering market data and viewing predictions.

## ❓ Problem Statement

Understanding cryptocurrency market movements is challenging because prices are volatile and influenced by multiple variables. This project investigates whether selected USDT and BNB closing prices and trading volumes can be used to estimate Bitcoin's closing price.

The objective is to demonstrate an end-to-end machine-learning workflow, from historical data analysis and feature selection to model development and interactive application deployment. The resulting estimate is for educational purposes and should not be considered a guaranteed future market price.

## ✨ Key Features

- Historical cryptocurrency data collection using yfinance.
- Exploratory Data Analysis (EDA) of prices and trading volumes.
- Visualization of trends, distributions, and correlations.
- Feature selection using SelectKBest.
- Regression model comparison using Scikit-learn.
- Random Forest Regressor for price estimation.
- Saved model integration using Pickle.
- Interactive Streamlit web interface.
- Separate USDT and BNB market input sections.
- Custom CSS styling with a dark theme and responsive layout.
- Formatted display of the estimated Bitcoin closing price.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| yfinance | Historical cryptocurrency market data |
| Matplotlib | Data visualization |
| Seaborn | Statistical plots and correlation analysis |
| Scikit-learn | Machine-learning models and evaluation |
| Random Forest Regressor | Regression-based price estimation |
| SelectKBest | Feature selection |
| MinMaxScaler | Feature scaling during model development |
| Streamlit | Interactive web application |
| HTML and CSS | Application presentation and styling |
| Pickle | Saving and loading serialized Python objects |
| Jupyter Notebook | Data exploration and model development |

## 📊 Dataset Description

The Jupyter Notebook uses historical market data retrieved through yfinance for the following cryptocurrencies:

- Bitcoin (BTC)
- Ethereum (ETH)
- Tether (USDT)
- Binance Coin (BNB)

The notebook retrieves a historical period of approximately five years. The exact number of usable rows depends on the data returned and the preprocessing performed.

### Input Features

| Feature | Description |
|---|---|
| `USDT_Close` | Tether closing price |
| `USDT_Volume` | Tether trading volume |
| `BNB_Close` | Binance Coin closing price |
| `BNB_Volume` | Binance Coin trading volume |

### Target Variable

`BTC_Close` — Bitcoin closing price, measured in USD.

**Note:** The Streamlit interface accepts the four selected features as manual inputs. It does not currently fetch live market data automatically.

## 🔄 Machine Learning Workflow

1. **Data collection:** Retrieve historical cryptocurrency market data.
2. **Data preparation:** Organize relevant closing prices and trading volumes for analysis.
3. **Exploratory Data Analysis:** Examine trends, distributions, and relationships among cryptocurrencies.
4. **Feature selection:** Use SelectKBest to identify the four selected input features.
5. **Data splitting:** Split the dataset into training and testing subsets.
6. **Feature scaling:** Apply MinMaxScaler as part of the model-development workflow.
7. **Model training:** Train and compare regression algorithms.
8. **Model evaluation:** Calculate MSE and R² to compare model performance.
9. **Model saving:** Serialize the selected Random Forest model using Pickle.
10. **Application development:** Integrate the saved model into Streamlit.
11. **Prediction:** Accept USDT and BNB market inputs and display the estimated BTC closing price.

## 🤖 Model and Evaluation

The project uses a Random Forest Regressor for the saved prediction workflow. The Jupyter Notebook also compares other regression algorithms and records model evaluation results.

### Evaluation Metrics

- **Mean Squared Error (MSE):** Measures the average squared difference between actual and predicted values. Lower values are generally preferable when comparing models on the same test data.
- **R-squared (R²):** Measures how well the model explains variation in the target values relative to a baseline. A higher score generally indicates a better fit on the evaluated dataset.

The notebook contains preliminary evaluation results. These should be reproduced after ensuring that feature preprocessing is identical during training and prediction and that the test data is appropriately held out. No performance guarantee is made by this project.

## 🧑‍💻 How to Use

1. Launch the Streamlit application.
2. Enter the USDT closing price.
3. Enter the USDT trading volume.
4. Enter the BNB closing price.
5. Enter the BNB trading volume.
6. Click **Predict Bitcoin Closing Price**.
7. View the estimated Bitcoin closing price displayed by the application.

The result depends on the values entered and the trained model. It is an estimate, not a guarantee of the actual or future market price.

## ⚠️ Limitations

- Cryptocurrency markets are volatile and difficult to predict reliably.
- The current interface requires users to enter market values manually.
- Only four selected market features are used by the application.
- The model's predictions depend on the training data and preprocessing pipeline.
- Training and prediction preprocessing must be consistent. The current implementation should be checked to ensure that the saved scaler is applied correctly before relying on predictions.
- Evaluation scores from a shuffled test split do not establish future forecasting performance.
- The application is an educational project, not financial advice or an automated trading system.

 ## 🔒 Responsible Use

This project is intended for learning, experimentation, and demonstration of machine-learning concepts. Predictions may be inaccurate, especially when market conditions differ from the training data. Do not use the output as the sole basis for financial or investment decisions.

**CoinPulse AI — Turning cryptocurrency market data into machine-learning estimates.**
