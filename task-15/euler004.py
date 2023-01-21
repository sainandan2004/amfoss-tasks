def largest_palindrome(n): #using def function
    palindrome = 0
    for i in range(100, 1000):    #checking for all 3digit numbers
        for j in range(100, 1000):
            product = i * j       #multiplying all possible 3digit numbers
            if product < n and str(product) == str(product)[::-1] and product > palindrome: #checking if product is valid and checking for palindrom
                palindrome = product
    return palindrome

t = int(input())   #taking input t
for i in range(t):
    n = int(input()) #taking input n
    print(largest_palindrome(n))   #printing palindrome
    
