b=input("enter a string\n")
rev=""
for i in range(len(b)-1,-1,-1):
	rev=rev+b[i]
if rev==b:
	print("string is palindrome")
else:
	print("string is not palindrome")

