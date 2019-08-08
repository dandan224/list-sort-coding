# by using  three pointers, left, keep all -1 on the left, right,keep all the 1 on the right, and index
class Solution(object):
  def rainbowSort(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if not array or len(array) == 0:
      return
    left = 0
    right = len(array) - 1
    index = 0
    while index <= right:
      if array[index] == -1:
        array[index], array[left] = array[left], array[index]
        left += 1
        index += 1
        
      elif array[index] == 1:
        array[index], array[right] = array[right], array[index]
        right -= 1

      else:
        index += 1
    return array
