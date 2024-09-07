def nabor():
    number=int(input("Введите число: "))
    if number>1000 and number<-1000 and type(number)!=int:
        return print('ERROR')
    return number

def Col(x1,y1,x2,y2):
    return (x2 - x1) * (0 - y2) == (y2 - y1) * (0 - x2)
