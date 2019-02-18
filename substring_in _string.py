S=input("enter a string 1\n")
T=input("enter a string 2\n")
if T in S:
	print("string 1 is in string 2")
elif S in T:
	print("string 2 is in string 1")
else:
	print("both are different string")
