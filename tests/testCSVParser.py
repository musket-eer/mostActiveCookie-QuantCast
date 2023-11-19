import unittest
import tempfile
import os
from datetime import datetime
from CSVParser import CSVParser  

class TestCSVParser(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.csv_content = "CookieName,Date\nChocolateChip,2023-01-15\nOatmealRaisin,2023-01-16"
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
        expected_cookies = [('ChocolateChip', '2023-01-15'), ('OatmealRaisin', '2023-01-16')]
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

    def test_invalid_date_format(self):
        # Test the case where the CSV file contains an invalid date format
        invalid_date_csv = tempfile.NamedTemporaryFile(mode="w", delete=False)
        invalid_date_csv.write("CookieName,Date\nChocolateChip,2023/01/15")
        invalid_date_csv.close()
        parser = CSVParser(invalid_date_csv.name)
        with self.assertRaises(ValueError):
            parser.getCookies()


if __name__ == "__main__":
    unittest.main()
