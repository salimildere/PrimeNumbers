def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

total_sum=0
print("Which value you want to find prime numbers in ? \nEnter the value ->")
temp=int(input())

for i in range(temp):
    if isPrime(i):
        total_sum += i

print(f"To {temp}.th value, total of prime numbers is -> {total_sum}")

