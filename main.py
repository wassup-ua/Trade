import deal

while True:
    print("""
    [1] Добавить сделку 
    [2] Показать сделки
    [3] Выход
    """)

    user_number = input("Выбери цифру из меню: ")
    if user_number == "1":
        deal.deal_get()
    elif user_number == "2":
        deal.conclusion_get()
    elif user_number == "3":
        break
    else:
        print("ℹ️Такой цифры нет в меню")




