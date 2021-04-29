# This project makes up the 9th lesson in CodeCademy's Python 2 course, which introduces lists and dictionaries. I've made minimal adjustments.
# Currently, my impression is that lists are essentially arrays and dictionaries are essentially maps.

# Represents the stock of a grocery store.
stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

# Represents the prices of items in a grocery store.
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Computes the prices of a grocery store visit based on an input list.
def compute_bill(food):
  total = 0
  for k in food:
    # if k is in stock
    if stock[k] > 0:
      # update total and reduce stock by one.
      total += prices[k]
      stock[k] -= 1
  return total

# Sample input and execution
shopping_list = ["banana", "orange", "apple"]
print compute_bill(shopping_list)
