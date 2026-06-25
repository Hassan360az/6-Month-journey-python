def calculate_total(price, quantity, discount):
    subtotal = price * quantity        # ← yahan breakpoint laga do (red dot)
    total = subtotal - discount
    return total

result = calculate_total(100, 2, 50)