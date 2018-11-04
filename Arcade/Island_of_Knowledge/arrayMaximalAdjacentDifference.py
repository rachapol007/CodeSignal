def arrayMaximalAdjacentDifference(inputArray):
  result = 0
  arrayMax = 0
  answer = []
  for i in range(len(inputArray)-1):
    if inputArray[i] >= inputArray[i+1] or inputArray[i] <= inputArray[i+1]:
      result = abs(inputArray[i] - inputArray[i+1])
      answer.append(result)
    
  return max(answer)

'''
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example:

  For inputArray = [2, 4, 1, 0], the output should be arrayMaximalAdjacentDifference(inputArray) = 3.


'''
