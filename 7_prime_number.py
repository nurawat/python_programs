# Python program to print all Prime numbers in an Interval
# Given two positive integer start and end. The task is to write a Python program toprint all Prime numbers in an Interval.

# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.


def printPrime(start,end):
  for val in range(start, end + 1): 
      if val > 1: 
          for n in range(2, val//2 + 2): 
              if (val % n) == 0: 
                  break
              else: 
                  if n == val//2 + 1: 
                      print(val) 



start = int(input("Enter the Number to Start : "))
end   = int(input("Enter the Number to End   : "))
printPrime(start,end)
