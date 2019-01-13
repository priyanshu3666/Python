#Program started
'''The input should be enter by user
x,y,z are the number enter by user'''
x = int(input("Enter 1st number"))
y = int(input("Enter 2nd number"))
z = int(input("Enter 3rd number"))
if (x < y) and (x < z) :    #logic for checking the smallest number
    print("The smallest number among ",x,",",y,",",z," is ",x)
elif y < z :
    print("The smallest number among ",x,",",y,",",z," is ",y)
else :
    print("The smallest number among ",x,",",y,",",z," is ",z)   #logic ends
#Program Ends
