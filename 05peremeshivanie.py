import random

my_list = ["a", "b", "c", "d", "e"]

for i in range(len(my_list)-1):
    j = random.randint(i, len(my_list)-1)
    my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)
