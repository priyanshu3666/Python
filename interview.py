l=[]
while (1):
	print(" press 1 for add a person in a list\n press 2 for go in the room\n press 3 to exit ")
	n=int(input(""))
	if n==1:
		name=input("")
		l.append(name)
	elif n==2:
		if len(l)>0:
		
			print(l.pop(0),", now its your turn ")
		else:
			print("Ther is no person in the list for interview")
	elif n==3:
		break
	else:
		print("wrong input")


