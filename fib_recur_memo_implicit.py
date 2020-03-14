from functools import lru_cache
n = int(input("Enter the term upto which the fibonacci is required"))
@lru_cache(maxsize=n) # By default it stores the last 128 LRU
                      # LRU(Least Recently Used Values)
def recycle(n):
    """
    This is the final and best version(in my power and knowledge) of the
    fibonacci sequence

    :return: This function returns the fibonacci sequence to the nth term
    using recursion and memoization.
    Here memoization has been done implicitly.
    """
    if type(n)!=int:
        raise TypeError("The number entered must be a positive integer "
                        "greater than equal to one")
    if n<1:
        raise ValueError("The number entered must be greater than +1")
    if n==1 or n==2:
        return 1
    elif n>2:
        return recycle(n-1)+recycle(n-2)
for n in range(n):
    if n>0:
        print(n," : ",recycle(n))
    elif n==0:
        print(0, " : ",0)

recycle(n)