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