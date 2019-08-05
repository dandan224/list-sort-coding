class Solution(object):
  def sort(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    for i in range(1,len(array)):
        j = i - 1
        num = array[i]
        while j >= 0 and array[j] > num:
            array[j + 1] = array[j]
            j -= 1
        array[j+ 1] = num
    return array
