import random
N = 4
my_list = [random.randint(-N, N) for _ in range(N)]
print(my_list)
product = 1
f = open("file.txt", "r")
for x in f:
    product *= my_list[int(x)]
f.close()
print("Произведение элементов на указанных в файле розициях = ", product)
