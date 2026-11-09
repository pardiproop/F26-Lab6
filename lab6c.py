# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/06/2026
# Purpose: Practice Set Operations.
# Usage: ./lab6c.py

# TO DO 1: Copy the code from lab5b.py and paste here.
def buildtheSet(divisor):
    s3=set()
    s5=set()
    s7=set()
    # Complete this function
    for num in range(1,101):
        if num%3==0:
            s3.add(num)
        if num%5==0:
            s5.add(num)
        if num%7==0:
            s7.add(num)
    return s3,s5,s7

def s3_or_s5(s3,s5):
    only_s3=s3.difference(s5)
    only_s5=s5.difference(s3)
    only_s7=s7.difference(s3)
    only_s7=s7.difference(s5)
    only_s3=s3.difference(s7)
    only_s5=s5.difference(s7)
    common_set=s3.intersections(s5).difference(s7)
    result_set=(only_s3.union(only_s5)).difference=only_s7(common_set)
    return result_set

def main():

    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

main()

# TO DO 2: Create the function s3_and_s5_not_s7().
# TO DO 3: Run the script. Take screenshot of only s3_and_s5_not_s7() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.
