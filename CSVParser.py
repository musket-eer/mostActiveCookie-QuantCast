import dateparser

class CSVParser:
    def __init__(self, path) -> None:
        file_object = open(path, "r")
        file_object.readline()

        self.cookiesList = []
        for line in file_object:
            self.cookiesList.append(line[0], dateparser.parse(line[1]).day)


    def getCookies(self):
        return self.cookiesList
    
    