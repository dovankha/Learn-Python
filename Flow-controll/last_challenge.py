# print("Please choose your option from the list below: "
#       "\n1. Learn Python"
#       "\n2. Learn Java"
#       "\n3. Go Swimming"
#       "\n4. Have dinner"
#       "\n5. Go to bed"
#       "\n0. Exit")
# print()
# print("Please enter your choice: ")

# while True:
#     choice = int(input())
#     if choice == 0:
#         break
#     elif (choice < 0 or choice > 5):
#         print("Your choice invalid. Please enter again.")
#     elif choice in (1, 2, 3, 4, 5):
#         print("You chose {}.".format(choice))
#     else:
#         print("Please choose your option from the list below: "
#               "\n1. Learn Python"
#               "\n2. Learn Java"
#               "\n3. Go Swimming"
#               "\n4. Have dinner"
#               "\n5. Go to bed"
#               "\n0. Exit")

choice = "-"
while choice != "0":
    if choice in "12345":
        print("Your chose {}".format(choice))
    else:
        print("Please choose your option from the list below: "
              "\n1. Learn Python"
              "\n2. Learn Java"
              "\n3. Go Swimming"
              "\n4. Have dinner"
              "\n5. Go to bed"
              "\n0. Exit")
    choice = input()
