def Fabonacci(num):
    a , b = 0 , 1
    li = []
    while a <= num:
        li.append(a)
        a, b = b, a + b
    return li
num = int(input())
print(Fabonacci(num))
