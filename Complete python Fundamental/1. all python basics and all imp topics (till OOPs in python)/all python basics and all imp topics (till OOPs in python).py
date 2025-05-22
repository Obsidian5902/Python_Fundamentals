# print("hello-world")


"""
# User Input
print(" Hello Mr., whats Your Name")
Name = input()
print(" hello " + Name)
print(" So" , Name, " what Are You Doing")
reply = input()
print("How about you")
reply2 = input()
print(" yeah! Well Same as you", reply2)

print("whats your age?")
age = input()
age = int(age) # very important to define the age variable as integer...
print(" I am " , age , " years old")
print(" So next year you will be", age+1, " years old")

"""





"""
'''
  (its a documentation Strings(docString), a type of comment in python) both can be used(""" """/''' '''')
 '''
 """



# import sys # to get arguments from the command prompt...
# print("______________________")
# print("First Name",sys.argv[1])
# print("Last Name",sys.argv[2]) # you need to run that mannually using terminal or command-prompt....
# print("______________________")




# nameing identifiers(these are variables, functions etc in which we stores values)..
# Dollars = 'harsh'
# print(Dollars) 




'''
 ------- operations --------------------------------
# addition(+)
# subtract(-)
# multiply(*)
# divide(/)
# Exponent(**)
# floor division(//)
# modulus(%) : -  (gives remainder)


# print(5 + 5)

a = 4
b = 5
print(a*b)
print(a/b)
print(a-b)
print(a%b)
print(4*a-b)
c = a + b /3
print(c*c)
print(c)
print(c**3)

'''






'''
----------------------------------------------------------------------------------------------------------------------------------------
# --------Variables---------
Base = 44
height = 44

Area = Base * height
# print(Area)
# ---- or------
# for convenient output..
print("A triagle whose base", Base, "With height", height, " and Area Will be", Area)
'''





'''
# floor division(//)........
print(" Enter the number of Days")
days = int(input())
Years = days // 365
r = days % 365
weeks = (days % 365)//7
days_remaining = days - Years*365 - weeks*7
print(Years, "Years")
print(weeks, "Weeks")
print(r, "days")
print(days_remaining, "Days remaining")
'''






# binary/ octal/ Hexadecimal numbers: - - - - - - - -
# num = 23
# print(bin(num))
# print(oct(num))
# print(hex(num))
# print(float(num))

# i = int('10001',2) # binary to decimal
# i = int('27',8) # octal to decimal
# print(i)

# p = int('DC',16) # hexadecimal to decimal 
# q = int('14',16)
# r = int('3C',16)
# print(p, q, r)






# Strings ----------------------------------------------------------------

# a = 'Ram'
# b = 'Disk'
# print(8 * ( a + ' '+  b + ' ' ) + '!')
# tom = a + ' ' + b 
# tom = tom + '!' # OR tom += '!
# name = tom * 100
# print(name)




'''
# indexing and slicing in strings ----------------------------------------------------------------
Type = input('Type something that can be used to print: ')

num0 = Type[0:2] # slicing in strings
num1 = Type[2:4]
num2 = Type[4:6]
print(num0, num1, num2)

num0 = int(num0, 16 )
num1 = int(num1, 16 )
num2 = int(num2, 16 )

print(num0, num1, num2)
'''





'''
# Strings (Str.format()) -------------------------
# interpolated strings(f"")
person = 'harsh'
last_name = 'yadav'
print('my first name is', person, 'and last name is', last_name,)
print(f'my name is {person} {last_name}') # interpolated strings

#.format() -------------------------
print('my first name is {} and my last name is {}' .format(person, last_name))

# OR using %s----------------------------------------------------------------
print('my name is %s %s' % (person, last_name))

t = 'my first name is {} and my last name is {}'
print(t.format(person, last_name))
'''






# string-functions----------------------------------------------------------------
# p = 'PYthons'
# p =p.lower() # lower the whole term
# p= p.upper() # upper the whole term
# p= p.capitalize() # capitalize the first letter only..
# p = p.startswith('P') # only first letter
# p = p.endswith('P') # any from but from at the last letter...
# print(p)


# Strip-function---------------------------------------------------------------(remove specific things in the string)
# text = 'This is my first name and my last name and I have no idea what you are doing here  ...'
# print(text.strip('This'))
# print(text.strip('...'))


# replace-function---------------------------------------------------------------(replace specific things in the string)
# text = 'This is my first name and my last name and I have no idea what you are doing here  ...'
# print(text.replace('This', 'I'))
# print(text.replace('a', '^'))
# for multiple replace words in text..
# text = text.replace('a', '1')
# text = text.replace('i', '$')
# print(text)


# split and count function---------------------------------------------------------------(split the words in the string)..
# text = ' I have no, idea, what you are doing here ...'
# print(text.split( ','))
# print(text.count('o'))


