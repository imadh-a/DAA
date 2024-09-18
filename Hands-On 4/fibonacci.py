
def fib(n):
    print(f"fib({n}) called")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

test = fib(5)
#calling the fib function with n=5 for testing purposes
print("Fibonacci of 5:", test)


