a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if ((a*a == b* b +c*c) or (b*b == a*a+c*c) or (c*c == a*a + b*b)):
    print('Является прямоугольным')
else:
    print("Не является прямоугольным")
