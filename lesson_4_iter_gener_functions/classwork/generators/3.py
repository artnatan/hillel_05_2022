import sys

source_list = [item for item in range(10_000_000)]
source_gen = (item for item in range(10_000_000))


print("list: ", len(source_list), sep=": ")
print(sys.getsizeof(source_list))


print("genenrator: ", source_gen, sep=": ")
print(sys.getsizeof(source_gen))
