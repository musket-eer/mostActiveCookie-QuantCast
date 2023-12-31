import collections
from datetime import datetime
from CSVParser import CSVParser

class FileProcessor:
    """
    A class for processing and analyzing cookie data stored in a dictionary structure.

    Attributes:
    - cookieDict (defaultdict): A defaultdict containing date-wise dictionaries of cookies and their frequencies.

    Methods:
    - __init__(self, cookieList: list) -> None:
        Initializes the FileProcessor object with a list of cookie data.
        Processes the data and populates cookieDict with date-wise dictionaries of cookies and their frequencies.

    - getCookieDates(self) -> defaultdict:
        Returns the date-wise dictionary of cookies and their frequencies.

    - getCookiesForSpecificDate(self, date: str) -> dict:
        Returns the dictionary of cookies and their frequencies for a specific date.

    - getMostFrequentCookiesInADay(self, date: str) -> list:
        Returns a list of the most frequently occurring cookies on a specific date.
        If there are ties in frequency, returns all tied cookies.

    Example usage:
    >>> cookie_data = [('chocolatecookie', '2023-01-15'), ('cresentcookie', '2023-01-16'), ...]
    >>> processor = FileProcessor(cookie_data)
    >>> all_dates_cookies = processor.getCookieDates()
    >>> cookies_on_specific_date = processor.getCookiesForSpecificDate('2023-01-15')
    >>> most_frequent_cookies = processor.getMostFrequentCookiesInADay('2023-01-15')
    """

    def __init__(self, cookieList: list):
        self.cookieDict = collections.defaultdict(dict)
        for cookie, date in cookieList:
            self.cookieDict[date][cookie] = 1 + self.cookieDict[date].get(cookie, 0)

    def getCookieDates(self):
        return self.cookieDict
        
    def getCookiesForSpecificDate(self, date):
        return self.cookieDict[date]
    
    def getMostFrequentCookiesInADay(self, date):
        if date[4] != '-' or date[7] != '-':
            print("Invalid date format")
            return []

        datesCookies = self.getCookiesForSpecificDate(date)
        if not datesCookies:
            return []
        
        datesCookiesSortedByFrequency = sorted(datesCookies, key=datesCookies.get, reverse=True)
        mostFrequentCookieCount = datesCookies[datesCookiesSortedByFrequency[0]]
        res = [datesCookiesSortedByFrequency[0]]
        
        for i in range(1, len(datesCookiesSortedByFrequency)):
            key = datesCookiesSortedByFrequency[i]

            if datesCookies[key] == mostFrequentCookieCount:
                res.append(key)

        return res
    
