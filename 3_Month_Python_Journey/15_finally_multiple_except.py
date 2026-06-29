def add_num (a , b):
    try:
        result = a + b
        return result
    except ValueError:
        print ("Enter valid Number")
    finally:
        print("Attempted Failed!")

print (add_num(10 , 20))


# finally always runs regardless the result true or false.

try:
    age = int (input ("Enter your age please :"))
    if age == 18 and age > 18:
        print ("you are eligible for vote.")
    else:
        print ("you are not eligible for vote.")
except ValueError:
    print("Enter a valid value please")
finally:
    print("Everything is done")

try:
    print ("Division")
    a = int (input ("Enter a first Number: "))
    b = int (input ("Enter a second Number:"))
    result = a / b
    print (f"your result for division is {result}")
except ValueError:
    print("Enter a valid integer value")
except ZeroDivisionError:
    print ("Zero division is not allowed in mathematics")

except Exception as e:
    print (f"Unexpected error occoured {e}")

finally:
    print("Everything is OK")