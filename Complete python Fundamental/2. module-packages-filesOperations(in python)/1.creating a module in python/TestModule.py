"""
import myModule

r = float(input("pls enter radius: -"))

print("the circumference of the circle with radius", r, "is :", myModule.circumference(r))
print("the area of the circle with radius", r, "is :", myModule.area(r)) # just import the data from mymodule and print it in TestModule...
"""

# second method for importing the data from myModule.. 
from myModule import*
r = float(input("pls enter radius: -"))

print("the circumference of the circle with radius", r, "is :",circumference(r)) # r = radius(it knows that automatically..., circumference(radius))
print("the area of the circle with radius", r, "is :", area(r)) # just import the data from mymodule and print it in TestModule directly...


















