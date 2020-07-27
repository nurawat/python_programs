# Python Program to check Armstrong Number
# Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
# Example:

# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153

# Input : 120
# Output : No
# 120 is not a Armstrong number.
# 1*1*1 + 2*2*2 + 0*0*0 = 9

# Input : 1253
# Output : No
# 1253 is not a Armstrong Number
# 1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723

# Input : 1634
# Output : Yes
# 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634

def checkIfArmstrongNumber(number, sumOftheNumber):
  if (number == sumOftheNumber):
    print("{0} is an Armstrong Number".format(number))
  else:
    print("{0} is NOT an Armstrong Number".format(number))

def indexNumber(number):
  number = number %10
  return number

def armstrong(number):
  sumOftheNumber = 0
  length = len(str(number))
  temp = number
  for i in range(length):
    index = int(indexNumber(temp))
    sumOftheNumber += int(pow(index, length))
    temp /= 10  

  checkIfArmstrongNumber(number, sumOftheNumber)

number = int(input("Enter the Number: "))
armstrong(number)
