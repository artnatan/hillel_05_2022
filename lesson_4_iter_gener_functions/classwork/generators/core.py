def foo(start: int):
    yield start + 10
    yield start + 20


bar = foo(20)
bar2 = foo(40)

# for i in bar:
# for i in foo():
#     print(i)

for i in bar:
    print(i)

for i in bar2:
    print(i)
