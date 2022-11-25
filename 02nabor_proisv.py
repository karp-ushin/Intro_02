N = int(input("Введите N : "))
my_list = [1]
my_str = "(1"
f = 1
s = "1"
for i in range(2, N+1):
    f *= i
    s += "*"+str(i)
    my_list.append(f)
    my_str += ", " + s
my_str += ")"
print(my_list, end=" ")
print(my_str)
