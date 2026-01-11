from downloader import download_file
from parser import parse_file
from validator import validate_data, REQUIRED_COLUMNS

URL = "https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download"
RAW_FILE = "employee_data.csv"
CLEAN_FILE = "scraped_employee_data.csv"

def run_scraper():
    try:
        # Step 1: Download raw file
        file_path = download_file(URL, RAW_FILE)

        # Step 2: Parse raw file
        df = parse_file(file_path)

        # Step 3: Validate + map data
        validate_data(df)

        # Step 4: Select only required columns
        final_df = df[REQUIRED_COLUMNS]

        # Step 5: Save cleaned data to new CSV
        final_df.to_csv(CLEAN_FILE, index=False)

        print("Employee data pipeline executed successfully!")
        print(f"Raw file saved as: {RAW_FILE}")
        print(f"Clean file saved as: {CLEAN_FILE}")

    except Exception as e:
        print(f"Scraper failed: {e}")

if __name__ == "__main__":
    run_scraper()
