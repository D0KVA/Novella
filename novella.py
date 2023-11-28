import time
from _ast import Break
import json
import os
import csv

items = ["Меч палладина", "Ключ", "Фляга эстуса", "Щит"]
enemy = {
    "Раб Годрика": "скрюченое существо, которое одним своим видом нагоняет ужас",
    "Рыцарь Годрика": "огромное, нет, ОЧЕНЬ ОГРОМНОЕ СУЩЕСТВО, которое одето в рыцарские доспехи"
}
enemy1 = enemy["Раб Годрика"]
enemy2 = enemy["Рыцарь Годрика"]
locations = {
    "Пещера": "узкая темная пещера с потолком, усыпанным сталактитами",
    "Центральная пещера": "место, где вы можете восстановить силы",
    "Замок Лотрика": "огромное место, где повсюду ходят рыцари"
}
loca1 = locations["Пещера"]
loca2 = locations["Центральная пещера"]
loca3 = locations["Замок Лотрика"]

def textOutput(someText):
    text = (someText)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)

def hi(player_name):
    print(f'Привет, {player_name}')

def klass(kl):
    print(f'Ваш класс: {kl}')

def textOutput1(someText):
    text = (someText)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.5)

def textOutput2(someText):
    text = (someText)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(1)

def create_save_csv():
    with open('sw_data_new.csv', 'w') as f:
        writer = csv.writer(f)
        for row in ChelCsv:
            writer.writerow(row)

def read_save_csv():
    with open('sw_data_new.csv') as f:
        print(f.read())

def create_save_json():
    with open('sw_templates.json', 'w') as f:
        f.write(json.dumps(ChelCsv))

def read_save_json():
    with open('sw_templates.json') as f:
        print(f.read())

print("Добро пожаловать в игру 'Негорящий'!")
print("1. Начать игру")
print("2. Выйти")
while True:
    try:
        text = textOutput('Напишите 1, если "да" или 2, если "нет"\n')
        answer = int(input())
        break
    except ValueError:
        print("Пожалуйста, введите корректное число.\n")
