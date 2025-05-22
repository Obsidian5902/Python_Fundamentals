" we need to wirte  a function  that returns  a random generated list  of  30 floating point values  each one being between 1.10 to 1.45"
"""
import random
# print(help(random))

def random_choice():
  possiblePrice = []
  price = 1.10
  while price <= 1.45:
    price += .01
    possiblePrice.append(round(price, 2))
    #return random.sample(possiblePrice, 30) # for randomly given the float numbers, prints all 30 numbers...
# return random.choice(possiblePrice) # prints single number randomly...

print(random_choice()) """
 # OR-------------------------------- 

import random
# print(help(random))

def random_choice():
  possiblePrice = []
  price = 1.10
  output = []
  while price <= 1.45:
    price += .01
    possiblePrice.append(round(price, 2))
    for i in range(0, 30):
      output.append(random.choice(possiblePrice))
    return output

def random_choice2():
  output = []
  for i in range(0,30):
    output.append(random.randint(110,145)/100)
  return output

    
print(random_choice())
print(random_choice2    ())














