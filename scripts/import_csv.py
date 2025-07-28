import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# -----------------------
# Configuration
# -----------------------
RAW_CSV_PATH = "data/raw/global_superstore.csv"
CLEAN_CSV_PATH = "data/processed/global_superstore_cleaned.csv"
SPREADSHEET_NAME = "Sales Performance Data"
WORKSHEET_NAME = "raw_data"
SERVICE_ACCOUNT_FILE = "sheets-service.json"

# -----------------------
# Helper Functions
# -----------------------
def read_and_clean_csv(path: str) -> pd.DataFrame:
    """
    Read the raw CSV, parse dates, convert to strings, and add Year/Month helper columns.
    """
    df = pd.read_csv(path, parse_dates=["Order Date", "Ship Date"])
    # Convert datetime columns to ISO strings for Sheets
    df["Order Date"] = df["Order Date"].dt.strftime('%Y-%m-%d')
    df["Ship Date"]  = df["Ship Date"].dt.strftime('%Y-%m-%d')
    # Add helper columns
    df["Year"]  = pd.to_datetime(df["Order Date"]).dt.year
    df["Month"] = pd.to_datetime(df["Order Date"]).dt.to_period("M").astype(str)
    return df


def save_clean_csv(df: pd.DataFrame, path: str) -> None:
    """
    Save the cleaned DataFrame locally as CSV.
    """
    df.to_csv(path, index=False)


def push_to_sheets(df: pd.DataFrame):
    """
    Authenticate using service-account and update the specified worksheet.
    """
    # Replace NaN with empty strings for JSON compatibility
    df = df.fillna("")

    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_FILE,
        scope
    )
    client = gspread.authorize(creds)

    # Open the spreadsheet and select the worksheet by name
    spreadsheet = client.open(SPREADSHEET_NAME)
    worksheet = spreadsheet.worksheet(WORKSHEET_NAME)

    # Clear existing data and update with new
    worksheet.clear()
    # Convert DataFrame to list of lists for Sheets
    data = [df.columns.tolist()] + df.values.tolist()
    worksheet.update(data)
    print(f"✅ Updated '{WORKSHEET_NAME}' in '{SPREADSHEET_NAME}' successfully!")


# -----------------------
# Main Execution
# -----------------------
if __name__ == "__main__":
    # 1. Read and clean
    df = read_and_clean_csv(RAW_CSV_PATH)

    # 2. Save locally (optional)
    save_clean_csv(df, CLEAN_CSV_PATH)

    # 3. Push to Google Sheets
    push_to_sheets(df)
