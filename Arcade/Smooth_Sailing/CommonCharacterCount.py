def commonCharacterCount(s1, s2):
  p1 = list(s1)
  p2 = list(s2)
  p3 = list()
   
  if len(p1) >= len(p2):
    for i in range(len(p1)):
      for j in range(len(p2)):
        if p2[j] == p1[i]:
          p3.append(p1[i])
          p2.remove(p2[j])
          break
        else:
          p3
  else:
    for i in range(len(p2)):
      for j in range(len(p1)):
        if p1[j] == p2[i]:
          p3.append(p2[i])
          p1.remove(p1[j])
          break
        else:
          p3
  
  a = len(p3)  
  return a    
  
  '''
  Given two strings, find the number of common characters between them.

  Example:
  For s1 = "aabcc" and s2 = "adcaa", the output should be commonCharacterCount(s1, s2) = 3.
  Strings have 3 common characters - 2 "a"s and 1 "c".
  
  
  '''
