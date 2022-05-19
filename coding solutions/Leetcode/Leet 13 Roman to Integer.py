"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given a roman numeral, convert it to an integer.
"""

# UNFINISHED SOLUTION
# HANDLES BASE CASES AND CASES OF I-SUBTRACTION
# DOES NOT HANDLE THE CASE OF X- AND C- SUBTRACTION

class Solution(object):
    def romanConverter(string):
        number = 0
        dictionary_1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        list_1 = list(string)
        length = len(list_1)
        for i in range(length):
            if list_1[i] in dictionary_1:
                if list_1[i] == 'V' or list_1[i] == 'X':
                    if i != 0 and list_1[i - 1] == 'I':
                        number = number + dictionary_1[list_1[i]] -1
                    else:
                        number = number + dictionary_1[list_1[i]]
                elif list_1[i] == 'I':
                    if i < length - 1 and list_1[i + 1] == 'I':
                        number = number + dictionary_1[list_1[i]]
                    elif i == length - 1:
                        number = number + dictionary_1[list_1[i]]
                    else:
                        pass
                else:
                    number = number + dictionary_1[list_1[i]]
    
        return number
        
roman_numeral = input("Enter a string of roman numerals: ")
print(Solution.romanConverter(roman_numeral))