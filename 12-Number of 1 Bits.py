#Leetcode 191 

def hammingWeight(n:int):
  count = 0
  while n:
    n &= n-1
    count +=1
  return count

if __name__ == "__main__":
  value = hammingWeight(12)
  print(value)
