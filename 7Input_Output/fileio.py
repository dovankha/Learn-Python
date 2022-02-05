# jabber = open(r"C:\Users\khadv\Desktop\sample.txt")
# for line in jabber:
#     print(line)

# jabber.close()

# with open(r"D:\Coding\Python\7Input_Output\sample.txt") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

with open(r"D:\Coding\Python\7Input_Output\sample.txt") as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

with open(r"D:\Coding\Python\7Input_Output\sample.txt") as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')