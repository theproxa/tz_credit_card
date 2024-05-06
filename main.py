

from classes import log
from funcs import get_answer, get_log_data, get_to_search_data, print_form, update_form

act = get_answer()
if (act == '1'):
    fl = open("card.balance",'r',encoding='utf8')
    print(fl.read())
    fl.close()

elif (act == '2'):
    log_data = get_log_data()
    fl = open("card.log",'a',encoding='utf8')
    fl.write(f'{log_data.date} {log_data.categori} {log_data.summa} {log_data.description}\n')
    fl.close()
    
    fl = open("card.balance",'r',encoding='utf8')
    balance = int(fl.read())
    fl.close

    fl = open("card.balance",'w',encoding='utf8')
    fl.write(f'{balance + log_data.summa}')
    fl.close
    
    
elif (act == '3'):
    all_logs = []
    fl = open("card.log",'r',encoding='utf8')
    for line in fl.readlines():
        ln = line.split()
        log_item = log(ln[0],ln[1],ln[2],ln[3])
        all_logs.append(log_item)
    fl.close
    
    for log_item in all_logs:
        print_form(log_item.date, log_item.categori, log_item.summa, log_item.description)
        log_item = update_form(log_item)
    
    fl = open("card.log",'w',encoding='utf8')
    for log_item in all_logs:
        fl.write(f'{log_item.date} {log_item.categori} {log_item.summa} {log_item.description}\n')
    fl.close
        
elif (act == '4'):
    filter_ = get_to_search_data()
    if filter_ != 404:
        fl = open("card.log",'r',encoding='utf8')
        if(filter_[0]==1):
            for line in fl.readlines():
                li = line.split()
                if(li[0]==filter_[1]):
                    print_form(li[0],li[1],li[2],li[3])
        elif(filter_[0]==2):
            for line in fl.readlines():
                li = line.split()
                if(li[1]==filter_[1]):
                    print_form(li[0],li[1],li[2],li[3])
        elif(filter_[0]==3):
            for line in fl.readlines():
                li = line.split()
                print(li[2])
                if(int(li[2])==filter_[1]):
                    print_form(li[0],li[1],li[2],li[3])
        fl.close()

    