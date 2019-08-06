class Solution(object):
  def dedup(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if not array or len(array) == 0 or len(array) == 1:
      return array
    i, n = 2, len(array)
    while i < n:
      if array[i] == array[i - 2]:
        del array[i]
        n -= 1
      i += 1
    return array[:n]
