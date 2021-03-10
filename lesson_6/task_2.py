"""
Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock.
"""


def total_price(stock, prices):
	total_price = 0
	for elem in stock:
		if elem in prices:
			total_price += stock[elem] * prices[elem]
	return total_price


stock = {
	"banana": 6,
	"apple": 0,
	"orange": 32,
	"pear": 15
}
prices = {
	"banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
}

tot_price = total_price(stock, prices)
print(tot_price)


