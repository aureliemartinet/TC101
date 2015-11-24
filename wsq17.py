import csv

def create_dictionary_from_file(path):
    with open(path, "r") as csvfile:
        lines = csv.reader(csvfile) #read file and each line is convert in list
    # different type for
        movies_dictionary = dict()
        for line in lines:
            for i in range(1, len(line)):
                movie = line[i].strip()
                if (movie not in movies_dictionary):
                    movies_dictionary[movie] = set() #create an entry in the dictionary that has a set as its value
                movies_dictionary[movie].add(line[0])
    return movies_dictionary


def get_actors_union(movie1, movie2, dictionary):
    actors_union = dictionary[movie1].union(dictionary[movie2])
    return actors_union

def get_actors_intersection(movie1, movie2, dictionary):
    actors_intersection = dictionary[movie1].intersection(dictionary[movie2])
    return actors_intersection

def get_actors_symmetric_difference(movie1, movie2, dictionary):
    actors_symmetric_difference= dictionary[movie1].symmetric_difference(dictionary[movie2])
    return actors_symmetric_difference

def get_co_actors(actor, dictionary):
    co_actors = set()
    for movie in dictionary:
        if actor in dictionary[movie]:
            co_actors = co_actors.union(dictionary[movie])
    co_actors.remove(actor)
    return co_actors

mydictionary = create_dictionary_from_file("movies.txt")

test_union = get_actors_union("Mr & Mrs Smith", "Bone Collector", mydictionary)
test_intersection = get_actors_intersection("Mr & Mrs Smith", "Bone Collector", mydictionary)
test_symmetric_difference = get_actors_symmetric_difference("Mr & Mrs Smith", "Bone Collector", mydictionary)
co_actors = get_co_actors("Brad Pitt", mydictionary)

print(test_union)
print(test_intersection)
print(test_symmetric_difference)
print(co_actors)
