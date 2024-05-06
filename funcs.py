from datetime import date

from classes import log

def get_answer():
    print("""выбрать действие: 
1)посмотреть баланс
2)добавить запись
3)обновить запис
4)найти запись""")
    a = input()
    if(a!= '1' and a!= '2' and a!= '3' and a!= '4'):
        print("input error")
        return '404'
    return a

def get_log_data():
    log_item = log
    log_item.date = date.today()
    try :
        log_item.categori = input("категория: ")
        log_item.summa = int(input("сумма: "))
        log_item.description = input("описание: ")
    except:
        return "input error"
    return log_item

def get_to_search_data():
    print("""метод поиска:
1)по дате
2)по кптигории
3)по сумме""")
    try:
        sert = int(input())
        if(sert == 3):
            filt = int(input("поиск:"))
        else:
            filt = input("поиск:")
    except:
        print("input error")
        return 404
    return [sert,filt]

def print_form(a,b,c,d):
    print(f"дата: {a}")
    print(f"категория: {b}")
    print(f"сумма: {c}")
    print(f"описание: {d}\n")

def update_form(log_item :log):
    if (input("обновить запись ?\n(нажмите enter чтобы пропустить)\n")):
        log_item.date = input("дата: ")
        log_item.categori = input("категория: ")
        log_item.summa = input("сумма: ")
        log_item.description = input("описание: ")
    return log_item