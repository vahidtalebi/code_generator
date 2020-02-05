
import hashlib


customer = input('Customer: ')
order = input('Order: ')
part = input('Part: ')
boardnumber = input('Board Numbers: ')

#this function calculate number of digits and number zeros we need 
def digit_calculator(number, n):
    digit = len(str(number))
    zeros = n - digit
    return digit, zeros

# this function create number and missing digit for serial number
def add_zero(number, zeros):
    number = ('0'*zeros) + str(number)
    return number 

def concat_3(a, b, c):
    result = a + b + c
    return result

def numbered(input, number):
    for i in range(number):
        i = i+1
        
        print (input + add_zero(i, digit_calculator(i, 10)[1]))

numbered(concat_3(add_zero(customer, digit_calculator(customer, 10)[1]),add_zero(order, digit_calculator(order, 5)[1]), add_zero(part, digit_calculator(part, 5)[1])), int(boardnumber))       
# print (add_zero(1080255664, digit_calculator(1080255664, 15)[1]))
# print (numbered('vahid', 10))