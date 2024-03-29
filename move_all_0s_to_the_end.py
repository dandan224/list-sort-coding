class Solution(object):
  def moveZero(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if not array or len(array) == 0:
      return []
    #verify the start is 0 or not

    # i is mutable
    count = 0
    for i in range(len(array)):
      if array[i] != 0:
        array[count] = array[i]
        count += 1


    while count < len(array):
      array[count] = 0
      count += 1
    return array
    
 
 ###Solution #2(keep the nonzero element original order):
 def moveZerosToEnd (arr, n): 
  
    # Count of non-zero elements 
    count = 0; 
  
    # Traverse the array. If arr[i] is non-zero, then 
    # swap the element at index 'count' with the 
    # element at index 'i' 
    for i in range(0, n): 
        if (arr[i] != 0): 
            arr[count], arr[i] = arr[i], arr[count] 
            count+=1
