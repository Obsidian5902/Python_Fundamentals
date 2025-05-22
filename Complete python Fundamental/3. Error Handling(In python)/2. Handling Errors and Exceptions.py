# 1. Try-Except----------------------------------------------------------------
"""
with open("filename.txt","r") as fobile:
    for line in fobile: 

        print(line)

print("Cant Execute the command at the end of the code: : :") # gives FileNotFoundError:error and cant print that print line....
"""


"""
try:
  name_of_the_command = "cant execute"
  name_of_the_command[1]= "cant execute part 2"
  print(name_of_the_command) #print only the valid line of code and ignores the unvalid part bcs of "except".
  with open("filename.txt","r") as fobile:
    for line in fobile: 

        print(line)

except FileNotFoundError:
   print("file not found")

except NameError:
   print("unknown name used")
except TypeError:
   print("you can type an string as that was in the list")

finally: # for the printing the last line in every situation except when we got the syntax error at first part of our code...
   print("Cant Execute the command at the end of the code: : :")
"""







#2. Custom Execption................................................................
class RecipeNotvalidError(Exception):
    def __init__(self):
        self.message = "Recipe-not-valid-Error" # custom exception message


try:
    # recipe = "chapatis"
    recipe = 8988
    if type(recipe) != str:
        raise RecipeNotvalidError

except RecipeNotvalidError as e:
    print(e.message)






















