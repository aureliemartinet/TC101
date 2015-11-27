import csv

def create_dictionary_from_file(path):
    #Open the file
    with open (path, "r") as csvfile:
    #Read line by line
        lines = csv.reader(csvfile)
        movies_dictionary = dict()
        #Go over the lines
        for line in lines:
            #Go over each element of the line
            for i in range(1,len(line)):
                movie = line[i].strip() #one element of the file
                if (movie not in movies_dictionary):
                    movies_dictionary[movie] = set() #add it the key
                movies_dictionary[movie].add(line[0]) #store the name of the actor
    return movies_dictionary


def get_actors_union(movie1, movie2, dictionary):
    actors_union = dictionary[movie1].union(dictionary[movie2])
    return actors_union

def get_actors_intersection(movie1, movie2, dictionary):
    actors_intersection = dictionary[movie1].intersection(dictionary[movie2])
    return actors_intersection

def get_actors_symmetric_difference(movie1, movie2, dictionary):
    actors_symmetric_difference = dictionary[movie1].symmetric_difference(dictionary[movie2])
    return actors_symmetric_difference

def get_co_actors(actor, dictionary):
    co_actors = set()
    for movie in dictionary:
        if actor in dictionary[movie]:
            co_actors = co_actors.union(dictionary[movie])
    co_actors.remove(actor)
    return co_actors

#Call the dictionary to answer to the questions
mydictionary = create_dictionary_from_file("movies.txt")


#Main Menu

print("Hi! This program can give you 2 informations:")
print("Option A: You want to know some informations about two movies")
print("Option B: Give me the name of an actor and find his/her co-actors")
letter = input("Type A or B in uppercase: ")

if (letter == "A"):
    print("Option AA: You want to find all the actors in two movies")
    print("Option AB: You want to find the common actors in two movies")
    print("Option AC: You want to find the actors who are in either of the movies but not both")
    letter_submenu = input("Type AA , AB OR AC in uppercase: ")

    if (letter_submenu == "AA"):
        first_movie = input("Give me your first movie: ")
        second_movie = input("Give me your second movie: ")
        result = get_actors_union(first_movie, second_movie, mydictionary)
        print(result)

    if (letter_submenu == "AB"):
        first_movie = input("Give me your first movie: ")
        second_movie = input("Give me your second movie: ")
        result = get_actors_intersection(first_movie, second_movie, mydictionary)
        print(result)

    if (letter_submenu == "AC"):
        first_movie = input("Give me your first movie: ")
        second_movie = input("Give me your second movie: ")
        result = get_actors_symmetric_difference(first_movie, second_movie, mydictionary)
        print(result)

elif (letter == "B"):
    myactor = input("Give me the name of the actor to know his co-workers (first letter firstname/ lastname uppercase please): ")
    result = get_co_actors(myactor, mydictionary)
    print (result)

else:
    print ("User error, you have to type A or B in uppercase")
