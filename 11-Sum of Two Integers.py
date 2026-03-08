#leet code 371

def getSum(a,b):
  list = [a,b]
  return sum(list)

#another method
def getSum(a,b):
  while b != 0:
    sum = a^b
    a = sum
    b = carry
  return a

if __name__ == "__main__":
  print(getSum(5,6))
