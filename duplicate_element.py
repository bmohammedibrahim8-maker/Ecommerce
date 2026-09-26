a = [10, 20, 30, 20, 40, 10, 50]

duplicates = set()

for i in a:
    if a.count(i) > 1:
        duplicates.add(i)

print("Duplicate elements:", duplicates)