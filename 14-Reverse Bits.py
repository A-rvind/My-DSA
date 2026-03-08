#190 leetcode

#brute force
class Sol:
  def reverserBit(self, n):
    binary = ""
    for i in range(32):
      if n & (1 << i):
        binary += "1"
      else:
        binary += "0"
    res = 0 
    for i, bit in enumerate(binary(::-1)):
      if bit == "1":
        res |= (1 << i)
    return res


#Bit manipulation
def reverseBit(n):
  res = 0
  for i in range(32):
    bit = (n >> 1) & 1
    res += (bit << (31 - i))
  return res


if __name__ == "__main__":
  obj = Sol()
  value = obj.reverseBit(432132)
  print(value)