# escape character---------------------------------------------------------------
# name = 'this is my home of a""ll page in the home in,  \'the director and we have to do something for this to work and no\'t just the  director itself '
# print(name)







# ---------------------------list----------------------------------
# student_name = ['harsh', 'ramhesh', 'ram', 'sham', 'kamul']
# student_Id = ['1', '2', ' 3', ' 4', ' 5']
# print(student_name + student_Id) 
# ---OR----
# student_name += student_Id

#open = list(student_name)
# student_name[5] = 'yadav'   
# print(student_name)
# print(open)




'''
#-------------------------------------list-function--------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Max_number = max(numbers)
Min_number = min(numbers)
print('Maximum number is: ', Max_number," and "'Minimum number is: ', Min_number)

Average_of_all_numbers = sum(numbers)/len(numbers)
print('The average is: -',Average_of_all_numbers)
print(sorted(numbers, reverse=True))
'''




'''
# --------------------------------------boolean-function--------------------------------

dancing = True
singing = True
chilling = True

chilling = not chilling
singing = not singing
if dancing and not chilling and not singing:
    print("studying very hard")

if not dancing or not chilling and not singing:
    print("Yes doing well")

if dancing and singing:
        print("Yoo man you got it....")
    


'''





'''
# --------------------------------Control-Statement--------------------------------
name = input('what you want to do in future: -')

if name == 'engineer':
    print('You choose the wrong path')
elif name == 'doctor':
    print('You choose the right path')
elif name == 'CA':
    print('You choose the wrong-right path')
else:
    print('No this path as', name, 'is not for you')

'''






'''
# -------------while-loop-statement-------------------
# start = 1
# finish = 1000000

# while start <= finish:
  #   print(start)
    # start = start * 1.2 # start += 1
# else:
#  print("thats the finish line")


# -------------while-If-loop-statement-------------------
print('Please enter your distance')
distance = int(input())

path = 1
while path <= distance:
    # if path and distance has no remainder
    if distance % path == 0:
        print( 'Your covered path ',path,  'is a factor of your total distance', distance) 
        path += 1 # no need to write else in here....
'''








'''
#------------------------------for-loops------------------------------

snetence = 'Nice too meet you Senor'
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']

for c in snetence: 
  print(c.upper()) # prints all the characters in the sentence..

for n in numbers:
  print('Square of number',n, 'is',n**2) # prints all the numbers in the numbers...

for l in letters:
  print(l.center(33, "*")) # prints all the letters in the letters... (here in center the 33 is width)

'''








# range functions----------------------------------------------------------------
#for i in range(0, -13, -3):
  #  print(i) 

# ---------------------------------------------------------------- 
# num = int(input('Enter any number i.e. in your mind'))
# print("the number you choose is: -",num)
# for i in range(0,10):
#    print(i*num)



'''
# number prime or not: ----------------------------------------------------------------
import time
num = int(input('Enter a number you wanna check'))

tic = time.ctime()

prime = True

for i in range(2, num):
    if num % i == 0: #  divide num by i and getting 0 as a remainder then num has a factor at least so it's not prime....
        prime = False   

toc = time.ctime()
print('time taken', tic, toc)

if prime == True:
    print(num , " is a prime number")
else:
    print(num, "is not a prime number")
'''




# ---------------------------------------------------------------- nested loops ----------------------------------------------------------------

# for i in range(0,10):
 #    for i1 in range(0,10):
   #     print(i, i1)


# ----------------------------------------------------------------
'''
cordinates = []

for i in range(0,7):
    for i1 in range(0,7):
        c = str(i) + ' ' + str(i1)
        cordinates.append(c)
print(cordinates)

'''



# ---------------------------------------------------------------- break ----------------------------------------------------------------
'''
for num in range(1, 11):
      if num == 6:
            break
      product = num-1
      print(num,'- 1 = ',  product)
print("loop completed")
'''

# ---------------------------------------------------------------- continue------------------------------------------------
'''
for num in range(1, 11):
      if num == 6:
            continue
      product = num-1
      print(num,'- 1 = ',  product)
print("loop completed")
'''

# ---------------------------------------------------------------- pass ----------------------------------------------------------------
'''
for num in range(1, 11):
      if num == 6:
            pass
      product = num-1
      print(num,'- 1 = ',  product)
print("loop completed")
'''







#----------------------------------------------------------------function------------------------------------------------
# def normal():
  #  print("normal " * 8)
# normal()

# ----------------------------------------------------------------
# def pyramid():
#    star = "@"
 #   for i in range(1,10):
  #      print(star.center(20, " "))
   #     star = star + '@@'
# pyramid()

# ---------------------------------------------------------------- OR ----------------------------------------------------------------

# def pyramid(layers):
  #  star = "@"
   # for i in range(1, layers):
    #    print(star.center(layers*2, " "))
     #   star = star + '@@'
