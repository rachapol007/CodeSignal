def pixel(matrix , i ,j):
  total = 0
  
  for x in range(i-1 ,i+2):
    for y in range(j-1, j+2):
      total += matrix[x][y]
  return total // 9



def boxBlur(image):
  result = []
  row = len(image)
  col = len(image[0])


  for i in range(1, row-1):
    temp = []
    for j in range(1, col-1):
      temp.append(pixel(image,i,j))
    
    result.append(temp)

  return result

'''
Example:

For image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be boxBlur(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1.
The border pixels are cropped from the final result.

'''
