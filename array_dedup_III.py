class Solution(object):
  def dedup(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if not array or len(array) == 0 or len(array) == 1:
      return array
    j = 0
    i = 0
    n = len(array)
    while i < n:
      start = i
      i += 1
      while i < n and array[i] == array[start]:
         i += 1
      if i == start+1:
          array[j] = array[start]
          j += 1
    return array[:j]
