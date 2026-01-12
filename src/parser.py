# Detects file type (CSV or Excel) and reads it into a pandas DataFrame.
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def parse_file(file_path):
    try:
        if file_path.endswith(".csv"):
            logging.info("Detected CSV file")
            df = pd.read_csv(file_path)

        elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
            logging.info("Detected Excel file")
            df = pd.read_excel(file_path)

        else:
            raise ValueError("Unsupported file format")

        return df

    except Exception as e:
        logging.error(f"Parsing error: {e}")
        raise
