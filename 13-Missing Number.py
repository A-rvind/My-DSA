#Sorting
def missingNumber(nums):
  n = len(nums)
  nums.sort()
  for i in range(n):
    if nums[i] != i:
      return i
  return n


#Hash set
def missingNumber(nums):
  nums_set = set(nums)
  n = len(nums)
  for i in range(n+1):
    if i not in nums_set
    return i

#Bitwise XOR
def missingNumber(nums):
  n = len(nums)
  xorr = n
  for i  in range(n):
    xorr ^= i^ nums[i]
  return xorr

#math
def missingNumber(nums):
  res = len(nums)
  for i in range(len(nums)):
    res += i - nums[i]
  return res

if __name__ == "__main__":
  value = missingNumber([2,3,4])
  print(value)
  
   
  
