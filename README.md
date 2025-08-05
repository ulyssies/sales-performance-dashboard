# 📊 Sales Performance Dashboard

A full-stack analytics pipeline that transforms raw sales data (`global_superstore.csv`) into interactive business insights. The pipeline cleans and loads the data into Google Sheets, which is live-linked to a Tableau dashboard for visualization. The final dashboard is embedded via GitHub Pages.

## 🔗 Live Dashboard

👉 [View the Tableau Dashboard on Tableau Public](https://public.tableau.com/views/SalesDashboard_17543609469410/Dashboard1)

![Dashboard Preview](./docs/dashboard-preview.png)

---

## ⚙️ Tech Stack

**ETL Pipeline**
- Python (pandas, gspread, oauth2client)
- Google Sheets API + Drive API

**Storage**
- Google Sheets (as cleaned data source)

**Visualization**
- Tableau Public (live-connected to Google Sheets)
- Dashboard includes KPIs, sales trends, forecasts, maps, and product/category breakdowns

**Hosting**
- GitHub Pages (with optional HTML embed)

---

## 🚀 Setup & Run (ETL Pipeline)

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/sales-performance-dashboard.git
cd sales-performance-dashboard

# 2. Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Place your Google service-account JSON in the project root (git-ignored)
#    e.g. sheets-service.json

# 5. Push cleaned data into the connected Google Sheet
python scripts/import_csv.py

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
│   └── index.html            # optional GitHub Pages embed
└── docs/
    ├── dashboard-preview.png
    ├── KPIs.md
    └── wireframes/

Credits
Data: Global Superstore

Visualizations: Built using Tableau Public

Author: Ulyssies Adams

