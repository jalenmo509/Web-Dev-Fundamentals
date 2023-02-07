
for i in range(0, 151, 1):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101, 1):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(0, 500000, 1):
    if i % 2 != 0:
        sum += i
print(sum)

for i in range(2018, 0, -4):
    if i % 2 == 0:
        print(i)

low = 2
high = 9
mlt = 3
for i in range(low, high+1, 1):
    if i % mlt == 0:
        print(i)
