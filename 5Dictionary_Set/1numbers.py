numbers = {
    1: 'one',
    3: 'three',
    5: 'five',
    7: 'seven',
    9: 'nine'
}

print("I can count odd numbers in order")
for key in numbers:
    print(numbers[key])

numbers[8] = 'eight'
numbers[4] = 'four'
numbers[6] = 'six'
numbers[2] = 'two'

print()
print("I can count to 9 in order")
for key in numbers:
    print(numbers[key])

# Sorted
print()
print("I really can")
for key in sorted(numbers):
    print(numbers[key])
