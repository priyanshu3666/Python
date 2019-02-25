1- santa clause wants to distribute 10 gifts to 10 children however the gifts can be taken out from the bag in the last in first out manner.The children comes in first come first served order.A program that takes 10 gifts then the names of 10 children then who got what gift.


#The program stated
l1=[]
l2=[]
i=0
while  i<10:
	n=input("enter gifts")
	l1.append(n)
	i=i+1
i=0
while i<10:
	m=input("enter  the name of children")
	l2.append(m)
	i=i+1
for a in range (1,11):
	b=(l1.pop())
	c=(l2.pop(0))
	print("gifts=",b,"name=",c)
