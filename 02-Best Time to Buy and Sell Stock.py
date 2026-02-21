class Sol:
  def maxProfite(self, prices):
    min_price = float('inf')
    max_profit = 0 
    for price in prices:
      if price<min_price:
        min_price = price
      profit = price - min_price
        
        if profit > max_profit:
            max_profit = profit

     return max_profit

if __name__ =="__main__":
    obj = Sol()
    result = obj.maxProfite([1,2,3,4,5])
    print(result)
