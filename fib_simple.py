n = int(input("Enter the term upto which the fibonacci is required"))

def recycle(n):
    """

    :return: This function returns the fibonacci sequence to the nth term
    without using recursion
    """
    a = 0
    b = 1
    print("0\n1")
    for x in range(n-2):
        c=a+b
        print(c)
        a,b=b,c
recycle(n)