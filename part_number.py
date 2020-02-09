
class part_numberCreate:
    def __init__(self, num, vr=None):
        self.part_number = num
        self.vr = vr

    def part_code_genarator(self):
        if self.vr is None:
            self.result = self.i + self.part_number
        else:
            self.result = self.i + self.part_number + self.vr
        return self.result

    # This function for get some unique item from user and add to beginning of partnumber, it can be digit or word. 
    def first_part(self):
        i = input('Hi! please enter the key value or enter No: ')
        if i == 'No' or i == 'no' or i == 'NO' or i == 'n' or i == 'N' :
            pass
        # elif i.isalpha(): 
        #     print ('Please enter a number!!!')
        #     pass
        else:
            self.i = str(i)
            # print (self.i)
            return self.i
        
    # This function calculate number of digit of customerID and return the lenght
    def digit_calculator(self, n=5):
        digit = len(str(self.part_number))
        self.zeros = n - digit

    # This function add zero to every numbers
    def add_zero(self):
        self.part_number = ('0'*self.zeros) + str(self.part_number)
        return self.part_number

c = part_numberCreate(25)
c.first_part()
c.digit_calculator()
c.add_zero()
print (c.part_code_genarator())