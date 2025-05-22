#open and read a text file................................................................
text = open("harrypotter.txt", 'r')
text = text.read()

# print a text file................................................................
# print(text)
# perform the basic operation on the content----------------------------------------------------------------
sentences =  text.split(".")
for sentence in sentences:
    if "Harry" in sentence:
             print(sentence)












