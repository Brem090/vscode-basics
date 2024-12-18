def print_max(num1, num2):
    if num1 > num2:
        print (num1, "максимально")
    elif num1 == num2:
        print(num1, "дорівнює", num2)
    else:
        print(num2, "максимально")
    return 

print_max(101, 101)

x = 7
b = 19
print_max(x, b)

def plus(a, b):
    c = a + b
    return c

res = plus(4, 6)
print(res)


counter = 1

while counter < 2:
    counter += 1
    print(counter)


