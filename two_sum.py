# by using two pointers from the start and the end to scan all the elements
class Solution(object):
  def existSum(self, array, target):
    """
    input: int[] array, int target
    return: boolean
    """
    # write your solution here
    if not array or len(array)<2:
      return False
    array.sort()
    i = 0
    j = len(array) - 1
    while i < j:
      if array[i] + array[j] == target:
        return True
      elif array[i] + array[j] > target:
        j -= 1
      else:
        i += 1
    return False
