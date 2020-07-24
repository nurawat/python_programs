# Python Program for simple interest
# Simple interest formula is given by:
# Simple Interest = (P x T x R)/100
# Where,
# P is the principle amount
# T is the time and
# R is the rate

# Examples:

# EXAMPLE1:
# Input : P = 10000
#         R = 5
#         T = 5
# Output :2500
# We need to find simple interest on 
# Rs. 10,000 at the rate of 5% for 5 
# units of time.

# EXAMPLE2:
# Input : P = 3000
#         R = 7
#         T = 1
# Output :210

def simpleInterest(principle, rate, time):
  si = (principle * rate * time)/100
  print("Principle Interest is: {0}".format(si))

principle = float(input("Enter the Principle Amount: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the Time: "))
simpleInterest(principle, rate, time)
