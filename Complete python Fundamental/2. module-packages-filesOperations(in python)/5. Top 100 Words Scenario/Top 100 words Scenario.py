import string
def remove_punctuation(st, case = "a"): #remove puntuation and save as a list of words................................................................
    # import string
    for c in string.punctuation:
          st = st.replace(c, "") 
    if case == "a": # for printing all letters as it is................................................................
           return st.split()
    if case == "l": # for in lower case letters.................................
           st = st.lower()
           return st.split()
    if case == "u": # for in uppercase letters................................................................
           title_words = []
           for word in st.split():
                if word.istitle():
                    title_words.append(word)  
           return title_words 



def frequency_dictionary(words): # making a dictionary where each word is a key that has a value of how many times the word repeats....
     unique_words = []
     for word in words:
          if word not in unique_words:
               unique_words.append(word)
     freq_dict = {}
     for word in unique_words:
          freq_dict[word]= words.count(word)
     return  freq_dict

# filter include option to filter out all the common words....
def strip_common_words(words):
     uniques = []
     common_words = open("common_words.txt", "r")
     common_words = common_words.read()
     for word in words:
          if word not in common_words:
               uniques.append(word)
     return uniques
          

def print_ranked_dictionary(dictionary, count = 7): # print ranked option to filter out al the common words................................................................
    rankedList = sorted(dictionary, key = dictionary.get, reverse=True)
    for i in range(0, count):
         print(rankedList[i],  "repeats", dictionary[rankedList[i]], "times")


       # completed code understood but whats the use of text file i.e. common_words.txt overe here......?????? we only used the HarryPotter.txt here.....
# Read the file................................................................\
def main():
    text = open('HarryPotter.txt', "r")
    text =text.read()
    word_list = remove_punctuation(text, "u")
    uniques = strip_common_words(word_list)
    # print(word_list)
    
    dictionary = frequency_dictionary(uniques)
    # dictionary = frequency_dictionary(word_list)
    # print(dictionary)
    print_ranked_dictionary(dictionary)


main()