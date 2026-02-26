name_nutrient_medium = input('введите название питательной среды ')
agar_concentration = input('введите концентрацию агара(%): ')
sterilization_temperature = input('введите температуру стерилизации (°C): ')
print (f'\t{name_nutrient_medium} \n{agar_concentration} \n{sterilization_temperature}')

with open("garaeva_pr/projects_2/task_2_3/recipe.txt", "w", encoding='utf-8') as recipy:
 recipy.write(f'\t{name_nutrient_medium} \n{agar_concentration} \n{sterilization_temperature}')
 