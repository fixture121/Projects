import random

passlen = int(input("Enter the length of your password:\n"))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?-_"
p = "".join(random.sample(s,passlen))
print("Here is your new password: " + p)