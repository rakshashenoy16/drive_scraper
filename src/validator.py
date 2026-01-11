import logging

logging.basicConfig(level=logging.INFO)

# What the user story expects
REQUIRED_COLUMNS = [
    "Employee ID",
    "First Name",
    "Last Name",
    "Email",
    "Job Title",
    "Phone Number",
    "Hire Date"
]

# Mapping from your actual CSV columns → user story columns
COLUMN_MAPPING = {
    "User Id": "Employee ID",
    "Phone": "Phone Number",
    "Date of birth": "Hire Date"
}

def validate_data(df):

    # Validates and transforms employee data to match user story schema
    

    # Rename columns based on mapping
    df.rename(columns=COLUMN_MAPPING, inplace=True)

    logging.info(f"Columns after mapping: {list(df.columns)}")

    # Check for required columns
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_columns:
        logging.error(f"Missing columns: {missing_columns}")
        raise ValueError(f"Missing columns: {missing_columns}")

    # Check for null values
    if df[REQUIRED_COLUMNS].isnull().any().any():
        logging.warning("Some records contain missing values in required fields")

    logging.info("Data validation successful. All required columns are present.")
    return True
