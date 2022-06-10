names = ["Dima", "Sasha", "Vania", "Tania"]

print("Out source names:")
for name in names:
    print(name)
print("\n\n")


data = iter(names)
print("Out iter names:")
# next(data)
# data.__next__()

while True:
    try:
        print(data.__next__())
    except StopIteration:
        break
