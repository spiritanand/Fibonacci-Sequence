n = int(input("Enter the term upto which the fibonacci is required"))

"""                                       
We are creating a dictionary that will     
store the values of the fibonacci sequence 
"""

fib_cache={}

def recycle(n):
    """
    

    :return: This function returns the fibonacci sequence to the nth term
    using recursion and memoization.
    Here memoization has been done explicitly..
    """
    # Incase we have cached the value already then simply return it
    if n in fib_cache:
        return fib_cache[n]
    # Computing the nth term if it has not been cached already
    if n==1 or n==2:
        val= 1
    elif n>2:
        val= recycle(n-1)+recycle(n-2)
    fib_cache[n]=val # Caching the value in the dictionary
    return val

for n in range(n):
    if n>0:
        print(n," : ",recycle(n))
    elif n==0:
        print(0, " : ",0)

recycle(n)
