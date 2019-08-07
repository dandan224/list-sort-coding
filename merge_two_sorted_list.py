class Solution(object):
  def merge(self, A, m, B, n):
    """
    input: int[] A, int m, int[] B, int n
    return: int[]
    """
    # write your solution here
    i = j = 0
    res = []
    while i < m and j < n:
      if A[i] < B[j]:
        res.append(A[i])
        i += 1
      elif A[i] > B[j]:
        res.append(B[j])
        j += 1
      else:
        res.append(A[i])
        res.append(B[j])
        i += 1
        j += 1
    while i < m:
      res.append(A[i])
      i += 1
    while j < n:
      res.append(B[j])
      j += 1
    return res
