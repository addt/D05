#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
f = open("words.txt")
str_1 = f.read().split()
for i in str_1:
    if len(i) > 20:
        print(i)

##############################################################################
def main():
    pass  # Call your functions here.

if __name__ == '__main__':
    main()
