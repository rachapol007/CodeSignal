def avoidObstacles(inputArray): 
    jump = 2
    i = 0
    while i < len(inputArray):
        if (inputArray[i] % jump == 0):
            jump +=1
            i = 0
        else: 
            i += 1

    return jump

'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example:

  For inputArray = [5, 3, 6, 7, 9], the output should be avoidObstacles(inputArray) = 4.
  
  For Input: inputArray: [2, 3]
  Expected Output:4



'''
