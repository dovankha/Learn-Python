shopping_list = ['rice', 'spam', 'eggs', 'bread']
print(id(shopping_list))
shopping_list += 'Noodle' #kết quả sẽ không phải thêm vào mảng phần tử noodle
print(shopping_list)
print(id(shopping_list)) # ID của list sẽ không thay đổi trong 1 lần chạy
shopping_list += ['Noodle'] #thêm vào mảng phần tử noodle
print(shopping_list)

a = b = c = d = shopping_list
print(a)
print("Adding cream")
b.append("Cream")
print(b)
print(c)
print(d)