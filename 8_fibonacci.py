# Python Program for n-th Fibonacci number
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

#     Fn = Fn-1 + Fn-2
# with seed values

#    F0 = 0 and F1 = 1.


def Fibonacci(number):
  if number == 1:
    return 1
  elif number == 0:
    print("invalid number")
  else:
    return(number * Fibonacci(number - 1))

num = int(input("Enter the Number: "))
print(Fibonacci(num))
