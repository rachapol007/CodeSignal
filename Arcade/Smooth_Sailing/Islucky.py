def isLucky(n):

  p1 = list(str(n))
  p2 = list()
  p3 = list()
  R = int(len(p1)/2)

  for i in range(0, int(len(p1)/2)):
    p2.append(int(p1[i]))
    value1 = sum(p2)
    
  for i in range(int(len(p1)/2), int(len(p1))):
    p3.append(int(p1[i]))
    value2 = sum(p3)
    
  if value1 == value2:
    return True
  else:
    return False

'''
Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.

Example:
  For n = 1230, the output should be isLucky(n) = true;
  For n = 239017, the output should be isLucky(n) = false.

'''
