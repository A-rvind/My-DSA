#LeetCode #1 - Two Sum

class Sol:
  def twoSum(self, nums, target):
    store = {}
    for index, num in enumerate(nums):
      search = target - num
      if search in store:
        return [index, store[search]]
      else:
        store[num] = index

if __name__ == "__main__":
  obj = Sol()
  value = obj.twoSum([2,7,11,15],9)
  print(value)

