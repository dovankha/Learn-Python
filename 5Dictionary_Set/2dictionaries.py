fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print("Keys = ", list(fruit.keys())) # show list of all keys in dictionary
# fruit.update({'lime':'a sour, green, red, blue'})
# print(fruit)
# print(fruit["lemon"])
fruit["pear"] = "an odd shape apple" # add an element into dictionary
print(fruit)
# fruit["pear"] = "great with tequila"
# print(fruit)
# del fruit["lemon"] # delete an element from dictionary
# print(fruit)
# fruit.clear()
# print("Fruit after cleared: ", fruit)
# print("Description of lemon: ", fruit.get("apple"))

'''
while True:
    dict_key = input("Enter a fruit: ")
    if dict_key == "quit":
        break
    else:
        print(fruit.get(dict_key, "We don't have a " + dict_key))
    # elif dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("We don't have a ", dict_key)

'''

# order_keys = sorted(list(fruit.keys()))
# print(order_keys)
# for k in order_keys:
#     print(k, " - ", fruit[k])
# print("-" * 40)
# print value of dictionary
for i in fruit.values():
    print(i)
print('-' * 40)
print(fruit.values()) # print value of dictionary
print(fruit.keys()) # print key of dictionary
