
#Fibonacci sequence
def printFib(n=2):
    uCurrent=1; uNext=2
    for i in range(0,n):
        print(uCurrent)
        uPrev = uCurrent
        uCurrent = uNext
        uNext = uPrev + uCurrent

#This should return 1, 2, 3, 5, 8

printFib(15)


