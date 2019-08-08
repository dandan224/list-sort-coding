class Solution(object):
  def interleave(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if not array or len(array) == 0:
      return array
    i = 0
    j = len(array) - 1
    
    while i < j:
      if array[i] < 0:
        i += 1
      else:
        array[i], array[j] = array[j], array[i]
        j -= 1
        
    # point
    pos, neg = i + 1, 0
    while pos < len(array) and neg < pos and array[neg] < 0:
      array[neg], array[pos] = array[pos], array[neg]
      pos += 1
      neg += 2   
    
    return array
