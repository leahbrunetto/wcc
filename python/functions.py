def multiply(a, b):
    result = a * b
    return result
#
# solution = multiply(4, 5) # Invoke multiply giving it the arguments 4 and 5
# print(solution) # Expected: 20

# print(multiply(6, 3))

# multiply(4, 5) #expected: no result

# print(multiply(9,11)) # 99
# print(multiply(-1, -55)) # 55
#print(multiply(1, -55))
#print(multiply(3, 'Hello')) # 'HelloHelloHello'
#print(multiply(0.5, 3))
#print(multiply(0, 1))

def isPositive(a):
    if a > 0:
        return True
    else:
        return False
        
#print(isPositive(-1))
#print(isPositive(0))
#print(isPositive(500))

# Import statements should always be at the top of your file, not in the body of functions
import random

def draw_random_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    random.shuffle(cards)
    return cards.pop()

# Test the function
# print(draw_random_card()) # Expected: Random number b/n 1 & 11
# print(draw_random_card())
# print(draw_random_card())

# def display_winner(winner, msg):
#     if winner == 'Player':
#         outcome = 'You win! '
#     else:
#         outcome = 'Computer wins! '
#
#     print(outcome + '(' + msg + ')')
#
# display_winner('Player', 'You were closest to 21')
# display_winner('Computer', 'It was closest to 21')
# display_winner('Computer', 'You busted')

def cube(a):
    product = a * a * a
    return product
#
# print(cube(3))

def calculate_lucky_number(birth_month, birth_day):

    lucky_number = birth_month;

    if birth_month in [2, 4, 6]:
        lucky_number = birth_month + birth_day
        return lucky_number
    elif birth_month in [8, 10, 12]:
        lucky_number = (birth_month * 10) - birth_day
        return lucky_number

    return lucky_number * 2

#print(calculate_lucky_number(11, 10))

# def isPositive(a):
#     if a > 0:
#         return True
#     else:
#         return False
        
def isPositive(a):
    return a > 0
        
#print(isPositive(5))

def mystery(x, y, z):
    return x + y*z

# Test this function:
#print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
#print mystery('Goodbye', 2, '@') # Expected: 'Goodbye@@'

def calculateTip(price, rating):
    if rating == 'A':
        return price * 0.2
    elif rating == 'B':
        return price * 0.18
    else:
        return price * 0.15

#print(calculateTip(30.50, 'C')) # Expected: 4.575
#print(calculateTip(15.00, 'B')) # Expected: 2.7
print(calculateTip(20.00, 'A')) # Expected: 4

# Alternative solution
# def calculate_tip(meal_price, rating):
#
#     if rating == 'A':
#         tip_percentage = .20;
#     elif rating == 'B':
#         tip_percentage = .18;
#     else:
#         tip_percentage = .15;
#
#     # Calculate the tip amount by multiplying the meal price by the tip percentage
#     tip_amount = meal_price * rating;
#
#     return tip_amount