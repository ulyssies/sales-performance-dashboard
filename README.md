# Sales Performance Dashboard

**Overview**
An end-to-end analytics pipeline that ingests raw sales data (`global_superstore.csv`), applies cleaning and transformations (Year/Month columns), and publishes the results to a Google Sheet. A live connection from Tableau Public visualizes key KPIs (revenue, profit, time series, regional comparisons).

**Tech Stack**

* Data & ETL: Python (pandas, gspread, oauth2client), Google Sheets API, Google Drive API
* Storage: Google Sheets (ETL backend)
* Visualization: Tableau Public
* Hosting: GitHub Pages (embed Tableau)

**Prerequisites**

1. Python 3.x installed
2. A Google Cloud service account key (JSON) with Sheets & Drive API enabled and shared with the target Sheet
3. Google Sheet named **Sales Performance Data**, shared with your service account email

**Setup & Run**

```bash
# 1. Clone the repo
git clone git@github.com:YOUR_USERNAME/sales-performance-dashboard.git
cd sales-performance-dashboard

# 2. Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Place your service-account JSON in the project root (ignored by Git)
#    e.g. sheets-service.json or sales-dashboard.json

# 5. Run the import script to push cleaned data into Google Sheets
python scripts/import_csv.py
```

**Project Structure**

```
sales-performance-dashboard/
├── .gitignore
├── README.md
├── requirements.txt
├── sheets-service.json      # your JSON key (git-ignored)
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
└── docs/
    ├── KPIs.md
    └── wireframes/
```

**Next Steps**

1. Build and refine Pivot Tables in Google Sheets for QA.
2. Connect Tableau Public to the live Sheet and design interactive dashboards.
3. Automate ETL scheduling (cron or Cloud Function).
4. Embed and document on GitHub Pages.
