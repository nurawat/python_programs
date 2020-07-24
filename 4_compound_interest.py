# Python Program for compound interest
# Compound Interest formula:

# Formula to calculate compound interest annually is given by:

# A = P(1 + R/100) t
# Compound Interest = A – P
# Where,
# A is amount
# P is principle amount
# R is the rate and
# T is the time span

# Example:

# Input : Principle (amount): 1200
#         Time: 2
#         Rate: 5.4
# Output : Compound Interest = 1333.099243


def compoundInterest(principle, rate, time):
  amount = (principle * (pow ((1 + (rate / 100)), time)))
  ci = amount - principle
  print("Principle Interest is: {0}".format(ci))

principle = float(input("Enter the Principle Amount: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the Time: "))
compoundInterest(principle, rate, time)
