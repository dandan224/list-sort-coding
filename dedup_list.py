###Solution #1(inplace):
class Solution(object):
  def dedup(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if len(array) == 0 or len(array) == 1:
      return array
    j = 1
    
    for i in range(1, len(array)):
      if array[i] != array[i - 1]:
        array[j] = array[i]
        j += 1
    
    
    return array[:j]
    
# Solution2: create a new temp list
