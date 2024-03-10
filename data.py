from openpyxl import load_workbook

class WebData:
    def __init__(self):
        self.url = "https://www.imdb.com/search/name/"
        self.name = "Anu"
        self.birthFromDate = "12-09-1990"
        self.birthToDate = "13-09-1990"
        self.birthday = "09-12"
        self.pageTitle = "Advanced name search"
        self.dashboardUrl = "https://www.imdb.com/search/name/?name=Anu"
        '''
        self.searchTopic = "Biography"
        self.subTopic = "Arrested"
        self.deathFromDate = "20-04-2065"
        self.deathToDate = "21-04-2065"
        self.credits = "Bio Hunter"
        '''
