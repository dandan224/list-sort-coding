# Solution #1(by using two pointers)
class Solution(object):
  def twoDiff(self, array, target):
    """
    input: int[] array, int target
    return: int[]
    """
    # write your solution here
    n = len(array)
    i = 0
    j = 1
    while i < n and j < n:
      if target >= 0:
        if i != j and array[j] - array[i] == target:
          return [i, j]
        elif array[j] - array[i] > target:
          i += 1
        else:
          j += 1
        
      else:
        if i != j and array[i] - array[j] == target:
          return [j, i]
        elif array[i] - array[j] > target:
          j += 1
        else:
          i += 1
        
    return []
    Time: O(n)
    
    Solution#2: Two loop
    Solution#3: Binary search
    ####traverse the array from left to right, and for each element arr[i], binary search for arr[i] + n in arr[i+1..n-1]. If the element is found, return the pair.
