def sortByHeight(a):
    people = iter(sorted(item for item in a if item > 0))
    return [t if t < 0 else next(people) for t in a]

'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example:
  For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

  For Input: a: [4, 2, 9, 11, 2, 16]
  Expected Output: [2, 2, 4, 9, 11, 16]

'''
