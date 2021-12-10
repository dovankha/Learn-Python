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