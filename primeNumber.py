from primeCheck import isPrime
from testing.customLib import addition

primeList = []
for i in range(10, 20):
    if isPrime(i):
        primeList.append(i)
print(primeList)
addition()
