from library import *
list=[]
chislo1=0
chislo2=0
chislo3=0
chislo4=0
for i in range(1, 5):  
    if i%2==0:
        print('Type Y: ')
    else:
        print('Type X: ')
    list.append(nabor())
    if i==1:
      chislo1=list[0]  
    if chislo1>1000 or chislo1<-1000:
        print("ERROR")
        break
    if i==2:
        chislo2=list[1] 
    if chislo2>1000 or chislo2<-1000:
        print("ERROR")
        break 
    if i==3:
        chislo3=list[2] 
    if chislo3>1000 or chislo3<-1000:
        print("ERROR")
        break 
    if i==4:
        chislo4=list[3] 
    if chislo4>1000 or chislo4<-1000:
        print("ERROR")
        break 
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
