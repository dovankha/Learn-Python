computer_parts = ['computer', 'monitor', 'keyboard', 'mouse', 'mouse mat']
for part in computer_parts:
    print(part)
print(computer_parts[3])
print(computer_parts[0:3:1])  # chỉ in tới 2 (0, 1 , 2). Bước nhảy là 1.

computer_parts[3] = "trackball"
computer_parts[3:] = "trackball" # ...'t', 'r', 'a', 'c', 'k', 'b', 'a', 'l', 'l']
computer_parts[3:] = ["trackball"]
print(computer_parts)
