def reverseParentheses(s):
  for i in range(len(s)):
        if s[i] == "(":
            start = i
            print (s[:start])
        if s[i] == ")":
            end = i
            print (end)
            return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
  return s

'''
You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. 
It is guaranteed that the parentheses in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. 
The results string should not contain any parentheses.

Example:
  For string s = "a(bc)de", the output should be reverseParentheses(s) = "acbde".
  
  For Input: s: "a(bcdefghijkl(mno)p)q"
  Expected Output: "apmnolkjihgfedcbq"

'''
