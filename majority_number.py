class Solution(object):
  def majority(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
  
    index = -1
    for i in range(len(array)):
      count = 0
      for j in range(len(array)):
        if array[j] == array[i]:
          count += 1
      if count > len(array) // 2:
        
        index = i
        break
    return array[index]
