menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["spam", "bacon", "sausage", "spam"]
]

for meal in menu:
    value = ", ".join((item for item in meal if meal != "spam"))
    print(value, end=' ')