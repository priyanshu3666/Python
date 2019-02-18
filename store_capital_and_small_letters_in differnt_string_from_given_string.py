b=input("enter a string")
result1=""
result2=""
for i in range (0,len(b)):
	if ord(b[i])>=65 and  ord(b[i])<=90:
		result1=result1+b[i]
	else:
		result2=result2+b[i]

print("The capital letters are",result1)
print("The small letters are",result2)	
