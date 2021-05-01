from datetime import datetime

class Date:
    def __init__(self):
        t = ['월','화','수','목','금','토','일']
        self.year = datetime.today().year
        self.month = datetime.today().month
        self.day = datetime.today().day
        self.day_of_week = t[datetime.today().weekday()]

    def __str__(self):
        return f'{self.month}월 {self.day}일 {self.day_of_week}요일'
        #print(f'{self.year},{self.month},{self.day},{self.day_of_week}')

    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def getDayOfweek(self):
        return self.day_of_week

if __name__ == '__main__':
    data = Date()
    data.__str__()

