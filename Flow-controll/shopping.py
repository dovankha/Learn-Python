shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item != "spam":
        print("Buy " + item)

print("--" * 10)

for item in shopping_list:
    if item == "spam":
        # continue
        break
    print("Buy " + item)