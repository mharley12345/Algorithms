#!/usr/bin/python

import argparse
# max profit = dif(largestPrice,smallestPrice)

def find_max_profit(prices):
  
    if len(prices) < 2:
        raise Exception('Need at least two stock prices!')

    # Start minimum price marker at first price
    min_stock_price = prices[0]

    # Start off with an initial max profit
    max_profit = prices[1] - prices[0]

    # Skip first index of 0
    for price in prices[1:]:

        # Check the current price against our minimum for a profit
        # comparison against the max_profit
        comparison_profit = price - min_stock_price

        # Compare against our max_profit so far
        max_profit = max(max_profit,comparison_profit)

        # Check to set the lowest stock price so far
        min_stock_price = min(min_stock_price,price)


    return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))