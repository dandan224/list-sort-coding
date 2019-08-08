
### for loop 
class Solution(object):
  def allPairs(self, array, target):
    """
    input: int[] array, int target
    return: int[][]
    """
    # write your solution here
    res = []
    i = 0
    j = 0
    for i in range(len(array)):
      for j in range(i + 1, len(array)):
        if array[i] + array[j] == target:
          res.append([i,j])
    return res
