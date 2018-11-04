def adjacentElementsProduct(inputArray):
 try:
    if len(inputArray) >= 2 & len(inputArray) <=10:
      return max([inputArray[i] * inputArray[i+1]
                  for i in range(len(inputArray)-1)])
 except Exception:
  print("pass")
  
 '''
 Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example:
  For inputArray = [3, 6, -2, -5, 7, 3], the output should be adjacentElementsProduct(inputArray) = 21. 
  7 and 3 produce the largest product.
  
 Test:
  Input: inputArray: [-1, -2]
  Expected Output: 2
  
  '''
