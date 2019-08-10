class Solution(object):
  def allTriples(self, array, target):
    """
    input: int[] array, int target
    return: int[][]
    """
    # write your solution here
    array.sort()
    res = []
    i = 0
    n = len(array) - 2
    while i < n:
    
      l = i + 1
      r = len(array) - 1
      
      while l < r:
        if array[i] + array[l] + array[r] == target:
          res.append([array[i], array[l], array[r]])
          l += 1
          r -= 1
          while l < r and array[l] == array[l - 1]:
            l += 1
          while l < r and array[r] == array[r + 1]:
            r -= 1
        elif array[i] + array[l] + array[r] < target:
          l += 1
        else:
          r -= 1
      i += 1
      while i < l and array[i] == array[i - 1]:
        i += 1
      
    return res

