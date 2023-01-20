t = int(input()) #taking input of T
sum=0

for t_itr in range(t): #taking T number of inputs of N
    n = int(input())
    for i in range(n):
        
        if (i%3 == 0 or i%5 == 0):
            sum = sum+i
    print(sum)
    sum=0 # reassigning value of sum, to not merge values of sum with different n inputs 
        
