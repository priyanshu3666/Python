'''A lottery ticket comntains 6 digit .the company has announce that a bumper  prize of rupees 1 lakh will be given to a candidate
whose ticket number is such that the sum of first three digit is equal  to last 3 digit.))))))))
find no. of candidates '''

#PROGRAM STARTED
c=0
for i in range(0,1000000):
    s=str(i)
    if len(s)!=6:
        s="0"*(6-len(s))
    sum1 = int(s[0])+int(s[1])+int(s[2])
    sum2 = int(s[3])+int(s[4])+int(s[5])
    if sum1==sum2:
        c=c+1
print("total count",c)        
