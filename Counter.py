#program counter from 3 to 117

sumNums = 0
for num in range(3,118):
    if num%15 == 0:
        add=15
    elif num%5 == 0:
        add=5
    elif num%3 == 0:
        add=3
    else:
        add=1
    sumNums = sumNums + add
    print(num)
     
print("The Total Sum: ",sumNums,sep="")
