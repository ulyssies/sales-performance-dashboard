<div align="center">

<br />

```
███████╗ █████╗ ██╗     ███████╗███████╗
██╔════╝██╔══██╗██║     ██╔════╝██╔════╝
███████╗███████║██║     █████╗  ███████╗
╚════██║██╔══██║██║     ██╔══╝  ╚════██║
███████║██║  ██║███████╗███████╗███████║
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝

██████╗  █████╗ ███████╗██╗  ██╗██████╗  ██████╗  █████╗ ██████╗ ██████╗
██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
██║  ██║███████║███████╗███████║██████╔╝██║   ██║███████║██████╔╝██║  ██║
██║  ██║██╔══██║╚════██║██╔══██║██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║
██████╔╝██║  ██║███████║██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝
```

### Sales Performance Dashboard

**An end-to-end analytics pipeline that transforms raw retail data into interactive business insights.**

[![Live Dashboard](https://img.shields.io/badge/View_Dashboard-Tableau_Public-6366f1?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/views/SalesDashboard_17543609469410/Dashboard1)
[![Python](https://img.shields.io/badge/Python-3.11-6366f1?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Google Sheets](https://img.shields.io/badge/Google_Sheets-API-6366f1?style=for-the-badge&logo=googlesheets&logoColor=white)](https://developers.google.com/sheets)
[![Tableau](https://img.shields.io/badge/Tableau-Public-6366f1?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com)

<br />

</div>

---

## Overview

Raw sales data from Global Superstore is cleaned and pushed into Google Sheets via a Python ETL pipeline. Google Sheets acts as a live data source for a Tableau dashboard that surfaces KPIs, regional trends, product performance, and sales forecasts — all embedded and accessible via GitHub Pages.

---

## Tech Stack

| Layer | Tools |
|---|---|
| ETL | Python, pandas, gspread |
| Storage | Google Sheets API, Drive API |
| Visualization | Tableau Public |
| Hosting | GitHub Pages |

---

## Features

- Automated ETL pipeline — cleans and loads raw CSV into Google Sheets
- Live Tableau connection — dashboard updates when data changes
- KPIs, sales trends, forecasts, regional maps, and category breakdowns
- Embedded dashboard via GitHub Pages

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/ulyssies/sales-performance-dashboard.git
cd sales-performance-dashboard

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your Google service account key to the project root
# File should be named sheets-service.json (already git-ignored)

# Run the pipeline
python scripts/import_csv.py
```

---

## Project Structure

```
sales-performance-dashboard/
├── data/
│   ├── raw/
│   │   └── global_superstore.csv
│   └── processed/
├── scripts/
│   └── import_csv.py
├── tableau/
│   └── dashboard.twbx
├── web/
│   └── index.html
├── docs/
│   ├── dashboard-preview.png
│   └── KPIs.md
├── requirements.txt
└── README.md
```

---

## Data

Source dataset: [Global Superstore](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset) — retail transactions across regions, categories, and customer segments.

---

<div align="center">

*Built by [Ulyssies Adams](https://ulyssies.github.io/personal-website)*

</div>
