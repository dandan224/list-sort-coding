class Solution(object):
  def allPairs(self, array, target):
    """
    input: int[] array, int target
    return: int[][]
    """
    # write your solution here
    array.sort()
    res = []
    if not array: return res

    i, j = 0, len(array) - 1
    while i < j:
      if array[i] + array[j] == target:
        res.append([array[i], array[j]])
        i += 1
        j -= 1        
        while i < j and array[i] == array[i-1]:
          i += 1
        while i < j and array[j] == array[j+1]:
          j -= 1
      elif array[i] + array[j] > target:
        j -= 1
      else:
        i += 1
      
    return res
