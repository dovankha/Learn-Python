data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 185, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

print("Length of data: ", len(data))

# Thử in ra vị trí của giá trị trong mảng
index = data.index(105)
print("index = ", index)
print(data[3])


# Thử xoá các giá trị trong mảng ngoài vùng [100:200]
# for i in range(len(data) - 1, - 1, - 1):
#     if (data[i] < min_valid) or (data[i] > max_valid):
#         del data[i]

# print("Data [{}]: ".format(len(data)), data)

# Dùng enumerate(reversed()) để in ngược mảng:

top_index = len(data) - 1
print("top_index = ", top_index)
for index, value in enumerate(reversed(data)):
    if (value < min_valid) or (value > max_valid):
        # index ban đầu = top_index - index(bị dịch ngược)
        # top_index = 5
        # index(revsersed) 5 4 3 2 1 0
        # index(ban đầu) = 0 1 2 3 4 5
        print(top_index - index, value)
        del data[top_index - index] # xoá các giá trị giới hạn ngoài [100:200]

print("Data [{}]: ".format(len(data)), data)