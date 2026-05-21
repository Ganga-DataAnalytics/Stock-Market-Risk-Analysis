# Stock Market Risk Analysis - Summary Report

## Project Purpose

This project analyses monthly NYSE stock returns to identify common market risk patterns, industry-level systematic risk, and stocks that move closely with the S&P500 market return.

## Data

The analysis uses:

- S&P500 monthly market return data
- Monthly return data for 92 NYSE stocks
- Sample period: January 2005 to December 2019

## Methods Applied

The project applies:

- Exploratory Data Analysis
- Principal Component Analysis
- Factor Analysis
- K-means Clustering
- Hierarchical Clustering
- Gaussian Mixture Model
- Multidimensional Scaling
- Correlation Analysis

## Main Findings

PC1 explains the largest share of variation among stock returns and shows a strong positive relationship with the S&P500 market return.

Factor Analysis shows that Finance, Insurance and Real Estate has the highest average communality, indicating stronger systematic risk exposure.

The final recommended stocks all belong to Industry H, Finance, Insurance and Real Estate. These stocks show strong market correlation, strong PC1 loading, strong Factor 1 exposure, and high communality.

Clustering methods support the recommendation result. K-means and GMM produce consistent grouping patterns, and MDS visualisation shows that the recommended stocks are located close together in the similarity space.

## Conclusion

The project demonstrates how PCA, Factor Analysis, clustering, and correlation analysis can be used together to understand market risk structure and support portfolio-style stock selection.