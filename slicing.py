prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}
min_value =min(prices, key=lambda k: prices[k])
print(min_value)


# import heapq
#
# portfolio = [
#  {'name': 'IBM', 'shares': 100, 'price': 91.1},
#  {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#  {'name': 'FB', 'shares': 200, 'price': 21.09},
#  {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#  {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#  {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# print(cheap)
# print(expensive)


