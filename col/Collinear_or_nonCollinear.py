from library import *
list=[]
for i in range(1, 5):  
    if i%2==0:
        print('Type Y: ')
    else:
        print('Type X: ')
    list.append(nabor())
for i in range(0, 4):
    if i==0:
        x1=list[i]
    if i==1:
        y1=list[i]
    if i==2:
        x2=list[i]
    if i==3:
        y2=list[i]
print(Col(x1,y1,x2,y2))
