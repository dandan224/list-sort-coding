class Solution(object):
  def common(self, A, B):
    """
    input: Integer[] A, Integer[] B
    return: Integer[]
    """
    # write your solution here
    i = j = 0
    m = len(A)
    n = len(B)
    lst = []
    while i < m and j < n:
      if A[i] < B[j]:
        i += 1
      elif A[i] > B[j]:
        j += 1
      else:
        lst.append(A[i])
        i += 1
        j += 1
    return lst
    
    #Space: O(n)
    # Time: O(n)
