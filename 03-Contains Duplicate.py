  #Leet code 217 contain Duplicate

def containDuplicate(nums):
  present={}
  for i in nums:
    if i i present:
      return True
    present[i]=1
  return False

if __name__ =="__main__":
  value = containDuplicate([1,2,3,1])
  print(value)
