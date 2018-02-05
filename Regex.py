import re

number = phoneNumRegex.search(raw_input('Enter a phone number: '))

def phonenumber(number):
    phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    if number == True:
        print('here is the phone number: ' + number.group())
        print(number.group(1))
        print(number.group(2))
        print(number.group(0))
        print(number.groups())
        
    else:
        print('That does not appear to be a US phone number, try again')
    



print phonenumber(number)