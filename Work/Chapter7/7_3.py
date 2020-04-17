"""Ask the user for a number, and then report whether the number is a multiple of 10 or not."""

num = input("Please enter a number, and I'll tell you whether it's a multiple of 10 or not: ")
if int(num) % 10 == 0 :
    msg = "This number is a multiple of 10!"
else:
    msg = "This is not a multiple of 10!"
print(msg)
