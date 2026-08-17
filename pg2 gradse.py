#GRADE SYSTEM
#SWETHA
i=0
s=0
for i in range(1,6):
    m=int(input('enter marks of subjects'))
    s+=m
avg= s/5
if avg>90:
    print('GRADE O')
elif avg>80:
    print('GRADE A+')
elif avg>70:
    print('GRADE A')
elif avg>60:
    print('GRADE B+')
elif avg>50:
    print('GRADE B')
elif avg>45:
    print('GRADE C')
else:
    print('RA')
    
    
    
