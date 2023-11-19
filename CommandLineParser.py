import argparse
from CSVParser import CSVParser
from FileProcessor import FileProcessor

class CommandLineParser:
    """
    A class to parse command-line arguments and execute the program accordingly.

    Methods:
    - run(self) -> None:
        Parses command-line arguments and executes the program based on the provided options.

    Example usage:
    >>> parser = CommandLineParser()
    >>> parser.run()
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Your program description")

        self.parser.add_argument("filepath", help="Path to the CSV file")
        self.parser.add_argument("-d", "--date", help="Date for analysis (format: YYYY-MM-DD)")

    def run(self):
        """
        Parses command-line arguments and executes the program.
        """
        args = self.parser.parse_args()

        if args.date:
            filepath = args.filepath
            date = args.date
            cookie_data = CSVParser(filepath).getCookies()
            result = FileProcessor(cookie_data).getMostFrequentCookiesInADay(date)
            print(result)
        else:
            print("Please provide a date using the -d or --date option.")


