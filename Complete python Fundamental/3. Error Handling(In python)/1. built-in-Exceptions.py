"""
# import nome # this will give the ModuleNotFoundError, bcs nome is not a existing module
names = print(input("enter the number: -"))
def names():
    # for names in range(0,10) # if you forget any comma, brackets etc then you will get syntax errors....
# for names in range(0,10): # if we misplaced the lines of codes in python then we will get IndentationError
    for names in range(0,10): 
        if names == 3:
            print("The number is  ", names)
        else:
            print("The number is other than 3 ", " i.e.", names)

names() """

"""
name = {"name": "Harshal", "Jimmy": "Harshal"}
print(name["age"]) # age is not in the dictionary "name", so it should give us the KeyError
"""

"""
a = 2
C = a + {"w", 1,2,3,4,5} # we can't add a number in the set directly, so we got(TypeError: unsupported operand type(s) for +: 'int' and 'set')........................
print(C)"""









""" 
name = {"name": "Harshal", "Jimmy": "Harshal"}
print(name.append("anything" )) # here we go the attribute-error(AttributeError: 'dict' object has no attribute 'append')///////////// need practice to understand this error.
# its a incorrect way to add values to the dictionary, we must use update instead of append...
""" 


""" 
name = {"name": "Harshal", "Jimmy": "Harshal"}

name.update({"anything"})# here we got valueError bcs we not gave the value to the key which is "anything"
print(name)  # just give the value to the key "anything" for removing this valueError...
"""


"""
list1= ["harsh"]
print(list1[1]) # here we got Index-Error: - list index out of range....
""" 

# NameError: - write any name, without defining them...
# jim

#fileNotFoundError: -
# i = open("name.txt", "r+")
