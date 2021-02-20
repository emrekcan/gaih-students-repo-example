lowNum = 0
upNum = 1000

def prime_first(num):
    for prime_num in range(2, num + 1):
        if prime_num > 1:
            for i in range(2, prime_num):
                if (prime_num % i) == 0:
                    break
            else:
                print(prime_num)

def prime_second(num):
    for prime_num in range(2, num + 1):
        if prime_num > 1:
            for i in range(2, prime_num):
                if (prime_num % i) == 0:
                    break
            else:
                print(prime_num)

for i in range(lowNum, upNum):
    if i < 500:
        prime_first(i)
    if 500 < i < 100:
        prime_second(i)
