def create_dictionary_from_file(path):

    car_file = open (path, "r")
    car_file = read(car_file)
    cars_dictionary = dict()

    for line in lines:

        #Delete the lines witch not possess the good informations
        if (lines % 2 == 0 ):
            lines.remove(line)

        for i in range(0,len(line)-1):
            midrange_price = line[43:47].strip() #delete space
            city_mpg = line[53:55].strip()
            highway_mpg = line[56:58].strip()

            if (midrange_price not in cars_dictionary):
                cars_dictionary[midrange_price] = set()
                cars_dictionary[midrange_price].add(line[43:47])

            if (city_mpg not in cars_dictionary):
                cars_dictionary[city_mpg] = set()
                cars_dictionary[city_mpg.add(line[53:55])

            if (highway_mpg not in cars_dictionary):
                cars_dictionary[highway_mpg] = set()
                cars_dictionary[highway_mpg.add(line[56:58])]

return cars_dictionary

#Average calculation
mydictionary = create_dictionary_from_file("93cars.data.txt")
my_dictionary[midrange_price] = sum(mydictionary[midrange_price])
my_dictionary[city_mpg] = sum(mydictionary[city_mpg])
my_dictionary[highway_mpg] = sum(mydictionary[highway_mpg])

average_midrange_price = my_dictionary[midrange_price] // len(mydictionary[midrange_price])
average_city_mpg = my_dictionary[city_mpg] // len(mydictionary[city_mpg])
average_highway_mpg = my_dictionary[highway_mpg] // len(mydictionary[highway_mpg])

#Display 3 values
print(average_midrange_price)
print(average_city_mpg)
print(average_highway_mpg)
