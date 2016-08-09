#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    while(True):
        try:
            user_input = int(input("Enter a no"))
            if (user_input % 2 == 0):
                print("Is even")
                break
            else:
                print("Odd")
                break
        except:
            print("Must be a no")


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    list = []
    chain = " "
    for i in range (1,101):
        if i % 10 == 0:
            list = list + [i]
            for j in list:
                if i < 11:
                    chain = chain + str(j) + "  " 
                else:
                    chain = chain + " " + str(j)
            print(chain)
            chain = ""
            list = []
        else:
            list = list + [i]


def cal_avg(lst):
    total = 0
    count = 0
    for i in lst:
        total += i
        count += 1
    print(total/count)
        

def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    lst_i = []
    while(True):
        try:
            user_input = input("Enter nos to be added")
            if user_input == 'done':
                cal_avg(lst_i)
                break
            else:
                lst_i = lst_i + [int(user_input)]
        except ZeroDivisionError as err:
            print("0")
            break
        except Exception as e:
            print(e)
            
##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    find_average()

if __name__ == '__main__':
    main()
