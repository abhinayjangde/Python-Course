age = 8
ticket_price = 12 if age >= 10 else 8
print(ticket_price)

isSunday=False

if isSunday:
    print(f"Today is Sunday and your age is {age} and ticket price is: ${ticket_price-2}")
else:
    print(f"Ticket price is ${ticket_price} and age {age} ")