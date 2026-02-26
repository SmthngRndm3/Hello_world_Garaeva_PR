volume_solution = float(input('Введите объем раствора (мл): '))
mass_salt = volume_solution * 0.009
volume_water = volume_solution
print(f'ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n', "-" * 23,f'\nОбщий объем:\t{volume_solution:.2f} мл \nМасса соли:\t{mass_salt:.2f} г \nОбъем воды:\t {volume_water:.2f} мл')
with open('garaeva_pr/projects_2/task_2_4/recipe.txt', 'w', encoding='utf-8') as recipe:
     recipe.write(f'ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n') 
     recipe.write("-" * 23)
     recipe.write(f'\nОбщий объем:\t{volume_solution:.2f} мл \nМасса соли:\t{mass_salt:.2f} г \nОбъем воды:\t {volume_water:.2f} мл')