# Python Program for factorial of a number
# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.

def factorial(n):
  return 1 if (n==1 or n==0) else n * factorial(n - 1);


number = int(input("Enter the Number: "))
print("Factorial of",number,"is: ", factorial(number)) 
