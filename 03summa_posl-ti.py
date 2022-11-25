N = 4
my_list = [(1 + 1/i)**i for i in range(1, N+1)]
print(round(sum(my_list), 2))
