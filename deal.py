
trade_log = []


def deal_get():
    date_deal = input("Дата сделки: ")
    name_coin = input("Напиши название актива: ").upper()
    shoulder_deal = float(input("Плечё сделки: "))
    percent_deal = float(input("Напиши процент сделки без '%': "))
    trend_deal = input("Выбери направление сделки:\n(1)🟢LONG\n(2)🔴SHORT\n ")
    while True:
        if trend_deal == "1":
            user_trend = "🟢LONG"
            break
        elif trend_deal == "2":
            user_trend = "🔴SHORT"
            break
        else:
            print("ℹ️Такой цифры нет в меню")

    profit_and_loss = input("Какая была сделка:\n(1)📈Прибыльная\n(2)📉Убыточная\n")
    while True:
        if profit_and_loss == "1":
            money_deal = float(input("Напишите ваш профит: "))
            deal_symbol = "+"
            break
        elif profit_and_loss == "2":
            money_deal = float(input("Напишите ваш убыток: "))
            deal_symbol = "-"
            break
        else:
            print("ℹ️Такой цифры нет в меню")

    comments_user = input("Ваш комментарий по сделке: ").capitalize()


    trade = {
        "date": date_deal,
        "coin": name_coin,
        "shoulder": shoulder_deal,
        "percent": percent_deal,
        "trend": user_trend,
        "symbol": deal_symbol,
        "money": money_deal,
        "comments": comments_user,
    }
    trade_log.append(trade)

    print("Сделка успешно добавлена ✅ :")
    print(f"""
            {date_deal}
            {name_coin}/USDT {shoulder_deal}X {user_trend}
            {percent_deal} %
            {deal_symbol} {money_deal} USDT
            Ваш комментарий: {comments_user}
            """)



def conclusion_get():
    print("Ваши сделки:")
    for i, trade in enumerate(trade_log, start=1):
        print(f"""
        {i}. {trade['date']}
           {trade['coin']}/USDT {trade['shoulder']}X {trade['trend']}
           {trade['percent']}%
           {trade['symbol']}{trade['money']} USDT
           Комментарий: {trade['comments']}
                """)
