class Solution(object):
  def diff(self, a, b):
    """
    input: int[] a, int[] b
    return: int[][]
    """
    # write your solution here
    # find the intersection
    i = j = 0
    m = len(a)
    n = len(b)
    lst = []
    while i < m and j < n:
      if a[i] < b[j]:
        i += 1
      elif a[i] > b[j]:
        j += 1
      else:
        lst.append(a[i])
        i += 1
        j += 1
    # remove the common elements from the two lists
    for k in lst:
      a.remove(k)
      b.remove(k)
  # space cost, try to find another way 