# pyramid(10)


'''
#  ----------------------------------------------------------------
def AreaOfCircle(r):
    A = 3.1412 * r**2
    print("area is ", A)
  
AreaOfCircle(10)

# ----------------------------------------------------------------OR----------------------------------------------------------------
def AreaOfCircle(r):
    import math # for taking the exact value of pi from math library...
    return math.pi * r**2 
      
  
print(AreaOfCircle(10))

'''


'''
# ----------------------------------------------------------------
def surfaceAreaofCuboid(L,R,H):
    \'''this function takes three parameters..\''' #must be in three quatations... for doc function...
    return 2*(L*H + H*R + R*L)

print(surfaceAreaofCuboid(2,3,4,))
print(surfaceAreaofCuboid.__doc__) 
'''







# ---------------------------------------------------------------- local and global variables----------------------------------------------------------------
'''
density = [22,44,55,77,88,99,101]
locations = 'kota'

def densityOfcity(values):
    day = 1
    for value in values:
        print("day", day, "   : ", value)
        day += 1
def averageOfDensity(values):
    import math # local function scope..../variable....
    return math.fsum(values) /  len(values)


def changeLocation(new_location):
    global locations # global function scope..../variable....
    locations = new_location
    print("change location", locations)



densityOfcity(density)
print(averageOfDensity(density))
print(locations)
changeLocation("Denmark")
print(locations)
'''






'''
# --------------------------------main function --------------------------------
# with the help of main function we can run program of other files if add __name__ ="__main__".... and before that we just write import file_name
def summation(number1, number2):
    total = number1 + number2
    return total
def main():
   print("the sum of number1 and number2 is ", summation  (20, 44))

__name__ = "__main__"
main()
'''








# ------------------------------- function-arguments --------------------------------
'''
def fancyName(name):
    print("================================================")
    print("================================================")
    print("="+ name.center(46, "$") + "=" )
    print("================================================")
    print("================================================")

def fancyNameByDefArgs(name, length=50, symbol='#'):
    print(symbol*length)
    print(symbol*length)
    print("=="+ name.center(length-4, "=") + "==" )
    print(symbol*length)
    print(symbol*length)
    

fancyName(name ="Harsh")
fancyName("Yadav")

fancyNameByDefArgs("harsh", 50, "=")
fancyNameByDefArgs("Riya")
'''

# def fancyName(*names):
  #  for name in names:
   #     print("================================================")
   # print("================================================")
   # print("="+ name.center(46, "$") + "=" )
   # print("================================================")
   # print("================================================")

# fancyName("Harsh", "Yadav")








"""
# --------------------------------Anonymous-functions(Lambda Function)--------------------------------

# by lambda function find the energy E = M*c**2.....
The_result = lambda M, c : M*c**2
print("the energy is", The_result(66, 3*10**8), "joules")
# --------------------------------OR--------------------------------
The_result = lambda M, c = 3**8 : M*c**2
print("the energy is", The_result(66, 3*10**8), "joules")


# find the abbriviation of each month by lambda function....
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
abr_months =list(map(lambda months:months[:3], months))
print(abr_months)


print(type(abr_months))
print(type(The_result))

"""








'''
# ----------------------------------------------------------------Lists----------------------------------------------------------------
number_list = [1, 2, 3, 4,5,[6, 7, 8, 9, 10]]
letter_list = ["a", "b", "c", "d", "e",]

# add lists of numbers to the list of letters:-
mix = number_list + letter_list
print(mix)
# OR
letters_list = letter_list + number_list
print(letters_list)


# read the index of the lists
print(letter_list[3])
print(number_list[5][2])


# write items into lists and nested lists----------------------------------------------------------------
number_list[3] = 99
print(number_list)
'''






# ----------------------------------------------------------------List-Methods----------------------------------------------------------------

 # number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# letter_list = ["a", "c", "b", "d", "e"]

'''
list.append(item)
list.extend(iterable)
list.index(insert, item)
list.remove(item)
list.pop([index]])
list.index(item, [,start [, end]])
list.count(item)
list.sort(key=note, reverse=True)
list.reverse()
list.copy()
'''

'''
# ----------------------------------------------------------------number-append----------------
number_list.append(10.1)
print(number_list)

number_list0 = number_list.copy()
number_list0.append(10.1)
print(number_list)
print(number_list0)

number_list2 =number_list.copy()
number_list2.append(10.1)    
print(number_list2)

number_list3 =number_list.copy()
number_list3.append(10.1)
print(number_list3)

'''





#----------------------------------------------------------------extend/clear/insert----------------------------------------------------------------
# number_list.extend("number_list")
# print(number_list)
# number_list.append(letter_list)
#print(number_list)

# ----------------------------------------------------------------clear
# number_list.clear()
# print(number_list)

