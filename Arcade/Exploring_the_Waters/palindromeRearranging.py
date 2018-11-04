def palindromeRearranging(inputString):
    temp={}
    for i in inputString:
        temp[i]=temp.get(i,0)+1
    return len([v for _,v in temp.items() if v%2==1])<2

'''

Given a string, find out if its characters can be rearranged to form a palindrome.

Example:
  For inputString = "aabb", the output should be palindromeRearranging(inputString) = true.

  We can rearrange "aabb" to make "abba", which is a palindrome.
'''
