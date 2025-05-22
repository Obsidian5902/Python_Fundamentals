# we created car and webBrowser modules in the favOject package................................
# access a python package via different import statements....
from favObjects.car import *
from favObjects import webBrowser as web
my_car = car("hondaCity", "BH77", 2011)

print(my_car.__dict__) 

# use the classes in the package to create objects to perform operations................................................................

tor = web.webBrowser("google.com")
print(tor.__dict__)






