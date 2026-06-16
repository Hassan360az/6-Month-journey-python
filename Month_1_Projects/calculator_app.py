print ("select an operation to perform calculation")

choice = int(input ("Enter your choice: \n 1: Addition 2: Subtraction 3: Multipilication 4: Division \n"))

first_num = int(input ("Enter first number for:"))

second_num = int(input ("Enter second number:"))

if choice == 1:
    result = first_num + second_num
    print ("Result :" , result)
elif choice == 2:
    result = first_num - second_num
    print( "Result :" , result)
elif choice == 3:
    result = first_num * second_num
    print ("Result :" , result)
elif choice == 4:
    result = first_num / second_num
    print ("Result :" , result)

else:
    "Select right operation Please!"

