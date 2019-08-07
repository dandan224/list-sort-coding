class Solution(object):
  def pairs(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    # first solution(two loops)
    array.sort()
    i = 0
    j = 1
    count = 0
    n = len(array)
    if n == 2 and array[1] - array[0] == target:
      return 1 
    for i in range(n):
      for j in range(i+1, n):
        if array[j] == array[i] + target:
        # can use binary search
          count += 1
    
    return count
    # time: O(n*n)
