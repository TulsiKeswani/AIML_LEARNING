# python internal heandling of Numbers assignment

m = 1000
n = 1000

print(m == n)
print(m is n)


m = 2000
# n = int(input("Enter Number : "))

print(m == n)
print(m is n)


x = 2
y = 3
z = 4

print(x,y,z)

# import sys

# sys.set_int_max_str_digits(10000000)

# print(2 ** 100000)


print(0.1 + 0.1 + 0.1 - 0.3)


from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
