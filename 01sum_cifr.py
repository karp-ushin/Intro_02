my_str = input("Введите число: ")
my_str = my_str.replace(",", "")
my_str = my_str.replace(".", "")
my_sum = 0
for c in my_str:
    my_sum += int(c)
print(my_sum)
