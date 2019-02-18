b=input("enter a string\n")
result1=""
for i in range (0,len(b)):
	if ord(b[i])%2==0:
		result1=result1+"#"
	else:
		result1=result1+b[i]
print("The modified string is",result1)
	
