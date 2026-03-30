# Multi-Source Data Integration & AI-Ready Pipeline

## Overview
This project builds a unified profile dataset for 10 public figures by integrating data from multiple public sources, including Wikipedia, YouTube, Twitter/X, Instagram, TikTok, and Google Knowledge Graph.

The goal was to collect, standardize, validate, and combine cross-platform information into a structured dataset suitable for downstream analysis and AI-ready workflows.

## Features
- Multi-source API and web data integration
- Unified schema design across platforms
- Data cleaning and validation
- Handling missing fields and inconsistent formats
- Cross-platform identity matching
- Structured output in CSV / dataframe format

## Data Sources
- Wikipedia / Wikidata API
- YouTube Data API v3
- Twitter/X API
- Apify-based scraping for Instagram
- Apify-based scraping for TikTok
- Google Knowledge Graph Search API

## Project Workflow
1. Identify retrievable fields from each source
2. Design a unified data schema
3. Extract data using APIs or controlled scraping
4. Clean and standardize inconsistent values
5. Resolve missing fields and platform-specific differences
6. Combine records into a final unified dataset

## Tech Stack
- Python
- pandas
- requests
- Jupyter Notebook
- API integration
- Web scraping tools

## Example Use Cases
- Cross-platform profile comparison
- Data validation across public sources
- Building AI-ready structured datasets
- Supporting downstream analytics and NLP workflows

## Repository Contents
- `API_Data Integration_Project.ipynb` — main notebook
- `DatasetOfUnifiedProfiles.csv` — final unified dataset
- `API_Data Integration_Project Report.docx` — project report
- `README.md` — project documentation

## Setup
Clone the repository and install dependencies:

```bash
pip install pandas requests python-dotenv