#----------------------------------------------------------------insert
# number_list.insert(2, "H")
# print(number_list)


#----------------------------------------------------------------remove/remove----------------------------------------------------------------
# number_list.remove(2)
# print(number_list)


#----------------------------------------------------------------pop
'''
last_number = number_list.pop()
print(last_number)
print(number_list)

first_number = number_list.pop(0)
print(first_number)
print(number_list)

'''





# index------------
# print(letter_list)
# print(letter_list.index('a')) 

#count------------ 
# print(letter_list)
# print(letter_list.count("a"))



'''
# sort/reverse------------
letter_list.sort()
print(letter_list)
letter_list.reverse()
print(letter_list)
'''



#----------------------------------------------------------------List-comprehension-------------.......
'''Syntax
variable-name = [operations   for-loop   if-statement(optional)]

'''
# cube = [num**3 for num in range(1, 10)]
# odd_cubes = [num**3 for num in range(1, 10) if num**3%2 != 0]
# even_cubes = [num**3 for num in range(1, 10) if num**3%2 == 0]
# print("The even cube are : ", even_cubes, " and ","the odd cubes are : ", odd_cubes)
# print(cube)








# ----------------------------------------------------------------Tuples ----------------------------------------------------------------
'''
# 1. create tuples.......
number_list = (1, 2, 3, 4, 5, 6, 7, 8 )
mix_list = (1, "b", 3.33)

#2. create nested / 2D tuples.....
two_D_tuples = ((2, 3), (4,5), (5,6))

#3. access the items from tuples and nested tuples....
print(mix_list[1])
print(two_D_tuples[2][1])

#4. pack and unpacking tuples......
packing_tuples = 2, "tt", 55.55
print(packing_tuples)

a, b, c = packing_tuples # unpacking tuples
print(a, b, c) #unpacking tuple
print(packing_tuples)
'''

# 5.slicing/iteration/functions/common errors(assignment, iteration) of tuples----------------------------------------------------------------
# number_lists = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# letter_lists = ("a", "b", "c", "d", "e")

#slice
#print(number_lists[1:3])
# print(number_lists[1:])
# print(number_lists[1::2]) # print difference of 2 numbers................................................................
# even_number_lists = number_lists[1::2]
# odd_number_lists = number_lists[0::2]
# print("the even numbers are: ", even_number_lists, '  ',"the odd numbers are: ", odd_number_lists)


# iterations with tuples................................................................
# for letter in letter_lists*3:
#    print(letter)

# for total_items in letter_lists + number_lists :
  #  print(total_items)

# for n in number_lists:
  #  print(n**2)


# function in tuples................................................................
# def area_and_circumference_of_cricle(radius):
  #  import math
   #  return (math.pi * radius**2, 2*math.pi*radius)

# print("(area, circumference): -",area_and_circumference_of_cricle(4), "respectively")


# common errors in tuples................................................................
#1.type_error (object doesnt support item assignment) ----->{letter_lists[2]= 'B'}
#2.type_error (object doesnt support item assignment) ----->{letter_lists +='t'}






# tuples next part------------------------
# import time
###### list of squares of first 10,000,000 numbers################################################################
# squares = [num**2 for num in range(1, 10000000)]

###### tuple of squares of first 10,000,000 numbers################################################################
# tup_squares = tuple([num**2 for num in range(1, 10000000)])
# print(squares[0:20])
# print(tup_squares[200:220])
'''
tic = time.clock()
total = 0
for i in squares:
    total += i # error in time.clock() i.e. AttributeError: module 'time' has no attribute 'clock'
toc  = time.clock()
print(i)

# conclusion: - tuples takes less memory and should process quicker than lists


print(toc - tic)
'''




'''
# ----------------------------------------------------------------tuples mathods----------------------------------------------------------------
pets = ['cat', 'tiger', 'lion']
number_lists = [1, 2, 3, 4, 5, 5, 6, 7, 8]
aliens = (0, False) 

#1. any() function
print(any(pets))
print(any(number_list))
print(any(aliens))

# .count() function
print(number_lists.count(5))
print(pets.count("cat"))
print(aliens.count(False))

# minimum()/ maximum() function
print(min(number_list))
print(max(pets))

# len() function
print(len(pets[1]))
print(len(aliens))

'''



#-----------------------------------------Dictionaries and sets----------------------------------------------------------------
# ---------------------------------1.  Dictionary{"dict":33}, here "dict" is a key and 33 is a value--------------------------------
"""
#Create a dictionary in 2 different ways:-
name = dict(
    name1 = "harsh",
    name2 = "Ram"
)
nickName = {"harsh": "Chotu", "Ram": "Ramu"}

print(name) # print dictionary first type
print(nickName) # print dictionary second type


# read a specific values from the dictionary................................
print(name["name2"])
name['name3'] = "Kabul" # adding new values in the dictionary(append)
print(name)
"""





