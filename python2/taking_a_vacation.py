# This project makes up the 7th lesson of CodeCademy's Python 2 course. I haven't made any notable adjustments.
# This lesson introduces functions and as such it makes use of several helper functions.

# Returns the cost of staying in a hotel for the given number of nights
def hotel_cost(nights):
  return 140 * nights

# Returns the cost of a plane ride to one of four supported cities
def plane_ride_cost(city):
  # Python does not support switch statements and I am mad about it
  
  if city == "Charlotte":
    return 183
  if city == "Tampa":
    return 220
  if city == "Pittsburgh":
    return 222
  if city == "Los Angeles":
    return 475

# Returns the cost of renting a car for the given number of days. Discounts are given based on the given number.
def rental_car_cost(days):
  price_per_day = 40
  price = 40 * days
  
  if (days >= 7):
    price -= 50
    
  elif (days >= 3):
    price -= 20
  return price

# Calculates the total cost of a trip, including a plane ride, hotel and rental car costs, and spending money
def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

# Sample use of the function
print trip_cost("Los Angeles", 5, 600)
