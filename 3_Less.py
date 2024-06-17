# #first use for and local function
# def oneVersion():
#     word = input("Enter your word: ").lower()
#     output = ''
#     for _ in range(3):
#         output += word
#     print(output)
# oneVersion()

# # first use While and local function
# def twoVersion():
#     word = input("Enter your word: ").lower()
#     output = ''
#     count = 0
#     while count < 3:
#         output += word
#         count += 1
#     print(output)
# twoVersion()

# # first use lambda and local function
# def threeVersion():
#     a= input("Enter your word: ").lower()
#     x =lambda a:a*3
#     print(x(a))
# threeVersion()

# #Second task
# def weightOnMoon():
#     weight_on_moon = lambda weight_on_earth: weight_on_earth / 6
#     weight_on_earth = int(input("Enter your weight on Earth (in kg): "))
#     moon_weight = weight_on_moon(weight_on_earth)
#     print("Your weight on the moon would be:", moon_weight, "kg")
# weightOnMoon()

#Third Task
def calculator():
    while True:
        # Take user input for the calculation
        num1 = input("Enter the first number: ")
        operation = input("Enter the operation (+, -, *, /, ^): ")
        num2 = input("Enter the second number: ")
        if not (num1.isdigit() or (num1[1:].isdigit() and num1[0] == '-') and
                num2.isdigit() or (num2[1:].isdigit() and num2[0] == '-')):
            return "Invalid numbers! Please enter valid numeric values."

        num1 = float(num1)
        num2 = float(num2)

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Error: Division by zero!"
            result = num1 / num2
        elif operation == '^':
            result = num1 ** num2

        return result
result = calculator()
print(result)
