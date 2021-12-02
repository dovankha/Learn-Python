for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:10}". format(i, i**2, i**3))

for i in range(1, 13):
    print("No. {0:>2} squared is {1:<3} and cubed is {2:^4}". format(
        i, i**2, i**3))

print(len("3.142857142857143"))
print("1 Pi is approximately {0:12}".format(22/7))
print("2 Pi is approximately {0:17.12f}".format(22/7))
print("3 Pi is approximately {0:12.50}".format(22/7))
print("4 Pi is approximately {0:52.50f}".format(22/7))
print("5 Pi is approximately {0:62.50f}".format(22/7))
print("6 Pi is approximately {0:72.50f}".format(22/7))
print("7 Pi is approximately {0:72.54f}".format(22/7))
print(f"8 Pi is approximately {22/7:1.50f}")
print("9 Pi is approximately %60.50f" % (22/7))