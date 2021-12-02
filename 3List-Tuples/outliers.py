data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 185, 188, 191, 350, 360]

'''
del data[0:2] # xoá 2 phần tử đầu tiên của mảng
print('data = ', data)
del data [14:] # xoá các phần tử từ vị trí 14 trở đi
print('data = ', data)
'''

min_valid = 100
max_valid = 200

print("Length of data: ", len(data))

# Thử in ra vị trí của giá trị trong mảng
index = data.index(105)
print("index = ", index)
print(data[3])

# Thử xoá các giá trị trong mảng ngoài vùng [100:200]
# Xoá nhưng bị nhảy số index, sau khi xoá thì mảng sẽ bị mất đi phần tử,
# và index trong mảng cũng cập nhật theo
# ------
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#         index -= 1

# Thử xoá các giá trị trong mảng ngoài vùng [100:200]
for i in range(len(data) - 1, - 1, - 1):
    if (data[i] < min_valid) or (data[i] > max_valid):
        del data[i]

print("Data [{}]: ".format(len(data)), data)

# Khắc phụ mảng bị nhảy index sau khi xoá:
# Xoá các phần tử giới hạn trái:
# stop = 0
# for index, value in enumerate(data):
#     if (value >= min_valid):
#         stop = index
#         break

# print("Stop: ", stop)  # debugging
# del data[:stop]
# print("Data [{}]: ".format(len(data)), data)

# # Xoá các phần tử giới hạn phải:
# start = 0
# for index in range(len(data) - 1, -1, -1):
#     if data[index] <= max_valid:
#         start = index
#         break

# print("Start: ", start) #debugging
# # vị trí start có giá trị nhỏ hơn max_valid nên mới break vòng for.
# # để xoá các giá trị lớn hơn max_valid thì từ vị trí start + 1 
# del data[start + 1:]
# print("Data [{}]: ".format(len(data)), data)

