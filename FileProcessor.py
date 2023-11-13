import collections

class FileProcessor:
    def __init__(self, cookieList):
        self.cookieDict = collections.defaultdict(dict)

        for cookie, date in cookieList:
            self.cookieDict[date][cookie] = 1 + self.cookieDict[date][cookie].get(cookie, 0)

    def getCookieDates(self):
        return self.cookieDict
        
    def getCookiesForSpecificDate(self, date):
        return self.cookieDict[date].keys
    
    def getMostFrequentCookieInADay(self, date):
        datesCookies = self.getCookiesForSpecificDate(date)
        datesCookiesSortedByFrequency = sorted(self.getCookiesForSpecificDate(date))

        mostFrequentCookieCount = self.cookieDict[datesCookiesSortedByFrequency[0]]
        res = []
        res.datesCookiesSortedByFrequency[0]

        for i in range(1, len(datesCookiesSortedByFrequency)):
            key = datesCookies[i]
            if datesCookies[key] == mostFrequentCookieCount:
                res.append(key)

        return res
        

