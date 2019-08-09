class Solution(object):
  def numOfTriangles(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    n = len(array)
    array.sort()
    count = 0
    # fix the first element
    for i in range(n - 2):
      k = i + 2
      # fix the second element
      for j in range(i + 1, n):
        while k < n and array[i] + array[j] > array[k]:
          k += 1
        if k > j:
          count += k - j - 1
    return count
    
    
