# 📈 Stock Market Risk Analysis

### Financial data analysis using Python, PCA, Factor Analysis, and clustering methods to identify market risk patterns and support portfolio decision-making.

---

## 🚀 Project Overview

This project analyses monthly NYSE stock returns to identify common market risk patterns, industry-level systematic risk, and stocks that move closely with the S&P500 market return.

The analysis applies high-dimensional data techniques including:

- Principal Component Analysis
- Factor Analysis
- K-means Clustering
- Hierarchical Clustering
- Gaussian Mixture Model
- Multidimensional Scaling
- Correlation Analysis

The project is designed as a portfolio-style data analytics project to demonstrate practical skills in financial data analysis, risk modelling, dimensionality reduction, clustering, and Python-based data storytelling.

---

## 🎯 Project Objectives

The main objectives of this project are to:

- Identify common movement patterns across 92 NYSE stocks
- Compare the first principal component with the S&P500 market return
- Measure industry-level systematic risk using Factor Analysis
- Recommend five stocks that move closely with the market
- Validate stock behaviour using clustering methods
- Visualise stock similarity using MDS
- Present results through clean outputs, figures, and summary tables

---

## 📊 Dataset

The project uses two datasets:

| Dataset | Description |
|---|---|
| `Market.csv` | S&P500 monthly market return data |
| `SampleI.csv` | Monthly return data for 92 NYSE stocks |

The dataset contains:

- 180 monthly observations
- 92 stock-return variables
- Sample period: January 2005 to December 2019

Each stock identifier begins with an industry code.

| Code | Industry |
|---|---|
| B | Mining |
| C | Construction |
| D | Manufacturing |
| E | Transportation and Public Utilities |
| F | Wholesale Trade |
| G | Retail Trade |
| H | Finance, Insurance and Real Estate |
| I | Services |

---

## 🧠 Methods Used

| Method | Purpose |
|---|---|
| Exploratory Data Analysis | Understand return behaviour, volatility, and outliers |
| PCA | Reduce 92 stock variables into key components |
| Factor Analysis | Estimate common factors and systematic risk |
| K-means Clustering | Group stocks with similar return behaviour |
| Hierarchical Clustering | Validate stock grouping using tree-based clustering |
| Gaussian Mixture Model | Apply probabilistic clustering |
| MDS | Visualise stock similarity in two dimensions |
| Correlation Analysis | Measure stock-market and stock-to-stock co-movement |

---

## 🔍 Key Findings

- PC1 explains the largest share of stock-return variation.
- PC1 has a strong positive relationship with the S&P500 market return.
- Finance, Insurance and Real Estate shows the highest average communality.
- This indicates that Industry H has the strongest systematic risk exposure.
- The top five recommended stocks all belong to Industry H.
- K-means and GMM produce consistent clustering results.
- MDS visualisation supports the similarity of the recommended stocks.

---

## ✅ Recommended Stocks

The final stock recommendation is based on:

- Market correlation
- PC1 loading
- Factor 1 loading
- Communality

The recommended stocks are selected because they show strong market co-movement and high exposure to common risk factors.

The final recommendation table is saved here:

```text
outputs/tables/top_five_recommended_stocks.csv

## Repository Structure

Stock-Market-Risk-Analysis/
│
├── data/
│   ├── Market.csv
│   └── SampleI.csv
│
├── notebooks/
│   └── 01_stock_market_risk_analysis.ipynb
│
├── outputs/
│   ├── figures/
│   └── tables/
│
├── report/
│
├── src/
│
├── README.md
└── requirements.txt