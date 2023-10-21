def compute_factorial(n):
    
    if n <= 1:
        return 1
    return n * compute_factorial(n-1)
    


num = int(input())
result = compute_factorial(num)
print("Factorial of " + str(num)+" is "+str(result))
             
