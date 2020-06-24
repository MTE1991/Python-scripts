question1 = int(input("How many cup of coffees do you want? >"))

cups = question1

question2 = float(input("How much does each coffee cost? >"))

cost = question2

question3 = float(input("What's the tax rate?"))

tax = question3

subtotal = cups * cost
total_tax = cups * (tax/100)
total = subtotal + total_tax

print("Subtotal =",subtotal)
print("Tax =",total_tax)
print("Total price =",total)
