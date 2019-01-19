#1 Get the input string and store as inputstring variable
#2 reverse the string using extended slice syntax and stored as reversestring variable
#3 Compare both the variables if it is the same

#Useful refeence: 
# Reverse string in Python (5 different ways): https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/

#Vincent Kok 19th Jan 2019

inputstring = raw_input("\nPlease give me a word:")

reversestring=inputstring[::-1]
print("Input string: {}".format(inputstring))
print("Reverse string: {}".format(reversestring))

if inputstring == reversestring:
   print("\nThe word {} is a palindrome! ({})\n".format(inputstring, reversestring))
else:
   print("\nThe word {} is NOT a palindrome! ({})\n".format(inputstring, reversestring))
