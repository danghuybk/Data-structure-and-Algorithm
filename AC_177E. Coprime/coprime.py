import math

def sieveOfErato(N):
    # Generate sieve
    sieve = [i for i in range(N + 1)]
    prime = 2
    while prime * prime <= N:
        if sieve[prime] == prime:
            for q in range(2 * prime, N + 1, prime):
                if sieve[q] == q:
                    sieve[q] = prime
        prime += 1
    return sieve

def factorize(num, sieve):
    output = set()
    while num > 1:
        output.add(sieve[num])
        num //= sieve[num]
    return output

def solve(N, nums, sieve):
    # Not coprime
    cd = nums[0]
    for i in range(1, N):
        cd = math.gcd(nums[i], cd)
    if cd != 1:
        return 2

    seen = set()
    for num in nums:
        factorizeNum = factorize(num, sieve)
        for prime in factorizeNum:
            if prime in seen:
                return 1
            else:
                seen.add(prime)

    return 0

N = int(input())
nums = list(map(int, input().split()))
MAX = max(nums)
sieve = sieveOfErato(MAX + 1)
output = solve(N, nums, sieve)

if output == 0:
    print("pairwise coprime")
elif output == 1:
    print("setwise coprime")
else:
    print("not coprime")
