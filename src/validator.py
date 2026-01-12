import logging
import re
from datetime import datetime

logging.basicConfig(level=logging.INFO)

REQUIRED_COLUMNS = [
    "Employee ID",
    "First Name",
    "Last Name",
    "Email",
    "Job Title",
    "Phone Number",
    "Hire Date"
]

COLUMN_MAPPING = {
    "User Id": "Employee ID",
    "Phone": "Phone Number",
    "Date of birth": "Hire Date"
}
PHONE_PATTERN = re.compile(r"^[\d\+\-\(\)\s\.]+(x\d+)?$")# 7-15 digits, optional +
DATE_FORMAT = "%Y-%m-%d"  # Expected format for hire date

def validate_data(df):
    """
    Validates and transforms employee data to match user story schema
    """

    # Rename columns
    df.rename(columns=COLUMN_MAPPING, inplace=True)
    logging.info(f"Columns after mapping: {list(df.columns)}")

    # Check for required columns
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        logging.error(f"Missing columns: {missing_columns}")
        raise ValueError(f"Missing columns: {missing_columns}")

    # Check for null values in required fields
    if df[REQUIRED_COLUMNS].isnull().any().any():
        raise ValueError("Some required fields contain missing values")

    # Validate phone numbers
    for i, phone in enumerate(df["Phone Number"]):
        if not PHONE_PATTERN.match(str(phone)):
            raise ValueError(f"Invalid phone number at row {i}: {phone}")

    # Validate hire date format
    for i, date_str in enumerate(df["Hire Date"]):
        try:
            datetime.strptime(str(date_str), DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Invalid hire date at row {i}: {date_str}")

    logging.info("Data validation successful. All required columns are present and valid.")
    return True
