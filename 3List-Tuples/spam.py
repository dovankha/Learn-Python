menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["spam", "bacon", "sausage", "spam"]
]

# nested list
for meal in menu:
    if "spam" in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{} has a spam score of {}".format(meal, meal.count("spam")))

# cách 1: xoá item "spam" ra khỏi list
# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]

#     print(meal)

# cách 2: in item không phải "spam"
for meal in menu:
    for item in meal:
        if item == "spam":
            print(item, end=' ')