#program started
'''taking input from user
n1,n2,n3 are the number'''
n1 = int(input("Enter 1st number"))
n2 = int(input("Enter 2nd number"))
n3 = int(input("Enter 3rd number"))
#method to compare number to be greater
if n1 > n2 and n1 > n3:
    print("The greatest number among them is ",n1)
elif n2 > n3:
    print("The greatest number among them is ",n2)
else :
    print("The greatest number among them is ",n3)
