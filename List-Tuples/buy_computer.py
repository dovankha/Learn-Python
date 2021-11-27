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
        index = int(current_choice) - 1 # mảng bắt đầu từ ví trí 0, ép kiểu int rồi trừ đi cho 1
        chosen_part = available_parts[index] # gán phần tử tại index vào biến chosen_part
        if chosen_part in computer_parts:
            # nếu đã chọn part của computer rồi thì bỏ qua (remove cái vừa chọn)
            print("Removing {} ...".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {} ...".format(current_choice))
            computer_parts.append(chosen_part) # đưa phần tử chosen_part vào mảng computer_parts
        print("Your list now containes: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for part in available_parts:
            print("{0}: {1}".format(available_parts.index(part) + 1, part))
    current_choice = input()

else:
    print('Computer parts list: ', computer_parts)