#---------------------working with dictionary-Methods-1-------------------------------------
# letter_list = ["a", "b", "c","d","e","f"]
# scores = {
  #  "student1" : 33,
   # "student2" : 44,
    #"student3" : 55}

'''
dict.copy()
dict.update()
dict.keys() # used to know what to query
keys = dict.fromkeys(list)
scores.get("key")
min/max/len()
dict.pop()
dict.popitem()
dict.clear()
'''

#.copy() function....
# print(scores)
# find_scores = scores.copy()
# print(find_scores)




#lets make new dictionary to update new dictionary....
# new_scores = {
  #   "a": 12,
    # "b":13,
    # "c":14
# }
# scores.update(new_scores)
# print(scores)

# for updating single element in the dictionary..
# scores.update({"d":5})
# print(scores)




# forming dictionary using list using form keys fuction........
# letter_listX = dict.fromkeys(letter_list)
# print(letter_listX)




# min/max/len() functions................................................................
 
# print(min(letter_list))
# print(max(letter_list))
# print(len(letter_list))



'''
#pop() function................................................................
# letter_with_numbers = {"a":1, "b":2, "c":3,"d":4,"e":5,"f":5}
# print(letter_with_numbers.pop("a"))
# print(letter_with_numbers)

scores = {
    "student1" : 33,
    "student2" : 44,
    "student3" : 55

}

print(scores.pop("student1"))
print(scores)

print(scores.popitem())
print(scores)


print(scores.clear())

'''





#---------------dictionary-iteration--------------------------------
'''
scores = {
    "student1" : 33,
    "student2" : 44,
    "student3" : 55,
    "student4" : 155

}

#for score in scores:
    #print(score) #  print all the keys in the dictionary...

# for printing values as well
for name in scores:
    # print(name) 
    # print(scores[name]) #print all the values in the dictionary with its keys....
# ----or----
    print("the score of ", name, "is", scores[name])

'''





"""
# -------------sentence_analyzer by dictionary------------
text = "the part of my body is very big when i woke up at morning so i need to do something which is very shy stuff love your hairs baby"

def text_analyzer(text):
    solutions = {} #making an dictionary that tells no. of every letter in the text.....
    for c in text:
        c = c.upper() # for ignoring small letters.....
        if c is not ' ': # for removing spaces from the text......
            if c in solutions:
                solutions[c] += 1
            else:
             solutions[c] = 1
    return solutions
# print(text_analyzer(text))

correct_way = text_analyzer(text)
for c in correct_way:
   print("the letter ", c, "repeates", correct_way[c] , "times....")
"""

    







#---------------------------------------------------------ordered-dictionaries functions--------------------------------
# from collections import OrderedDict

# a = OrderedDict(name = 'Harsh', roles = 'lord', home = 'India')
# b ={}
# dictionary_functions = dir(b) 
# OrderedDict_functions = dir(a) 
# print(dictionary_functions) # prints all the list of functions in a dictionary...


'''
b = {}
all_functions = dir(b)
print(all_functions) # prints all the list of functions in a dictionary '''


"""
b ={}
dictionary_functions = dir(b)
for f in dictionary_functions:
    print(f.__doc__) # usind doc we can print the list of all the functions in a dictionary with explanation..
"""


"""
from collections import OrderedDict
a = OrderedDict(name = 'Harsh', roles = 'lord', home = 'India')
b ={}
dictionary_functions = dir(b)
OrderedDict_functions = dir(a) 
for f in  OrderedDict_functions:
    if  f not in dictionary_functions:
        print(f) # showing all unique fucntions in reverse dictionary
"""



# ----------------------------------------------------------------ordered-dictionaries --------------------
"""
from collections import OrderedDict
a = OrderedDict(name = 'Harsh', roles = 'lord', home = 'India')
b = OrderedDict(roles = 'lord', name = 'Harsh', home = 'India')

print(a==b) # False 
c = {'name' : 'Harsh', 'roles' :'lord', 'home' : 'India'}
d = { 'roles' :'lord', 'home' : 'India', 'name' : 'Harsh'}

print(a==c) # true (bcs python treated ordered dictionary as much as standard dictionary)
print(d==c) # true 

"""











#----------------------------------------------------------------2.SETS----------------------------------------------------------------

#create 2 sets----------------------------------------------------------------
# a = {1,2,3,4}
# b = {5,6,7,8,9,10,11,12}

# print(a, b) #print sets but we can't print each element of sets........

# for num in a:
  #  print(num)#iterate through sets and print

# add elements --------------------------------
# a.add(1.1) # add new element in set
# print(a)
# a.update(b) # print all elements in a and b including the new element 1.1--------------------
# print(a)

