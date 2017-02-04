print('Welcome to the Mad Lib Generator!')
adjective1 = raw_input('Type in an adjective: ')
name = raw_input('Type in the first name of a woman musician: ')
adjective2 = raw_input('Type in another adjective: ')
adjective3 = raw_input('And another adjective: ')
plural_animal = raw_input('Type in a plural of an animal: ')
beverage = raw_input('Type in a beverage: ')
adjective4 = raw_input('And yet another adjective: ')
plural_noun = raw_input('Type in a plural of any noun: ')
verb = raw_input('Type in a verb: ')
plural_body_part = raw_input('Type in a plural of a body part: ')

#adjective1 = 'fearless'
#adjective2 = 'gooey'
#adjective3 = 'sassy'
#adjective4 = 'fancy'

#plural_animal = 'elephants'
#verb = 'skip'
#plural_noun = 'marbles'

#name = 'Ani'
#beverage = 'chocolate milk'
#plural_body_part = 'knees'

print
print('Excellent choices! Here\'s your story:')
print('--------------------------------')
print("There once was a " + adjective1 + " programmer named " + name + " who wanted to build a " + adjective2 + " mobile app to help " + adjective3 + " " + plural_animal + " find new homes.")
print
print(name + " stayed up all night, drinking lots of caffeinated " + beverage + " as she worked and worked, trying to complete her " + adjective4 + " program.")
print
print("Whenever " + name  + " hit a dead end, she would exclaim " + plural_noun + "! But she was not discouraged, and after a quick break to " + verb + " and clear her head, she got back to work.")
print
print("By morning, when the sun started to rise, she let out a big yawn and stretched her " + plural_body_part + ". Finally, she was done.")
print('--------------------------------')
