# Solve the following problem:
# In comments Provide the Time Complexity of your solution.
# Your mission is to solve this problem in O(n) time or better

# [ log(n), n, n**2, n**3 ]

# A phrase is a  if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true or false.
 
# s = "A man, a plan, a canal: Panama"
# true
# "amanaplanacanalpanama" is a palindrome.

# s = "race a car"
# false
# "raceacar" is not a palindrome.

# s = " "
# true
# s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

s = "amanaplanacanalpanama"
# "A man, a plan, a canal: Panama"

def pdrome(string):
    w = ""
    for letter in string:
        w = letter + w
    
    if (string == w):
        print("True")
    else:
        print("False")
print(pdrome("amanaplanacanalpanama"))
print(pdrome("raceacar"))
