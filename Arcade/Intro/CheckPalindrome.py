def checkPalindrome(inputString):
      for i,char in enumerate(inputString):
        if char != inputString[-i-1]:
            return False
      return True

'''
Given the string, check if it is a palindrome.

Example:
  For inputString = "aabaa", the output should be checkPalindrome(inputString) = true;
  For inputString = "abac", the output should be checkPalindrome(inputString) = false;
  For inputString = "a", the output should be checkPalindrome(inputString) = true.
 
'''
