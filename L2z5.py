a = int(input("Введите стоимость покупки:"))
if a > 1000:
    print("Конечная стоимость покупки:", a-a*10/100)
else:
    print("Спасибо за покупку")