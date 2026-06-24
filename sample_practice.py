def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    finally:
        print("Division attempt finished.")

print(divide_numbers(10, 2))