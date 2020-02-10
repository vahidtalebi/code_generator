import datetime
class Createorder:
    def __init__(self):
        pass

    def generator(self):
        pass

    def date_time(self):
        self.today = datetime.datetime.today()
        if self.today.month <= 9:
            self.month = '0' + str(self.today.month)
        else:
            self.month = str(self.today.month)
    
    def parts(self):
        pass

    def concat(self):
        pass