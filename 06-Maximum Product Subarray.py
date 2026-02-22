#Leetcode 152 
#Greedy approach , O(n) - time, O(1)- Space

def maxSub(nums):
  n = len(nums)
  currMax = nums[0]
  currMin = nums[0]
  maxProduct = nums[0]

  for i in range(1,n):
    temp = max(nums[1], nums[i]* currMax, nums[i]*currMin)
    currMin = min(nums[i], nums[i]*currMax, nums[i]*currMin)
    currMax = temp
    maxProduct = max(maxProduct, currMax)
  return maxProduct

if __name__== "__main__":
  value = maxSub([-2,6,-3,-10,0,2])
  print(value)
