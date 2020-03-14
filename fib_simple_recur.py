n = int(input("Enter the term upto which the fibonacci is required"))

def recycle(n):
    """

    :return: This function returns the fibonacci sequence to the nth term
    using simple recursion but it starts getting slow for any input
    in which n>27
    """
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return recycle(n-1)+recycle(n-2)
for n in range(n):
    if n>0:
        print(n," : ",recycle(n))
    elif n==0:
        print(0, " : ",0)

recycle(n)