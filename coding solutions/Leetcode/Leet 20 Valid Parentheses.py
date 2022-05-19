"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given a roman numeral, convert it to an integer.
"""

# UNFINISHED SOLUTION
# HANDLES SIMPLE CASES OF STANDARD PARENTHESES
# DOES NOT HANDLE THE CURLY OR SQUARE PARENTHESES
# DOES NOT CHECK IF THEY ARE CLOSED IN ORDER OR NOT

class Solution(object):
    def romanConverter(string):
        list_1 = list(string)
        length = len(list_1)
        left_bracket = 0
        right_bracket = 0
        for i in range(length):
            if list_1[i] == '(':
                left_bracket = left_bracket + 1 
            elif list_1[i] == ')':
                right_bracket = right_bracket + 1 
        check = right_bracket == left_bracket
        return check
        
roman_numeral = input("Enter a string of parentheses: ")
print(Solution.romanConverter(roman_numeral))