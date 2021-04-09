from num2words import num2words
from word2number import w2n
from collections import OrderedDict
import datetime


while True:
    ip=input('\npress 1-number to words\npress 2-words to number\npress 3-number to roman number\npress 4-palindrome numeer\npress 5-age calculator\nQ/q to quit\nenter your choice : ')


    if ip=='1':
        
        try:
            n= int(input("Enter number : "))
            print(f'{n} in words is {num2words(n)}')
        except ValueError:
            print("Enter integer number")

    elif ip == '2':

        test_str = input('enter string : ')

        print("The original string is : " + test_str)

        res = w2n.word_to_num(test_str)

        print("The string after performing replace : " + str(res))

    elif ip=='3':

        def write_roman(num):

            roman = OrderedDict()
            roman[1000] = "M"
            roman[900] = "CM"
            roman[500] = "D"
            roman[400] = "CD"
            roman[100] = "C"
            roman[90] = "XC"
            roman[50] = "L"
            roman[40] = "XL"
            roman[10] = "X"
            roman[9] = "IX"
            roman[5] = "V"
            roman[4] = "IV"
            roman[1] = "I"

            def roman_num(num):
                for r in roman.keys():
                    x=num//r
                    yield roman[r] * x
                    num -= (r * x)
                    if num <= 0:
                        break

            return "".join([a for a in roman_num(num)])
        try:
            n= int(input("Enter number : "))
            print(write_roman(n))
        except ValueError:
            print("Enter integer number: ")

    elif ip=='4':

        def reverse(num):
            reverse = 0
            while num > 0:
                digit = num % 10
                reverse = reverse * 10 + digit
                num = num // 10
            return reverse


        try:
            num = int(input("Enter any number : "))
            temp = num
            if num == reverse(num):
                print(f'{num} is a palindrome number')
            else:
                while True:
                    num -= 1
                    if num == reverse(num):
                        x = num
                        print(f'Before palindrome is : {x}')
                        break
                while True:
                    num += 1
                    if num == reverse(num):
                        y = num
                        print(f'Next palindrome is : {y}')
                        break
                # print(abs(x-temp))
                # print(abs(y-temp))
                if abs(temp - x) < abs(temp - y):
                    print(x)
                else:
                    print(y)
        except ValueError:
            print("Enter integers only")

    elif ip=='5':
        def age_calculator():
            current_date = datetime.datetime.now()
            date_of_birth = input("Enter your date of birth (dd/mm/yyyy) : ")
            dendline_date = datetime.datetime.strptime(date_of_birth, '%d/%m/%Y')
            print(dendline_date)
            # daysLeft =  dendline_date - current_date
            daysLeft = current_date - dendline_date

            years = ((daysLeft.total_seconds()) / (365.242 * 24 * 3600))
            yearsInt = int(years)

            months = (years - yearsInt) * 12
            monthsInt = int(months)

            days = (months - monthsInt) * (365.242 / 12)
            daysInt = int(days)

            hours = (days - daysInt) * 24
            hoursInt = int(hours)

            minutes = (hours - hoursInt) * 60
            minutesInt = int(minutes)

            seconds = (minutes - minutesInt) * 60
            secondsInt = int(seconds)

            print(f'Your are {yearsInt} years, {monthsInt} months, {daysInt} days, {hoursInt} hours, {minutesInt} minutes {secondsInt} seconds')


        age_calculator()

    else:
        if ip=='Q' or ip=='q':
            break
