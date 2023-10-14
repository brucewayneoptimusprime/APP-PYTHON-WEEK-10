def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")

reversed_string = reverse_string(string)

if is_palindrome(string):
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")

print("Reversed string:", reversed_string)
