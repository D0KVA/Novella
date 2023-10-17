import time
from _ast import Break

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
print("Добро пожаловать в игру 'Негорящий'!")
print("1. Начать игру")
print("2. Выйти")
answer = int(input())
if answer == 1:
    player_name = input("Введите ваше имя: ")
    text = (f'Вы очнулись в {loca1}.\n')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    text = ('Вы поняли, что ваш разум затуманен.\n')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    text = (f'Встав с пятой точки, вы наткнулись ногами на {items[0]}.\n')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    text = ("Вы возьмёте меч?\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    text = ("Введите 'да' или 'нет'. \n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    a = input()
    if a == "да" or "Да" or "ДА" or "дА":
        text = ('Вы взяли меч, ведь вы считаете, что он вам пригодится.\n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = (f'Неожиданно, впереди вас появился {enemy1}.\n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = (f'Это существо вас заметило, вы решили, что можете дать отпор. \n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = (f'Вы еле как смогли его одолеть. \n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = (f'Но вдруг, впереди вы увидели длинный проход.\n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = (f'Пройдя в него, вы увидели, что это туннель, на стенах которого было написано: "Долой нежить", "Топчи нечестивую гадость", "Смерть нечестивым гадам". \n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = (f'Пройдя  этот длинный туннель, вы пришли в {loca2}.\n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = (f'Вы сели у костра, чтобы восстановить силы. \n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = (f'К вам подошла красивая дама, у неё на глазах была повязка. \n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = (f'Она промолвила вам: "Я поняла, что ты из негорящих, я Хранительница огня Мелина." \n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = (f'С этими словами, она вам протянула {items[2]}. \n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = (f'Выпив из фляги, вы почувствовали себя лучше. \n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = ('Вы увидели, что рядом с костром валяется щит.\n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        text = ('Вы возьмёте с собой щит?\n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        z = input('Напишите "да" или "нет"')
        if z == "да" or "Да" or "ДА" or "дА":
            text = ('Вы решили взять его с собой.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Далее вы направились к воротам, которые находились в другом конце центральной пещеры.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Но тут, на вашем пути появился странный силуэт, который решил начать с вами диалог.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('"Не иди туда, ты станешь смертником, если отправишься к замку Лотрика."\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Вы решили проигнорировать его и прошли мимо него\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('"Глупец" - сказал он вам в след.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Дойдя до огромных ворот, вы их открыли.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = (f'И вдруг, перед вами оказалось {loca3}.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Но резко, позади вас захлопнулись двери.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Этот шум привлёк одного из рыцарей.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = (f'Когда он к вам подошёл, вы поняли, что это {enemy2}.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Неожиданно он совершил удар, который вы успешно успели паррировать щитом, который вы взяли у костра.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('После успешного паррирования вы совершили сокрушительный удар, который застанил рыцаря.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Благодаря этому стану вы смогли совершить три удара, которые убили данного рыцаря.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('С данного рыцаря вы подобрали меч, который был в два раза больше, чем вы.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Это было фатальной ошибкой, ведь, пока вы его подбирали, сзади вас появился второй рыцарь Годрика.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Он нанёс молниеносный удар, который чуть вас не убил.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = (f'Вы использовали {items[2]}.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('После чего решили нанести удар, но вы не учли, что он может ударить сбоку.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Этот удар был настолько сильным, что он откинул вас в пропасть.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('В вашей голове были одни мысли: "АААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА".\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.025)
            text = ('Вы приземлились в болото, и вдруг вы вспомнили своё имя..\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = (f'Вас зовут: {player_name}.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = (f'Вы потеряли сознание.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = (f'ОТКРЫТАЯ КОНЦОВКА.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = (f'продолжение в следующей практической.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
        elif z == "нет" or "НЕТ" or "Нет" or "НеТ" or "нЕТ" or "НЕт":
            text = ('Вы решили не брать его с собой.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Далее вы направились к воротам, которые находились в другом конце центральной пещеры.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Но тут, на вашем пути появился странный силуэт, который решил начать с вами диалог.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('"Не иди туда, ты станешь смертником, если отправишься к замку Лотрика."\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Вы решили проигнорировать его и прошли мимо него\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('"Глупец" - сказал он вам в след.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Дойдя до огромных ворот, вы их открыли.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = (f'И вдруг, перед вами оказалось {loca3}.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Но резко, позади вас захлопнулись двери.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Этот шум привлёк одного из рыцарей.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = (f'Когда он к вам подошёл, вы поняли, что это {enemy2}.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Неожиданно он совершил удар, который разрубил вас пополам.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('Вас оковала сильнейшая боль, после чего вы умерли.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            text = ('ВЫ УМЕРЛИ.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
            Break
    elif a == "нет":
        text = ('Вы не взяли меч, ведь вы считаете, что он вам не пригодится\n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text = (f'Неожиданно, впереди вас появился {enemy1}\n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text = (f'Это существо вас заметило, вы поняли, что надо было брать меч \n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text = ("ВЫ УМЕРЛИ")
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        Break
elif answer == 2:
    print("Ладно")
    Break