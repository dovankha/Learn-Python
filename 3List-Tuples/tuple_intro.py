t = ("a", "b", "c")
tt = 'ad'
print(type(t))
print(type(tt))

name = "Kha"
age = 15
print((name, " is", age, " years old!"))

#------ TUPLE -----------
cat = "ConMeoCon", "CatCat", 1999

print(cat)
print(cat[0])
print(cat[1])
print(cat[2])
#cat[0] = "ConMeoCha" # không thể assigment.

#Muốn thay đổi thì đổi sang list
cat1 = list(cat)
cat1[0] = "ConMeoCha"
print(cat1)

#------------- More tuple

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)

albums = [("a", "HaNoi", 34), ("b", "BinhDinh", 77), ("c", "Tp. Ho Chi Minh", 59)]
for album in albums:
    print("1: {}, 2: {}, 3: {}".format(album[0], album[1], album[2]))

for char, name, code in albums:
    print("char: {}, name: {}, year: {}".format(char, name, code))

for album in albums:
    char, name, code = album
    print("char: {}, name: {}, year: {}".format(char, name, code))