new_reagent_name = input()
quantity = input()
print (f"Реактив {new_reagent_name} поступил на склад в количестве {quantity} шт.")
with open("garaeva_pr/projects_2/task_2_2/inventory.txt", "w", encoding="utf-8") as file: 
    file.write (f'Реактив {new_reagent_name} поступил на склад в количестве {quantity} шт.\n')

