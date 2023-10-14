def sum_two_numbers(num1, num2):
    answer = num1 + num2
    if 120 <= answer <= 320:
        return 200
    else:
        return answer

def sum_three_numbers(num1, num2, num3):
    total = num1 + num2 + num3
    if 120 <= total <= 320:
        return 200
    else:
        return total

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

result1 = sum_two_numbers(num1, num2)
result2 = sum_three_numbers(num1, num2, num3)

print("Sum of two numbers (with range check):", result1)
print("Sum of three numbers (with range check):", result2)
