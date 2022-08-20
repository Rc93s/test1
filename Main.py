"""
print("button1")
print("test pull")
print("this is also a test")

username = input("enter username: \n")
print("\n")
print("hello {}".format(username))
"""


DIGIT_NUMBER = 5

def returnDigitNum(num):
    if not isinstance(num, int):
        return None
    c = 0
    while num != 0:
        num = num // 10
        c += 1
    return c    

def extractDigits(num):
    if not isinstance(num, int):
        return None
    digits = []
    while num != 0:
        digits.append(num % 10)
        num = num // 10
    return digits    

 
userInput = int(input("please enter a {} digit number: ".format(DIGIT_NUMBER)))
while returnDigitNum(userInput) != 5:
    userInput = int(input("please enter a {} digit number: ".format(DIGIT_NUMBER)))
print("you entered the number:", userInput)

digits = extractDigits(userInput)

for i in range(DIGIT_NUMBER - 1, 0, -1):
    print("{}, ".format(digits[i]), end = " ")
print(digits[0])

print("the sum of digits is:", sum(digits))





  