# remove elements --------------------------------
# a.discard(2)
# a.remove(1)
# print(a)
# print(a.pop()) # print first element of set




"""
#----------------------------------------------------------------Sets-operationa------------------------
A = {1, 2, 3}
B = {1,2,3,5,5, 6, 7}
#1. union a and b...
print(A.union(B))
#----------------------------------------------------------------OR--------------------------------
print(A|B)

#2. a intersection b ....
print(A.intersection(B))
print(A&B)

# 3. A equals b ....
print(A==B) #False

#4. subset a and b...
print("subset a and b" "and" "superset a and b")
print(A.issubset(B)) # True
print(B.issuperset(A)) # True

# frozen Set-operation...   
a = frozenset([1, 2, 3])
print(a)

"""







#---------------------------------------------------------OOP in Python----------------------------------------------------------------
#1.------------------------------------------------------ classes/ objects/attributes----------------------------------------------------------------
"""
# create a class and object and its attributes:-
class bikes():
    pass
honda = bikes() # first object of class bikes
hayabhusa = bikes()# second object of class bikes

honda.model = "NV440" # attribute of object honda in class bikes... 
honda.weight = 550

print("The model and weight of honda is :", honda.model," and ", honda.weight,"KG respectively" )
print(honda.__dict__)
print(hayabhusa.__dict__)
"""



#2.----------------------------------------------------------------The_init_method----------------------------------------------------------------
# creating the init function for class car and print each attribute accordingly........
"""
class cars:
    def __init__(self, make, model, weight, year):
        self.make = make
        self.weight = weight
        self.model = model
        self.year = year

car_info1 = cars("HONDA","NH40", 670, 2022) # object of class car
car_info2 = cars("Audi","PH00", 770, 2027) # object of class car
print(car_info1.__dict__, car_info2.__dict__)
print("the second car is", car_info2.make, "and its model is", car_info2.model)
"""




# ----------------------------------------------------------------mobile phone problem------------------------
"""

# write a class mobilePhone which has a init function with attributes for display  Size, RAM,  and Operating System,
# this class should work seemlessly with the code below to print an automated review.......... 

class MobilePhone:
    def __init__(self, dispay_size, ram, os):
        self.display_size = dispay_size
        self.ram = ram 
        self.os= os 
        

peraphone = MobilePhone(5.5, "3GB", "IOS-13.33", )
simsum = MobilePhone(5.2, "8GB", "NONA-DIMENSITY-14.00", )
print(f"The new peraphone has a {peraphone.display_size }"
      f" inch-display, With {peraphone.ram} of Ram and runs on "
      f"the latest version of {peraphone.os}. Its biggest competitor is "
      f"The simsum phone sports a similar AMOLAD, {simsum.display_size} "
      f"inch display.{simsum.ram} of RAM and runs {simsum.os}")
"""







# 3. --------------------------------Method In Classes ----------------------------------------------------
"""
# instance-method----------------------------------------------------------------
class person:
    def  __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hello ! My name is " , {self.name}, "and I am", {self.age}, "years old...") # --OR--
        # print(f"Hello ! My name is {self.name} and I am {self.age} years old...")
    
    def greet(self, person):
        if person.name == "Harsh":
            print("Hello ! My sweet neighbor", {self.name})
        else:
            print(f"Hello ! {self.name}")

harsh = person("Harsh", 21)
harsh.greet(harsh)
Gendu = person("Gendu Ji", 21)
Gendu.greet(Gendu)
"""

#----------------------------------------------------------------adding new methods and attributes----------------------------------------------------------------
"""
class cars:
    def __init__(self, make, model, weight, year, Max_Speed):
        self.make = make
        self.model = model
        self.weight = weight
        self.year = year
        self.Max_Speed = Max_Speed # creating new attribute in object car_info1 in class cars..... as Max_Speed
        self.current_speed =0
    
    def acceleration(self,  add_speed = 55): # adding new methods
        self.current_speed += add_speed
        if self.current_speed > self.Max_Speed:
           self.current_speed = self.Max_Speed



car_info1 = cars("HONDA","NH40", 670, 2022, 300)
for i in range(0, 5):
    car_info1.acceleration(130)
    car_info1.acceleration(30) #adding 30 in 130........
print(car_info1.__dict__)

car_info2 = cars("Audi","PH00", 770, 2027, 280) 
for i in range(0, 3):
    car_info2.acceleration(130)
    car_info2.acceleration(30) #adding 30 in 130........
print(car_info2.__dict__)
"""







#----------------------------------------------------------------Automated Geomertric Calculations Scenarios----------------------------------------------------------------

