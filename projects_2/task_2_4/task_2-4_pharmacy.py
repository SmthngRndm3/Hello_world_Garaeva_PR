quality_capsules= int(input('Введите общее количество произведенных капсул: '))
capsules_in_package= int(input('Введите количество капсул в одной упаковке: '))
count1 = quality_capsules // capsules_in_package
count2 = quality_capsules % capsules_in_package
print(f'\tОтчет фасовочного цеха\n Полных упаковок:\t{count1}\n Остаток капсул:\t{count2}')
