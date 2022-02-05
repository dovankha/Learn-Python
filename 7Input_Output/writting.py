# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

# with open(r"D:\Coding\Python\7Input_Output\cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)
        

# cities = []
# with open(r"D:\Coding\Python\7Input_Output\cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n')) # city.script('\n'): cat bo \n truoc khi dua vao mang

# print(cities)
# for city in cities:
#     print(city, end='')


# imelda = "a", "b", "2020", ((1, "c"), (2, "d"), (3, "e"), (4, "f"))

with open(r"imelda3.txt", 'r') as imelda_file:
    # print(imelda, file=imelda_file)
    contents = imelda_file.readline()
imelda = eval(contents)
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)