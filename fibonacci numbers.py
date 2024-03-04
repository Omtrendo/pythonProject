def fibo(n):
    a = 0
    b = 1
    if n ==0:
        return  a
    elif n ==1:
        return b
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter a number: "))
l = [str(fibo(i)) for i in range(0, n+1)]

print(','.join(l))