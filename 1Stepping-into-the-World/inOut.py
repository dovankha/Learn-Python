# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))

# print(num1 + num2)

# multiple input 
# x, y, z = input("Enter a two value: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)
# print("Number of the \"bede\"", z)
# print("First number is {}, second number is {} and \"bede\" is {}.".format(x, y, z))

#type casting using list() function
# x = list(map(int, input("Enter a multiple value: ").split()))
# print(x)

# x, y = [int(x) for x in input("Enter two value: ").split()]
# print("Enter Number is: ", x)
# print("Enter Number is: ", y)
# print()

# print("Do Van Kha")
# print("Kha Do Van", end="**")
# print("Van Kha Do")


# import time

# count_seconds = 3
# for i in reversed(range(count_seconds + 1)):
#     if i > 0:
#         print(i, end=">>>", flush=True) # end= thì nó sẽ in trên 1 hàng. flush sẽ in ra sau mỗi lần đếm.
#         time.sleep(1)
#     else:
#         print("Start")

#dummy file: file giả tạo, bù nhìn :))

import io
dummy_file = io.StringIO()
print("Hello world", file=dummy_file)
print(dummy_file.getvalue(),end="") # lấy giá trị từ file ảo để hiển thị ra
print('a', 'b', 'c', sep='-') #sep la separator : ngăn cách giữa các kí tự
print("khadv", end="@") # dùng đối số kết thúc @
print("DoVanKha")
print("a %d" % 3)
print("Kha {}{}".format("a", 1))