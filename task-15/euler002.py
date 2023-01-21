def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
 
t_sum=0
t = int(input())
for i in range(t):
    n=int(input())
    f=list(str(fibonacci(n)))

    for j in f:
        if (int(j))%2==0:
            t_sum += j
    print(t_sum)
    t_sum=0
    
