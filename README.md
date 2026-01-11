# Employee Data Scraper

A Python-based scraper to download employee data from a Google Drive file, validate it, and generate a cleaned dataset ready for further processing or ingestion into a data warehouse.

---

## Features

- Downloads CSV or Excel files from a Google Drive URL.
- Detects file type automatically (CSV / Excel).
- Validates that all required columns are present.
- Maps columns from source format to the standard schema.
- Handles missing or invalid data gracefully.
- Unit tests implemented using `unittest` with mocks to avoid actual network calls.

---

##  Project Structure

