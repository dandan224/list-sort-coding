class Solution(object):
  def smallerPairs(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    array.sort()
    i, j = 0, len(array) - 1
    count = 0
    while i < j:
      if array[i] + array[j] < target:
        count += (j - i)
        i += 1
      else:
        j -= 1
    return count
