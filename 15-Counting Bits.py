#Leetcode 338

def Counting(n):
  count = [i, bit_count() for i in range(n+1)]
  return count

if __name__ =="__main__":
  value = Counting(5)
  print(value)
  
