protein_mass = input('Массa белков в продукте (г):')
fat_mass = input('Массa жиров в продукте (г):')
carbohydrates_mass = input('Масса углеводов в продукте (г):')

calorie_content = (float(protein_mass) * 4) + (float(fat_mass) * 9) + (float(carbohydrates_mass) * 4)
print(f"Oбщaя калорийность: {calorie_content:.2f}")