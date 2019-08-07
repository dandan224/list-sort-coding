class Solution(object):
  def minDistance(self, a, b, c):
    """
    input: int[] a, int[] b, int[] c
    return: int
    """
    # write your solution here
    # initialize the min difference
    import sys
    diff = sys.maxsize
    res_i = 0
    res_j = 0
    res_k = 0

    i = j = k = 0
    m = len(a)
    n = len(b)
    p = len(c)
    
    while i < m and j < n and k < p:
      #find minimun and maximum element
      minimum = min(a[i], min(b[j], c[k]))
      maximum = max(a[i], max(b[j], c[k]))

      #update the difference if the diff is less
      if maximum - minimum < diff:
        res_i = i
        res_j = j
        res_k = k
        diff = maximum - minimum
      if diff == 0:
        break
      
      if a[i] == minimum:
        i += 1
      elif b[j] == minimum:
        j += 1
      else:
        k += 1
    return abs(a[res_i] - b[res_j]) + abs(b[res_j] - c[res_k]) + abs(a[res_i]- c[res_k])
