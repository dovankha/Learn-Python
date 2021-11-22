current_choice = '-'
computer_parts = []

while current_choice != '0':
    if current_choice in '123456':
        print("Adding {} ...".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("keyboard")
        elif current_choice == '3':
            computer_parts.append("mouse")
        elif current_choice == '4':
            computer_parts.append("monitor")
        elif current_choice == '5':
            computer_parts.append("mouse mat")
        elif current_choice == '6':
            computer_parts.append("hdmi cable")

    else:
        print("Please add options from the list below:"
              "\n1: computer"
              "\n2: keyboard"
              "\n3: mouse"
              "\n4: monitor"
              "\n5: mouse mat"
              "\n6: hdmi cable"
              "\n0: to finish")
    current_choice = input()

else:
    print('Computer parts list: ', computer_parts)