'''# Circle area and circumference................................................................
import math
#define the circle class and circle constructor methods..
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def circumference(self):
        return 2 * math.pi * self.radius

while True:
    radius = float(input("please enter the radius of the circle: "))
    circle = Circle(radius)
    print("Area of Circle: ", circle.area())
    print("circumference of Circle: ",   circle.circumference())
'''
# both above and below codes doing same thing........
'''
import math
#define the circle class and circle constructor methods..
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def circumference(self):
        return 2 * math.pi * self.radius

    def change_radius(self,new_radius):
        self.radius = new_radius

circle = Circle(1)
while True:
    radius = float(input("please enter the radius of the circle: "))
    circle.change_radius(radius)
    print("Area of Circle: ", circle.area())
    print("circumference of Circle: ",   circle.circumference())
'''






#----------------------------------------------------------------Class-Attributes----------------------------------------------------------------   
"""
# class-attributes----------------------------------------------------------------
class webBrowser:
    connected = True # class attribute
    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False

chrome = webBrowser("Tumbler.com")
firefox = webBrowser("Google.com")

print(chrome.__dict__)
print(firefox.__dict__)

# 1. check class attribute: -
print(chrome.connected)
print(firefox.connected)

# 2. change attribute for instance only: -
chrome.connected = False
print(chrome.__dict__)
print(firefox.__dict__)

# 3. check again after change: -
print("chrome connectes: -",chrome.connected)
print("fire-fox connecctes: -",firefox.connected)


# 4. change attribute for all instance: -
webBrowser.connected = False
print(chrome.__dict__)
print(firefox.__dict__)
# 5. check again after change: -
print("chrome connectes: -",chrome.connected)
print("fire-fox connecctes: -",firefox.connected)
"""


# 6. counting instance of class: -
"""
class webBrowser:
    connected = True # class attribute
    counter_web_browser = 0 # class variable/ attribute

    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False
        webBrowser.counter_web_browser += 1

print(webBrowser.counter_web_browser)
chrome = webBrowser("Tumbler.com")
firefox = webBrowser("Google.com")
print(webBrowser.counter_web_browser)
onion = webBrowser("onion.com")
print(webBrowser.counter_web_browser)
"""





# ------------------------------------------elevator class attribute scenario---------------------------------------------

""" ------------------------------------------ theory and steps
Attributes
Occupants attribute which 0 by  default
floor  attribute which is 0 by default

methods:
- add_occupants
- go to floor

properties
- Occupants  can only  be added if the occupants limit has not been exceeded
- only floors from  -5  to 50 exist

""" 

""" -------coding-------
class Elevator:
    occupancy_limit = 8 # class variable/attribute

    #def __init__(self, occupants = 0 ,floor = 0 ):
    def __init__(self, occupants = 0  ):
        self.floor = 0
       # self.floor = floor
        if occupants <= Elevator.occupancy_limit:
            self.occupants = occupants
        else:
            self.occupants = Elevator.occupancy_limit
            print("Out of range!!!! which is: -", occupants-Elevator.occupancy_limit, "left outside" )
    
    def add_occupants(self, num):
        self.occupants += num
        if self.occupants > Elevator.occupancy_limit:
            print("Out of range!!!! which is: -", self.occupants-Elevator.occupancy_limit, "left outside" )
            self.occupants = Elevator.occupancy_limit
    
    def remove_occupants(self, num):
        if self.occupants - num > 0:
            self.occupants -= num
        else:
            print("Elevator is empty..")
            self.occupants = 0
        

    def goto_floor(self, floor):
        if floor < - 5  or floor > 50:
            print("Out of range!!!! which is: -", floor, "floor doesnt exists here....")
        else:
            self.floor = floor

Elevator1 = Elevator(6)
Elevator1.add_occupants(7)
Elevator2 = Elevator(100)
Elevator1.remove_occupants(1)
Elevator2.remove_occupants(3)

Elevator1.goto_floor(33)
Elevator2.goto_floor(51)



print(Elevator1.__dict__)
print(Elevator2.__dict__)
        
"""



# ----------------------------------------------------------------Class Methods-----------------------------------------------------------------------------
"""
class webBrowser:
    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False
    
    def navigate(self, new_page):
        self.current_page = new_page
        if not self.is_incognito:
            self.history.append(new_page)



    def clear_history(self):
        self.history[:-1] = [] # remove everything up from the last element(current page)

    @classmethod
    def with_incognito(cls, page):
        instance = cls(page)
        instance.is_incognito = True
        instance.history = []
        return instance

chrome = webBrowser.with_incognito("Tumbler.com")
firefox = webBrowser("Google.com")
chrome.navigate("Dictionary.com")
chrome.navigate("new.com") # here we navigate dictionary.com to new.com......
# chrome.clear_history() # clears the history from the browser chrome except the current page....

print(chrome.__dict__)
print(firefox.__dict__)

"""






