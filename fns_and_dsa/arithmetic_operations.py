def perform_operations(string):
    # Assume string is in the format "num1,num2"
    num1_str, num2_str = string.split(",")
    num1 = float(num1_str)
    num2 = float(num2_str)
    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)
    print("Division:", num1 / num2)

num1_str = input("Enter a number: ")
num1 = float(num1_str)
print(num1)