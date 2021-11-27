even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print("Min even = ", min(even))
print("Max even = ", max(even))
print("Min odd = ", min(odd))
print("Max odd = ", max(odd))

print()
print("len even = ", len(even))
print("len odd = ", len(odd))

print()
print("Count charactor in string: ", "mississippi".count("iss"))

# Sorting list
even.extend(odd)
print(even)

even.sort() # sắp tăng dân
print("Tang dan - ascending", even)
another_even = even
print("Another_even: ", another_even)
even.sort(reverse=True) # sắp giảm dần
print("Giam dan - decrease", even)
print("Another_even: ", another_even) # Suprise khi nó vẫn bị đổi