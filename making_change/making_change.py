#!/usr/bin/python

import sys

def making_change(amount, denominations):
  
  denominations = [1,5,10,25,50] 
  n=len(denominations)
  ans = []
  i = n - 1
  while(i >= 0): 
    while (V >= denominations[i]): 
            V -= denominations[i] 
            ans.append(denominations[i]) 
  
    i -= 1
  
    # Print result 
  for i in range(len(ans)): 
        print(ans[i], end = " ") 
          

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")