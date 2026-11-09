# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/06/2026
# Purpose: Creating dictionary.
# Usage: ./lab6d.py

# TO DO 1: Create function times_ten as instructed in readme.md file. 
def times_ten(start_index: int, end_index: int):
    my_dict={}
    for num in range(start_index, end_index+1):
        my_dict[num]=num*10
    return my_dict

def main():
    my_dict=times_ten(2,6)
    print(my_dict)
main()

# TO DO 2: Run the script.
