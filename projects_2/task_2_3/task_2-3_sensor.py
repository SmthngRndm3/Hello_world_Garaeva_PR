operator_name = input('Введите имя оператора:')
pressure_value = input('Введите текущее значение давления (Па):')
print (f'Введите имя оператора:\t {operator_name} \nВведите текущее значение давления (Па):\t {pressure_value}')

with open('garaeva_pr/projects_2/task_2_3/sensor_log.txt', 'w', encoding='utf-8') as log:
    log.write(f'Введите имя оператора:\t {operator_name} \nВведите текущее значение давления (Па):\t {pressure_value}')
    print ('Данные успешно сохранены в sensor_log.txt')