pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
# sorted = sorted(numbers) # chỗ này biến sorted bị trùn g từ khoá, nên ở dòng 14 sẽ bị lỗi nếu chạy
# print(sorted)
# chỗ này biến sorted bị trùng từ khoá, nên ở dòng 14 sẽ bị lỗi nếu chạy
sorted_number = sorted(numbers)
print(sorted_number)
print(numbers)  # không còn bị thay đổi, vì dùng sorted()

numbers.sort()
print(numbers)
print(sorted)

# key = str.casefold : dùng để sắp xếp a-z
# Nếu ko có key = str.casefold thì các chữ IN HOA sẽ được sắp trước
missing_letter = sorted(
    "The quik brown fox jumped over the lazy dog", key=str.casefold)
print(missing_letter)

name_list = ["Kha",
             "Trung",
             "hoat",
             "vuong"]
name_list.sort(key=str.casefold)            
print(name_list)
