import csv

def create_dictionary_from_file(path):

    with open (path, "r") as csvfile:
        lines = csv.reader(csvfile)
        banana_dictionary = dict()

        for line in lines:
            for i in range (0,len(line)):
                word = str(line[i]).strip()
                word = word.lower()

                if (word not in banana_dictionary):
                    banana_dictionary[word] = 1
                else:
                    banana_dictionary[word] += 1
    return banana_dictionary


mydictionary = create_dictionary_from_file("checkbanana.txt")
print (mydictionary["banana"])
