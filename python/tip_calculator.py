cost = raw_input('How much was your meal?')
tip = float(cost) * 0.2
total = tip + float(cost)
print('You should tip $' + str(tip))
print('Your total cost would be $' + str(total))

#alternative solution
#meal_price = float(raw_input('How much was your meal? '))
#tip = meal_price * .20
#total_price = meal_price + tip

#print('You should tip $' + str(tip))
#print('Your total cost would be $' + str(total_price))