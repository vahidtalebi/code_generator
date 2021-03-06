import datetime
# This class get a number as input, do some proccess and give a number as output
# that number including the year and month of customer register day and customerID  
class CustomerCreate:
    def __init__(self, num):
        self.customer_id = num
        self.today = datetime.datetime.today()
        if self.today.month <= 9:
            self.month = '0'+ str(self.today.month)
        else:
            self.month = str(self.today.month)

    # Generate our customer id 
    def create_customerID(self):
        self.result = str(self.today.year) + self.month + self.customer_id
        return self.result

    # This function calculate number of digit of customerID and return the lenght
    def digit_calculator(self, n=5):
        digit = len(str(self.customer_id))
        self.zeros = n - digit

    # This function add zero to every numbers
    def add_zero(self):
        self.customer_id = ('0'*self.zeros) + str(self.customer_id)
        return self.customer_id

c = CustomerCreate(124) 

c.digit_calculator()
c.add_zero()
l = c.create_customerID()
print (l)