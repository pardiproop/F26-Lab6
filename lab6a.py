# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/06/2026
# Purpose: Create Sets.
# Usage: ./lab6a.py

# TO DO 1: Complete the functions below.

def buildtheSet(divisor):
    s3=set()
    s5=set()
    s7=set()
    s21=set()
    # Complete this function
    for num in range(1,101):
        if num%3==0:
            s3.add(num)
        if num%5==0:
            s5.add(num)
        if num%7==0:
            s7.add(num)
        if num%11==0:
            s21.add(num)
    return s3,s5,s7,s21

def main():

    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")

    s11 = buildtheSet(11)
    print("s11: ", s11)

main()

# TO DO 2: Run the script. Take screenshot of only buildtheSet() function. No need to capture main() in the screenshot. 
