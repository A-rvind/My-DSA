#Leetcode 53

#using Kadane alog
def maxSub(nums):
  max_sum = current_sum = nums[0]

  for number in nums[1:]:
    current_sum = max(number, current_sum + number)
    max_sum = max(max_sum, current_sum)

  return max_sum

if __name__ =="__main__":
  obj = maxSub([5,4,-1,7,8])
  obj1 = maxSub([-2,1,-3,4,-1,2,1])
  print(obj)
  print(obj1)
