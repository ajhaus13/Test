# for loop

set1 = 0
set2 = 0

for i in range(0,101):
    set1 += i*i
    set2 += i

set3 = set2 * set2
difference = set3 - set1

print(difference)

# while loop

n = 600851475143
i = 2

while i < n:
    while n % i == 0:
        n = n / i
    i = i + 1

print(n)

#list comprehension

test1 = [i for i in range(0,1001) if i % 3 == 0 or i % 5 == 0]
print(sum(test1))