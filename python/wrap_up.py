#print round(3.1459, 2) == 3.15
#
# def addTogether(a, b):
#     return a + b
#
# print(addTogether(9, 50))

# def getSeason(month):
#     item = month.lower()
#     winter = ['dec','jan','feb']
#     spring = ['mar', 'apr', 'may']
#     summer = ['jun', 'jul', 'aug']
#     fall   = ['sep', 'oct', 'nov']
#     if item in winter:
#         return "Winter"
#     elif item in spring:
#         return "Spring"
#     elif item in summer:
#         return "Summer"
#     elif item in fall:
#         return "Fall"
#     else:
#         return "That is not a valid month."
#
# print(getSeason("Cats"))

# def getCelsius(F):
#     C = (F - 32) / 1.8
#     return round(C, 2)
#
# print getCelsius(55)

# def getFahrenheit(C):
#     F = (C * 1.8) + 32
#     return round(F, 2)
#
# print getFahrenheit(10)

# def temperatureConverter(temp, type):
#     if type == 'C':
#         C = (temp * 1.8) + 32
#         print round(C, 2)
#     elif type == 'F':
#         F = (temp - 32) / 1.8
#         print round(F, 2)
#     else:
#         print "Error: Invalid temperature scale; Must be `F` or `C`"
#
# temperatureConverter(55, 'foo')

def vowelCounter(string):
    counter = 0
    for letter in string:
        if letter in 'aeiou':
            counter +=1
    print counter

vowelCounter("monkey")


    


    