#----------------------------------------------------------------encapsulation and information hiding----------------------------------------------------------------
"""
class car:
    def __init__(self, make, model, year):
        self.__make = make # both __make and __year are private attributes...... they can't be changed but we can access them..
        self._model = model # singleunderscore before model(_model) shows its a protected attribute but, 1% chance of change... we can change it now by using set function...
        self.__year = year
    
    def get_make(self): # (get) for makeing private attributes accessible.....
        return self.__make
    def get_model(self):
        return self._model
    def get_year(self):
        return self.__year
    def set_model(self, new_model): # (set)for making model assessable by user and making change in it(protected attribute only like _model)....
        self._model = new_model

my_car=car("Honda", "VH55", 2002)

print(my_car._model) # protected attribute are accessible without get but private attributes are not accessible(without get method)
# print(my_car.__year)# shows no attibute error.......
print(my_car.__dict__) 
print(my_car.get_year())
my_car.set_model("VH69") # adding / changing the protected Attributes.....(_model)
print(my_car.get_model())# now we can accessing the data of make and year.... 
print(my_car.__dict__)
"""






# ----------------------------------------------------------------Class inheritance----------------------------------------------------------------
"""
class cat:
    def __init__(self, mass, lifespan, speed): # here "def" are method fucntions.....
        self.mass_in_kgs = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed
    
    def speakings_of_cat(self): 
        print("mauwwwwwmawwwwwwmawwwwwmawwwwwww")

class Leopard(cat): # child class................................................................
    def speakings_of_cat(self): 
        print("wgrrrrrrrrrrrr")  

class Tiger(cat): # child class................................................................
    def speakings_of_cat(self): 
        print("huaaaahhhhhhhhhhhhhhhhhhhrrrrrrrs")   


tom = cat(44, 33, 12) # for a random cat
tom.speakings_of_cat()
print(tom.__dict__)


tigy = Tiger(104, 133, 70) # for king of jungle tiger
tigy.speakings_of_cat()
print(tigy.__dict__)

leo = Leopard(90, 100, 150) # for fastest animal "cheetah"
leo.speakings_of_cat()
print(leo.__dict__)

"""




# -------------------------------------Overriding Methods(inheritance) ----------------------------------------------------
"""
class cat:
    def __init__(self, mass, lifespan, speed): # here "def" are method fucntions.....
        self.mass_in_kgs = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed
    
    def speakings_of_cat(self): 
        print("mauw")
    
    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
                f"weight is {self.mass_in_kgs} kgs"\
                f" and lifetime is {self.lifespan_in_years} years"\
                f" and speed is {self.speed_in_kph} kph" 
                
                       
class Leopard(cat): # child class.....
    def __init__(self, mass, lifespan, speed, spotted = True): #overridding main class i.e. "cat"....
        super().__init__(mass, lifespan, speed)
        self._spotted= spotted

    def speakings_of_cat(self): 
        print("wgrr") 

    def __str__(self): # overridding str method from main cat class to child class Leopard......
        if self._spotted == True: # adding attribute spotted and comment in it in the child class.....
            st = "spotted"
        else:
            st = " "
        return f"The {st} {type(self).__name__.lower()} "\
                f"weight is {self.mass_in_kgs} kgs"\
                f" and lifetime is {self.lifespan_in_years} years"\
                f" and speed is {self.speed_in_kph} kph"  

class Tiger(cat): # child class.....
    def speakings_of_cat(self): 
        print("huarr")   


tom = cat(44, 33, 12) # for a random cat
tom.speakings_of_cat()
print(tom) # printing the str method.....


tigy = Tiger(104, 133, 70) # for king of jungle tiger
tigy.speakings_of_cat()
print(tigy) # printing the str method.....

leo = Leopard(90, 100, 150, True) # for fastest animal "cheetah"
leo.speakings_of_cat()
# print(leo.__dict__)
print(leo) # printing the str method.....
"""



# ----------------------------------------------------------------multiple inheritance(MIXIN)----------------------------------------------------------------
"""
class MobilePhone():
    def __init__(self, memory):
        self.memory = memory

class camera:
    def takePicture(self):
        print("Say Cheese")

class CameraPhone(MobilePhone, camera):
    pass

iphone = CameraPhone("22GB")
print(iphone.memory)
iphone.takePicture()
"""





#-----------------------------------------------------------######################################--------------------------------------------------
#-----------------------------------------------------------######################################--------------------------------------------------
#-----------------------------------------------------------######################################--------------------------------------------------
#-----------------------------------------NOW THE LAST TWO TOPICS ARE IN OTHER FOLDER SO CHECK THESE BOTH TOPICS OVER THERE-------------------------
#-------------------------------------------------------IN THIS FILE THE WORK FINISHED AT OOPs Python-----------------------------------------------
#-----------------------------------------------------------######################################--------------------------------------------------
#-----------------------------------------------------------######################################--------------------------------------------------
#-----------------------------------------------------------######################################--------------------------------------------------













































