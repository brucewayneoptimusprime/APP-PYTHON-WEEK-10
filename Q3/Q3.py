def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to calculate its factorial: "))
result = factorial(num)
print("Factorial of", num, "is", result)
