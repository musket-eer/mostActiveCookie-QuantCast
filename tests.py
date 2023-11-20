#!/usr/bin/python3

import unittest
import tempfile
import os
from CSVParser import CSVParser  

class TestCSVParser(unittest.TestCase):
    """A test case class for the CSVParser class.

    This class contains unit tests for the CSVParser class, focusing on various scenarios:
    - Testing the `getCookies` method with a sample CSV file.
    - Testing the case where the CSV file is not found.
    - Testing the case where the CSV file is empty.

    Attributes:
        csv_content (str): Sample CSV content for testing.
        temp_csv (str): Path to the temporary CSV file created for testing.
    """
    def setUp(self):
        # Create a temporary CSV file for testing
        self.csv_content = "CookieName,Date\nsnowballcookies,2023-01-15\niceboxcookies,2023-01-16"
        self.temp_csv = tempfile.NamedTemporaryFile(mode="w", delete=False)
        self.temp_csv.write(self.csv_content)
        self.temp_csv.close()

    def tearDown(self):
        # Remove the temporary CSV file after testing
        os.remove(self.temp_csv.name)

    def test_getCookies(self):
        # Test the getCookies method with a sample CSV file
        parser = CSVParser(self.temp_csv.name)
        cookies = parser.getCookies()
        expected_cookies = [('snowballcookies', '2023-01-15'), ('iceboxcookies', '2023-01-16')]
        self.assertEqual(cookies, expected_cookies)

    def test_file_not_found(self):
        # Test the case where the CSV file is not found
        with self.assertRaises(FileNotFoundError):
            CSVParser("nonexistent_file.csv")

    def test_empty_file(self):
        # Test the case where the CSV file is empty
        empty_temp_csv = tempfile.NamedTemporaryFile(mode="w", delete=False)
        empty_temp_csv.close()
        parser = CSVParser(empty_temp_csv.name)
        cookies = parser.getCookies()
        self.assertEqual(cookies, [])




if __name__ == "__main__":
    unittest.main()
