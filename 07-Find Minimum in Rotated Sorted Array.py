#Leet code 153

def minimum(num):
  low, high =  0 , len(num)-1
  while low<high:
    if num[low] < num[high]:
      return num[low]
    mid =(low+high) //2

    if num[mid] > num[high]:
      low = mid +1
    else:
      high = mid
  return num[low]

if __name__ == "__main__":
  value = minimum([6,4,3,2,1])
  print(value)
