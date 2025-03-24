# Football Data Pipeline 🏆⚽

## 📌 Project Overview
This project extracts Premier League match data from API-Football, loads it into Google BigQuery, and transforms it using DBT. The entire process is orchestrated using Apache Airflow.

## 🔹 Features
- Calls API-Football to fetch match data
- Loads raw data into Google BigQuery
- Cleans & transforms data using DBT Core
- Orchestrates everything with Apache Airflow
- Implements a star schema (fact & dimension tables)

## 🚀 Tech Stack
- **Python** (`requests`, `pandas`)
- **BigQuery** (Cloud Data Warehouse)
- **DBT Core** (Data modeling & transformations)
- **Airflow** (Task orchestration)
- **API-Football** (Football data API)

## 📂 Repository Structure

football-data-pipeline/
│── dags/                   # Airflow DAGs (Orchestration)
│   ├── football_pipeline.py
│   ├── extract.py          # API extraction logic
│   ├── load.py             # Load data to BigQuery
│   ├── transform.py        # Trigger DBT models
│── dbt/                    # DBT project folder
│   ├── models/
│   │   ├── staging/        # Raw staging tables
│   │   ├── marts/          # Final transformed tables
│   │   ├── schema.yml      # DBT tests & metadata
│   ├── dbt_project.yml     # DBT project config
│── scripts/                # Utility scripts for local testing
│   ├── test_api.py         # Test API connection
│   ├── manual_load.py      # Manually load a sample dataset
│── config/                 # Configuration files (DO NOT COMMIT SECRETS)
│   ├── example_config.yaml # Example for API keys (DO NOT store real keys)
│── notebooks/              # Jupyter notebooks for data exploration
│── .gitignore              # Ignore sensitive files (see below)
│── README.md               # Project documentation
│── requirements.txt        # Python dependencies
│── airflow_settings.json   # Airflow environment settings (optional)

## Insert Schema Diagram