###Solution #1:
class Solution(object):
  def threeSumSmaller(self, num, target):
    """
    input: int[] num, int target
    return: int
    """
    # write your solution here
    count = 0
    for i in range(0, len(num) - 2):
      for j in range(i+1, len(num) -1):
        for k in range(j + 1, len(num)):
          
          if num[i] + num[j] + num[k] < target:
            count += 1
    return count
    
# Solution #2
