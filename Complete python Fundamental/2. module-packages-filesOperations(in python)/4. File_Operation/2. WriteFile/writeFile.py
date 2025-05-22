# create a file that we  can write text to and write some text into it..... 
text = open('textfile.txt', 'r+')
# text.write("bcs i am batman")
for i in range(0, 100):
    text.write(str(i) + 30*" ") #  doubt 30 times spance whyyy? !!!!!!!!!!!!??????????
    text.write('\n')

text.write('The end')
text.seek(0)
text.write('The start is here')
# text.write('\n') # there is not any new line thing in a string, text file is like a string with new line characters
















