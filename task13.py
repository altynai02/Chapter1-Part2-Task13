# 13. For a given integer N, print all the squares of integer numbers where the
# square is less than or equal to N, in ascending order.
number = int(input("Enter a number: "))
for i in range(number):
    if i*i <= number:
        print(i*i)