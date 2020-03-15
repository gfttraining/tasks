
# Python script to return a value True if the input string is a Palindrome and else it will return False
# The script is case insensitive and ignore any non-alphanumeric characters

import sys

input_str = sys.argv[1]

def isPalindrome(input_str):

    try:
      
        result_str = "".join(char.lower() for char in input_str if char.isalnum())

        return result_str == result_str[::-1]

    except:

        print('An error occured')

check_palindrome = isPalindrome(input_str)

print('The input string "' + input_str + '" is a palindrome: ' + str(check_palindrome))
