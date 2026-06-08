# Pattern 1
for i in range(1, 5):
    print("*" * i)

print()

# Pattern 2
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print()

# Pattern 3
for i in range(1, 6):
    print("ABCDE"[:i])

print()

# Pattern 4
for i in range(1, 6):
    print("5" * i)

print()

# Pattern 5
for i in range(5, 0, -1):
    print("*" * i)