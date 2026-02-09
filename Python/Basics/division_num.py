num = int(input("Enter a number ->"))

print ("\nVerify if the number will be divide by 2, 3 or 5 ... :) ...\n")

if num % 2 == 0:
    print(" Divisible by 2 (even)\n")
else:
    print("Not divisible by 2 (odd)\n")

if num % 3 == 0:
    print(" Divisible by 3\n")
else:
    print("Not divisible by 3\n")


if num % 5 == 0:
    print(" Divisible by 5\n")
else:
    print("Not divisible by 5\n")
