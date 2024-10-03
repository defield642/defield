#Write a python program that takes an integer as input and returns an integer with reserved digit ordering
def reserved_integer(num):
    #convert integer to string and reserve it
    reserved_str = str(num)[::-1]
    
    if num < 0:
        #check if is -ive and adjust sign
        reserved_str = '-' + reserved_str[:-1]
    #convert reserved string back to integer
    reserved_num = int(reserved_str)
    return reserved_num


user_input = int(input("Enter an integer:\n"))


#call def function

reserved_int = reserved_integer(user_input)

print(f"Reserved integer is:{reserved_int}")




