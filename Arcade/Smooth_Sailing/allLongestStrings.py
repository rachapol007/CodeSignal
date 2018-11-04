def allLongestStrings(inputArray):
    result = list()
    Max = max(inputArray, key=len)
    z = 0
    z = len(Max)
    #print(Max)
    r = len(inputArray)
    for i in range (r):
      if len(inputArray[i]) >= z:
        result.append(inputArray[i])
      else:
        P = 0
    
    return result
    
    
'''
Given an array of strings, return another array containing all of its longest strings.

Example:
  For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

  For inputArray: ["abc", "eeee", "abcd", "dcd"]
  Expected Output: ["eeee", "abcd"]

'''
