class Solution(object):
  def rainbowSortII(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if not array or len(array) == 0:
      return array
    left, right = 0, len(array) -1
    index = 0
    while index <= right:
      if array[index] == 3:
        array[index], array[right] = array[right], array[index]
        right -= 1
      elif array[index] == 0:
        array[index], array[left] = array[left], array[index]
        index += 1
        left += 1
      else:
        index += 1
    while left <= right:
      if array[left] == 2:
        array[left], array[right] = array[right], array[left]
        right -= 1
      if array[left] == 1:
        left += 1
    return array
