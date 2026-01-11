import logging
logging.disable(logging.CRITICAL)  

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

from src.downloader import download_file
from src.parser import parse_file
from src.validator import validate_data


class TestEmployeeScraper(unittest.TestCase):

    # Test Case 1: Verify CSV File Download
    @patch("src.downloader.requests.get")
    def test_file_download_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.content = b"Employee ID,First Name\n1,John"
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = download_file("http://fakeurl.com/file.csv", "test.csv")
        self.assertEqual(result, "test.csv")

    # Test Case 2: Verify CSV File Extraction
    @patch("pandas.read_csv")
    def test_csv_parsing(self, mock_read_csv):
        mock_df = pd.DataFrame({
            "Employee ID": [1],
            "First Name": ["John"]
        })
        mock_read_csv.return_value = mock_df

        df = parse_file("test.csv")
        self.assertEqual(df.iloc[0]["First Name"], "John")

    # Test Case 3: Validate File Type and Format
    def test_invalid_file_format(self):
        with self.assertRaises(ValueError):
            parse_file("invalid.txt")

    # Test Case 4: Validate Data Structure
    def test_validate_correct_structure(self):
        data = {
            "Employee ID": [1],
            "First Name": ["John"],
            "Last Name": ["Doe"],
            "Email": ["john@example.com"],
            "Job Title": ["Engineer"],
            "Phone Number": ["1234567890"],
            "Hire Date": ["2022-01-01"]
        }

        df = pd.DataFrame(data)
        result = validate_data(df)
        self.assertTrue(result)

    # Test Case 5: Handle Missing or Invalid Data
    def test_missing_columns(self):
        data = {
            "Employee ID": [1],
            "First Name": ["John"]
        }

        df = pd.DataFrame(data)

        with self.assertRaises(ValueError):
            validate_data(df)


if __name__ == "__main__":
    unittest.main()
