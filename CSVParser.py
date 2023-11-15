
class CSVParser:
     """
    A simple CSV parser for reading and extracting information from a CSV file containing cookie data.

    Attributes:
    - path (str): The file path of the CSV file to be parsed.
    - cookiesList (list): A list to store extracted cookie data in the format (cookie_name, date).

    Methods:
    - __init__(self, path: str) -> None:
        Initializes the CSVParser object with the provided file path.
        Reads the CSV file, skipping the header.
        Parses each line to extract relevant information (cookie_name, date) and stores it in cookiesList.

    - getCookies(self) -> list:
        Returns the list of extracted cookie data in the format (cookie_name, date).

    Example usage:
    >>> parser = CSVParser("path/to/cookie_data.csv")
    >>> cookies = parser.getCookies()
    >>> print(cookies)
    [('ChocolateChip', '2023-01-15'), ('OatmealRaisin', '2023-01-16'), ...]
    """
    def __init__(self, path) -> None:
        file_object = open(path, "r")
        file_object.readline()

        self.cookiesList = []
        for line in file_object:
            single_line = line.split(",")
            self.cookiesList.append((single_line[0], (single_line[1][0:10])))

    def getCookies(self):
        return self.cookiesList
    

