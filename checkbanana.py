#First open the file
#Read line by line the file and convert each line in list
#Add each element of the lists in the diccionary
#Convert each element of the diccionary in lowercase
#Associate to each key of the diccionary a value like a number (this number is how many times the word appeared)
#Display the value of the key is banana

import csv

def create_dictionary_from_file(path):
    # Open the file and read it
    with open(path, "r") as csvfile:
        lines = csv.reader(csvfile) #each line is convert in list
        mydictionary = dict()

        for line in lines:
            for i in range(0, len(line)+1):
                word = line[i].strip()
                word = line[i].lower()
                if (word not in mydictionary):
                    mydictionary.add(word)
                    mydictionary[word] = 1 # the value of each key will be a number (kind of counter)
                else:
                    mydictionary[word] += 1
    return mydictionary


banana_dictionary = create_dictionary_from_file("checkbanana.txt")

number_banana = banana_dictionary[banana]
print (number_banana)
