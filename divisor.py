from math import*
a = int(input("input a positive integer: "))
print("the divisors of ", a, "are...")
for i in range(1, a+1):
    if(a % i) == 0:
        print(i)
