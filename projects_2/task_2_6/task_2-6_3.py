donor_blood = input("Введите группу крови донора (I/0, II/А, III/В, IV/АВ): ").strip().upper()
recipient_blood = input("Введите группу крови реципиента (I/0, II/А, III/В, IV/АВ): ").strip().upper()
if donor_blood == recipient_blood or donor_blood == "I/0" :
    print('Переливание возможно')
elif recipient_blood == 'IV/АВ':
    print('Переливание возможно')
else:
    print('Переливание запрещено')