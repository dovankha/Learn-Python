s1 = {1, 2, 3, 4}
s2 = {1, 2, 10, 11, 12, 13}
# s1 = s1et([1, 2, 3])
s1.add(5)
s1.update([3, 4, 5, 6, 7, 8])
print(s1)

#remove() and dis1card() đều xoá 1 phần tử. remove() s1ẽ lỗi nếu phần tử đó ko tồn tại

s1.remove(3)
print(s1)
s1.discard(3)
print(s1)
s3 = s1.union(s2) # ghép 2 set lại với nhau
print(s3)

print(s1.intersection(s2, s3)) # lấy ra các phần tử cùng có ở s1, s2, s3
#or
print(s1 & s2 & s3)

# difference: trả về phần tử có trong s1 mà ko có trong s2
print(s1.difference(s2))
#or
print(s1 - s2)

# symetric_difference: trả về các phần tử ko có trong cả 2 s1, s2.
print(s1.symmetric_difference(s2))
#or
print(s1 ^ s2)