weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))

bmi = weight / (height ** 2)
print(f"Рост:\t {height} м \nВес:\t {weight} кг \nИндекс массы тела пациента:\t {bmi:.2f}")