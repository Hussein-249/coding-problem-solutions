"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def twoSum(nums, target):
        
        # Flag for case in which target is unreachable
        Flag = False

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    Flag = True
                    return [i, j]
        if Flag == False:
            return "Not possible"

# user input
numbers = []
while True:
    
    user_input1 = input("Add an integer to the list. Type E to exit.")  
    if user_input1 == 'E':
        break
    else:
        numbers.append(int(user_input1))

print(numbers)
user_input2 = int(input("Enter the target integer: "))

# call function
print(Solution.twoSum(numbers, user_input2))