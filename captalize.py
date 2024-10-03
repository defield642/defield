#write a program that accepts a string as input and captilizes the first letter of each world in the string and then return the result string

def Capitalizes_First_Letter(input_string):
    
    
    result_string = input_string.title()
    return result_string



name = input("Enter your name:\n")


user_input = input("Enter your String:")

result = Capitalizes_First_Letter(user_input)


print("Result=>", result)
