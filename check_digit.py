one = input("Please enter your first number: \n")
two = input("Please enter your second number: \n")
three = input("Please enter your third number: \n")
four = input("Please enter your fourth number: \n")
five = input("Please enter your fifth number: \n")
six = input("Please enter your sixth number: \n")
seven = input("Please enter your seventh number: \n")
eight = input("Please enter your eighth number: \n")
nine = input("Please enter your ninth number: \n")
ten = input("Please enter your tenth number: \n")

total = (one * 2) + (two * 3) + (three * 4) + (four * 5) + (five * 6) + (six * 7) + (eight * 9) + (nine * 10) + (ten * 11)

remainder = total % 11

answer = 11 - remainder
if answer == 11:
    print "0"
elif answer == 10:
    print "X"

else:
    print answer

