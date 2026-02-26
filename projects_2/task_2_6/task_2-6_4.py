choice = input('Куда пойдешь? ').upper().lower().strip()
if choice == 'налево':
    print('Коня потеряешь')
elif choice == 'направо':
    print('Голову потеряешь')
elif choice == 'прямо':
    print('Жив будешь')
else:
    print('А другого выбора нет. Иди, из этих 3 выбирай.')       