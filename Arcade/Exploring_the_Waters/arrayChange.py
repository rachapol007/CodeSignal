def arrayChange(inputArray):
    i = 1
    sum = 0
    while i < len(inputArray):
        if inputArray[i] <= inputArray[i-1]:
            sum += (inputArray[i-1] - inputArray[i]) + 1
            inputArray[i] += (inputArray[i-1] - inputArray[i]) + 1 
        i += 1
    return sum
'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example:
  For inputArray = [1, 1, 1], the output should be arrayChange(inputArray) = 3.

'''