if answer == 1:
    player_name = input("Введите ваше имя: ")
    hi(player_name)
    kl = input("Введите ваш класс: ")
    klass(kl)
    text = textOutput(f'Вы очнулись в {loca1}.\n')
    text = textOutput('Вы поняли, что ваш разум затуманен.\n')
    text = textOutput(f'Встав с пятой точки, вы наткнулись ногами на {items[0]}.\n')
    text = textOutput("Вы возьмёте меч?\n")
    while True:
        try:
            text = textOutput('Напишите 1, если "да" или 2, если "нет"\n')
            a = int(input())
            break
        except ValueError:
            print("Пожалуйста, введите корректное число.\n")
    if a == 1:
        text = textOutput('Вы взяли меч, ведь вы считаете, что он вам пригодится.\n')
        text = textOutput(f'Неожиданно, впереди вас появился {enemy1}.\n')
        text = textOutput(f'Это существо вас заметило, вы решили, что можете дать отпор. \n')
        text = textOutput(f'Вы еле как смогли его одолеть. \n')
        text = textOutput(f'Но вдруг, впереди вы увидели длинный проход.\n')
        text = textOutput(f'Пройдя в него, вы увидели, что это туннель, на стенах которого было написано: "Долой нежить", "Топчи нечестивую гадость", "Смерть нечестивым гадам". \n')
        text = textOutput(f'Пройдя  этот длинный туннель, вы пришли в {loca2}.\n')
        text = textOutput(f'Вы сели у костра, чтобы восстановить силы. \n')
        text = textOutput(f'К вам подошла красивая дама, у неё на глазах была повязка. \n')
        text = textOutput(f'Она промолвила вам: "Я поняла, что ты из негорящих, я Хранительница огня Мелина." \n')
        text = textOutput(f'С этими словами, она вам протянула {items[2]}. \n')
        text = textOutput(f'Выпив из фляги, вы почувствовали себя лучше. \n')
        text = textOutput('Вы увидели, что рядом с костром валяется щит.\n')
        text = textOutput('Вы возьмёте с собой щит?\n')
        while True:
            try:
                text = textOutput('Напишите 1, если "да" или 2, если "нет"\n')
                z = int(input())
                break
            except ValueError:
                print("Пожалуйста, введите корректное число.\n")
        if z == 1:
            text = textOutput('Вы решили взять его с собой.\n')
            text = textOutput('Далее вы направились к воротам, которые находились в другом конце центральной пещеры.\n')
            text = textOutput('Но тут, на вашем пути появился странный силуэт, который решил начать с вами диалог.\n')
            text = textOutput('"Не иди туда, ты станешь смертником, если отправишься к замку Лотрика."\n')
            text = textOutput('Вы решили проигнорировать его и прошли мимо него\n')
            text = textOutput('"Глупец" - сказал он вам в след.\n')
            text = textOutput('Дойдя до огромных ворот, вы их открыли.\n')
            text = textOutput(f'И вдруг, перед вами оказалось {loca3}.\n')
            text = textOutput('Но резко, позади вас захлопнулись двери.\n')
            text = textOutput('Этот шум привлёк одного из рыцарей.\n')
            text = textOutput(f'Когда он к вам подошёл, вы поняли, что это {enemy2}.\n')
            text = textOutput('Неожиданно он совершил удар, который вы успешно успели паррировать щитом, который вы взяли у костра.\n')
            text = textOutput('После успешного паррирования вы совершили сокрушительный удар, который застанил рыцаря.\n')
            text = textOutput('Благодаря этому стану вы смогли совершить три удара, которые убили данного рыцаря.\n')
            text = textOutput('С данного рыцаря вы подобрали меч, который был в два раза больше, чем вы.\n')
            text = textOutput('Это было фатальной ошибкой, ведь, пока вы его подбирали, сзади вас появился второй рыцарь Годрика.\n')
            text = textOutput('Он нанёс молниеносный удар, который чуть вас не убил.\n')
            text = textOutput(f'Вы использовали {items[2]}.\n')
            text = textOutput('После чего решили нанести удар, но вы не учли, что он может ударить сбоку.\n')
            text = textOutput('Этот удар был настолько сильным, что он откинул вас в пропасть.\n')
            text = textOutput('В вашей голове были одни мысли: "АААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА".\n')
            text = textOutput('Вы приземлились в болото, и вдруг вы вспомнили своё имя..\n')
            text = textOutput(f'Вас зовут: {player_name}.\n')
            text = textOutput(f'Вы потеряли сознание.\n')
            text = textOutput(f"Вы очнулись возле костра, но он был не таким, как тот\n")
            text = textOutput(f"Подняв глаза, вы увидели, что перед вами находится скрюченный силуэт.\n")
            text = textOutput(f"Он сказал вам: 'akflsalsdfadsfkl asdlfkdfsa'.\n")
            text = textOutput(f"Вы не поняли, что он вам сказал, но вы заметили {items[1]}, который он протянул вам.\n")
            text = textOutput(f"Вы взяли {items[1]}.\n")
            text = textOutput(f"Пройдя дальше, вы увидели домик.\n")
            text = textOutput(f"Подойдя к домику, вы попробовали открыть дверь, но вы поняли, что она заперта.\n")
            text = textOutput(f"Вы решили использовать ключ, который идеально подошёл к данной двери.\n")
            text = textOutput(f"Пройдя в дверь вы услышали резкий хлопок.\n")
            text = textOutput(f"Это была дверь позади вас.\n")
            text = textOutput(f"Вы решили попробовать открыть дверь, но вы услышали, что после вашей попытки открылось нечто иное.\n")
            text = textOutput(f"Это был проход в противоположной части дома, из которого вышли три {enemy2}.\n")
            text = textOutput(f"Позади вас оказалось три прохода.\n")
            text = textOutput(f"Выберите ваш проход, выписав номер.\n")
            text = textOutput(f"1 - Деревянный проход.\n")
            text = textOutput(f"2 - Каменный проход.\n")
            text = textOutput(f"3 - Стена.\n")
            print(f" ------------------- \n")
            print(f"|                   |\n")
            print(f"|                   |\n")
            print(f"|                   |\n")
            print(f"|                   |\n")
            print(f"|               ++  |\n")
            print(f"|               ++  |\n")
            print(f"|                   |\n")
            print(f"|                   |\n")
            print(f"|                   |\n")
            print(f" ------------------- \n")
            while True:
                try:
                    d = int(input())
                    break
                except ValueError:
                    print("Пожалуйста, введите корректное число.")
            if d == 1:
                text = textOutput(f"Вбежав в Деревянный проход, вы услышали, как за вами захлопнулась дверь.\n")
                text = textOutput(f"Перед вами оказалась огромная гостинная.\n")
                text = textOutput(f"Вы увидели чашку чая на столике.\n")
                text = textOutput(f"Вы выпьете чай?\n")
                while True:
                    try:
                        text = textOutput('Напишите 1, если "да" или 2, если "нет"\n')
                        g = int(input())
                        break
                    except ValueError:
                        print("Пожалуйста, введите корректное число.\n")
                if g == 1:
                    text = textOutput(f"Вы решили попробовать чай.\n")
                    text = textOutput(f"Но вдруг вас резко окутала огромная боль.\n")
                    text = textOutput(
                        f"Ваше лицо начало покрываться язвами, ваш язык начинает расплываться, а глазные яблоки впадают в орбиты.\n")
                    text = textOutput(f"ВЫ УМЕРЛИ.\n")
                    ChelCsv = {
                        "Имя": player_name,
                        "Класс": kl,
                    }
                    create_save_json()
                    read_save_json()
                    create_save_csv()
                    read_save_csv()
                    Break
                elif g == 2:
                    text = textOutput(f"Вы решили не попробовать чай.\n")
                    text = textOutput(f"Вы увидели, как из чая выползли тысячи, если не миллионы жуков.\n")
                    text = textOutput(f"Они резко ринулись на вас.\n")
                    text = textOutput(f"Единственный выход, который вы увидели - это камин, за дровами которого было что-то напоминающее выход.\n")
                    text = textOutput(f"Влетев с двух ног в камин, вы выпрыгнули в какую-то пещеру\n")
                    text = textOutput(f"Вы потеряли сознание\n")
                    text = textOutput(f"Вы очнулись в {loca1}.\n")
                    text = textOutput('Вы поняли, что ваш разум затуманен.\n')
                    text = textOutput(f'Встав с пятой точки, вы наткнулись ногами на {items[0]}.\n')
                    text = textOutput(f'ВЫ ОТКРЫЛИ КОНЦОВКУ "День Сурка"\n')
                    text = textOutput1(f'Поздравляю вас!\n')
                    ChelCsv = {
                        "Имя": player_name,
                        "Класс": kl,
                    }
                    create_save_json()
                    read_save_json()
                    create_save_csv()
                    read_save_csv()
                Break
            elif d == 2:
                text = textOutput(f"Вбежав в Каменный проход, вы услышали, как за вами покатился булыжник.\n")
                text = textOutput(f"ВЫ РИНУЛИСЬ ВПЕРЁД, ТОЛЬКО ВПЕРЁД.\n")
                text = textOutput(
                    f"ЕДИНСТВЕННЫЕ МЫСЛИ, КОТОРЫЕ БЫЛИ В ВАШЕЙ ГОЛОВЕ: 'ОЙ БЛ****, Я ХОЧУ ЖИТЬ. ААААААААААААААААААААААААА'.\n")
                text = textOutput(f"Вдруг, впереди вы уцвидели справа в стене проход.\n")
                text = textOutput(f"Вы нырнули в этот проход, но там оказалась яма с шипами.\n")
                text = textOutput(f"Вы открыли концовку 'Олух'.\n")
                text = textOutput1(f"Поздравляю вас?\n")
                ChelCsv = {
                    "Имя": player_name,
                    "Класс": kl,
                }
                create_save_json()
                read_save_json()
                create_save_csv()
                read_save_csv()
                Break
            elif d == 3:
                text = textOutput(f"Вбежав в Стену, вы прошли сквозь неё.\n")
                text = textOutput(f"Вы оказались в тёмном помещении.\n")
                text = textOutput(f"Вокруг вас стоял хохот.\n")
                text = textOutput(f"Вдруг вас окружил огромная вспышка света.\n")
                text = textOutput(f"С вами начал говорить источник света:'Здравствуй. Странник. Ты. Попал. К. Нам. Выбирай. Что. Ты. Будешь. Делать.'.\n")
                text = textOutput(f"Мы. Даём. Тебе. Выбор.\n")
                text = textOutput(f"1. Уйти, но пройти этот путь сначала\n")
                text = textOutput(f"2. Остаться и умереть, познав мир\n")
                while True:
                    try:
                        h = int(input())
                        break
                    except ValueError:
                        print("Пожалуйста, введите корректное число.\n")
                if h == 1:
                    text = textOutput(f"Мы пошутили, ты не уйдёшь после того, как сумел увидеть нас\n")
                    text = textOutput(f"Вы открыли концовку 'Повёлся'.\n")
                    text = textOutput(f"Поздравляю.\n")
                    ChelCsv = {
                        "Имя": player_name,
                        "Класс": kl,
                    }
                    create_save_json()
                    read_save_json()
                    create_save_csv()
                    read_save_csv()
                Break
                if h == 2:
                    text = textOutput(f"Хорошо\n")
                    text = textOutput(f"Узнай, и прими правду.\n")
                    text = textOutput(f"Ты и есть причина беспорядков в мире.\n")
                    text = textOutput(f"Ты уничтожил род Хранителей Огня.\n")
                    text = textOutput(f"Ты создал свою империю.\n")
                    text = textOutput(f"Но тебя предал твой же брат.\n")
                    text = textOutput(f"Твой брат - Лотрик.\n")
                    text = textOutput(f"Теперь ты можешь умереть счистой совестью\n")
                    text = textOutput(f"Вы открыли концовку 'Просветление'\n")
                    text = textOutput(f"Поздравляю.\n")
                    ChelCsv = {
                        "Имя": player_name,
                        "Класс": kl,
                    }
                    create_save_json()
                    read_save_json()
                    create_save_csv()
                    read_save_csv()
                    Break
            Break
        elif z == 2:
            text = textOutput('Вы решили не брать его с собой.\n')
            text = textOutput('Далее вы направились к воротам, которые находились в другом конце центральной пещеры.\n')
            text = textOutput('Но тут, на вашем пути появился странный силуэт, который решил начать с вами диалог.\n')
            text = textOutput('"Не иди туда, ты станешь смертником, если отправишься к замку Лотрика."\n')
            text = textOutput('Вы решили проигнорировать его и прошли мимо него\n')
            text = textOutput('"Глупец" - сказал он вам в след.\n')
            text = textOutput('Дойдя до огромных ворот, вы их открыли.\n')
            text = textOutput(f'И вдруг, перед вами оказалось {loca3}.\n')
            text = textOutput('Но резко, позади вас захлопнулись двери.\n')
            text = textOutput('Этот шум привлёк одного из рыцарей.\n')
            text = textOutput(f'Когда он к вам подошёл, вы поняли, что это {enemy2}.\n')
            text = textOutput('Неожиданно он совершил удар, который разрубил вас пополам.\n')
            text = textOutput('Вас оковала сильнейшая боль, после чего вы умерли.\n')
            text = textOutput2('ВЫ УМЕРЛИ.\n')
            ChelCsv = {
                "Имя": player_name,
                "Класс": kl,
            }
            create_save_json()
            read_save_json()
            create_save_csv()
            read_save_csv()
        Break
    elif a == 2:
        text = textOutput('Вы не взяли меч, ведь вы считаете, что он вам не пригодится\n')
        text = textOutput(f'Неожиданно, впереди вас появился {enemy1}\n')
        text = textOutput(f'Это существо вас заметило, вы поняли, что надо было брать меч \n')
        text = textOutput2("ВЫ УМЕРЛИ\n")
        ChelCsv = {
            "Имя": player_name,
            "Класс": kl,
        }
        create_save_json()
        read_save_json()
        create_save_csv()
        read_save_csv()
        Break
elif answer == 2:
    print("Ладно")
    Break
