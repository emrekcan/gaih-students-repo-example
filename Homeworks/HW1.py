import random

upperNum = 100
lowerNum = 2

primeNumbers = list()

for i in range(lowerNum, upperNum+1):
    for j in range(lowerNum, i):
        if(i%j == 0):
            break
        primeNumbers.append(i)
#print(primeNumbers)
matrix = [[0 for i in range(3)]for j in range(3)]
for row in range(len(matrix)):
    for column in range(len(matrix)):
        matrix[row][column] = primeNumbers.pop(random.randint(0,len(primeNumbers)-1))
print(matrix)
