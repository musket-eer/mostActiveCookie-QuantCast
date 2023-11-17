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
        self.parser = argparse.ArgumentParser(description="Cookie Data Analyzer")

        # Define command-line arguments
        self.parser.add_argument("filepath")
        self.parser.add_argument("-d", "--date", help="Specify a date for cookie analysis")
        

    def run(self):
        """
        Parses command-line arguments and executes the program based on the provided options.
        """
        args = self.parser.parse_args()

        # Check if the date option is provided
        if args.date:
            path = args
            date = args.date
            # Add your program logic here based on the provided date
            print(f"Analyzing data for date: {date}")
            cookie_data = CSVParser("path/to/cookie_data.csv").getCookies()
            result = FileProcessor(cookie_data).getMostFrequentCookiesInADay(date)
            print(result)
        else:
            print("Please provide a date using the -d or --date option.")

if __name__ == "__main__":
    # Run the program when the script is executed
    cli_parser = CommandLineParser()
    cli_parser.run()
