#Leet code 33 
#using Single Binary search

def Srsa(nums, key):
  low = 0 
  high = len(nums)-1

  while low <= high:
    mid = low + (high -low) //2

    if nums[mid] == key:
      return mid
    if nums[mid] >=nums[low]:
      if key >= nums[low] and key <nums[mid]:
        high = mid -1
      else:
        low = mid + 1
    else:
      if key > nums[mid] and key <= nums[high]:
        low = mid +1
      else:
        high = mid+1
  return -1


if __name__ =="__main__":
  value = Srsa([4,5,6,1,2,3],6)
  print(value)
  
