available_parts = ['computer',
                   'monitor',
                   'keyboard',
                   'mouse',
                   'mouse mat',
                   'hdmi cable',
                   'music speaker']
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
print(valid_choices)                  
current_choice = '-'
computer_parts = []

while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {} ...".format(current_choice))
        index = int(current_choice) - 1 # mảng bắt đầu từ ví trí 0, ép kiểu int rồi trừ đi cho 1
        chosen_part = available_parts[index] # gán phần tử tại index vào biến chosen_part
        computer_parts.append(chosen_part) # đưa phần tử chosen_part vào mảng computer_parts

    else:
        print("Please add options from the list below:")
        for part in available_parts:
            print("{0}: {1}".format(available_parts.index(part) + 1, part))
    current_choice = input()

else:
    print('Computer parts list: ', computer_parts)
