
def largest_prime_factor(n): #using def function for for two inputs of n
    i = 2
    while i * i <= n:   #condition
        if n % i:       #finding largest prime factors
            i += 1
        else:    
            n //= i     
    return n            #returning statement n to print

t = int(input().strip())    #input t

for t_itr in range(t):
    n = int(input().strip())     #input n
    print(largest_prime_factor(n))
    
