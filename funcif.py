# creating a function that takes in 3 parameters and check if they are equal to eacother

def ConditionalCheck(num1,num2,num3):
    if num1 == num2 and num2 == num3:
        print(True)
    elif num2 == num1 or num1 == num3:
        print(True)
    elif num1 == int(num3) or num2 < num1:
        print(True)
    else:
        print(False)

ConditionalCheck(3,2,"3")
