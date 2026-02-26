pH = float(input('введите значение pH: '))
if pH > 7: 
    print('Щелочная среда')
elif pH < 7:
    print('Кислая среда')
else:
    print('Нейтральная среда')