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
def textOutput(someText):
    text = (someText)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
def smert1(someText):
    text = textOutput(someText)('Вы не взяли меч, ведь вы считаете, что он вам не пригодится\n')
    text = textOutput(someText)(f'Неожиданно, впереди вас появился {enemy1}\n')
    text = textOutput(someText)(f'Это существо вас заметило, вы поняли, что надо было брать меч \n')
    text = textOutput(someText)("ВЫ УМЕРЛИ")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
        Break
        
def nesmert1(someText):
    text = textOutput(someText)('Вы взяли меч, ведь вы считаете, что он вам пригодится.\n')
    text = textOutput(someText)(f'Неожиданно, впереди вас появился {enemy1}.\n')
    text = textOutput(someText)(f'Это существо вас заметило, вы решили, что можете дать отпор. \n')
    text = textOutput(someText)(f'Вы еле как смогли его одолеть. \n')
    text = textOutput(someText)(f'Но вдруг, впереди вы увидели длинный проход.\n')
    text = textOutput(someText)(f'Пройдя в него, вы увидели, что это туннель, на стенах которого было написано: "Долой нежить", "Топчи нечестивую гадость", "Смерть нечестивым гадам". \n')
    text = textOutput(someText)(f'Пройдя  этот длинный туннель, вы пришли в {loca2}.\n')
    text = textOutput(someText)(f'Вы сели у костра, чтобы восстановить силы. \n')
    text = textOutput(someText)(f'К вам подошла красивая дама, у неё на глазах была повязка. \n')
    text = textOutput(someText)(f'Она промолвила вам: "Я поняла, что ты из негорящих, я Хранительница огня Мелина." \n')
    text = textOutput(someText)(f'С этими словами, она вам протянула {items[2]}. \n')
    text = textOutput(someText)(f'Выпив из фляги, вы почувствовали себя лучше. \n')
    text = textOutput(someText)('Вы увидели, что рядом с костром валяется щит.\n')
       
def smert2(someText):
    text = textOutput(someText)('Вы решили не брать его с собой.\n')
    text = textOutput(someText)('Далее вы направились к воротам, которые находились в другом конце центральной пещеры.\n')
    text = textOutput(someText)('Но тут, на вашем пути появился странный силуэт, который решил начать с вами диалог.\n')
    text = textOutput(someText)('"Не иди туда, ты станешь смертником, если отправишься к замку Лотрика."\n')
    text = textOutput(someText)('Вы решили проигнорировать его и прошли мимо него\n')
    text = textOutput(someText)('"Глупец" - сказал он вам в след.\n')
    text = textOutput(someText)('Дойдя до огромных ворот, вы их открыли.\n')
    text = textOutput(someText)(f'И вдруг, перед вами оказалось {loca3}.\n')
    text = textOutput(someText)('Но резко, позади вас захлопнулись двери.\n')
    text = textOutput(someText)('Этот шум привлёк одного из рыцарей.\n')
    text = textOutput(someText)(f'Когда он к вам подошёл, вы поняли, что это {enemy2}.\n')
    text = textOutput(someText)('Неожиданно он совершил удар, который разрубил вас пополам.\n')
    text = textOutput(someText)('Вас оковала сильнейшая боль, после чего вы умерли.\n')
    text = textOutput(someText)('ВЫ УМЕРЛИ.\n')
    Break
   
def nesmert2(someText):
            text = textOutput(someText)('Вы решили взять его с собой.\n')
            text = textOutput(someText)('Далее вы направились к воротам, которые находились в другом конце центральной пещеры.\n')
            text = textOutput(someText)('Но тут, на вашем пути появился странный силуэт, который решил начать с вами диалог.\n')
            text = textOutput(someText)('"Не иди туда, ты станешь смертником, если отправишься к замку Лотрика."\n')
            text = textOutput(someText)('Вы решили проигнорировать его и прошли мимо него\n')
            text = textOutput(someText)('"Глупец" - сказал он вам в след.\n')
            text = textOutput(someText)('Дойдя до огромных ворот, вы их открыли.\n')
            text = textOutput(someText)(f'И вдруг, перед вами оказалось {loca3}.\n')
            text = textOutput(someText)('Но резко, позади вас захлопнулись двери.\n')
            text = textOutput(someText)('Этот шум привлёк одного из рыцарей.\n')
            text = textOutput(someText)(f'Когда он к вам подошёл, вы поняли, что это {enemy2}.\n')
            text = textOutput(someText)('Неожиданно он совершил удар, который вы успешно успели паррировать щитом, который вы взяли у костра.\n')
            text = textOutput(someText)('После успешного паррирования вы совершили сокрушительный удар, который застанил рыцаря.\n')
            text = textOutput(someText)('Благодаря этому стану вы смогли совершить три удара, которые убили данного рыцаря.\n')
            text = textOutput(someText)('С данного рыцаря вы подобрали меч, который был в два раза больше, чем вы.\n')
            text = textOutput(someText)('Это было фатальной ошибкой, ведь, пока вы его подбирали, сзади вас появился второй рыцарь Годрика.\n')
            text = textOutput(someText)('Он нанёс молниеносный удар, который чуть вас не убил.\n')
            text = textOutput(someText)(f'Вы использовали {items[2]}.\n')
            text = textOutput(someText)('После чего решили нанести удар, но вы не учли, что он может ударить сбоку.\n')
            text = textOutput(someText)('Этот удар был настолько сильным, что он откинул вас в пропасть.\n')
            text = textOutput(someText)('В вашей голове были одни мысли: "АААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА".\n')
            text = textOutput(someText)('Вы приземлились в болото, и вдруг вы вспомнили своё имя..\n')
            text = textOutput(someText)(f'Вас зовут: {player_name}.\n')
            text = textOutput(someText)(f'Вы потеряли сознание.\n')
            text = textOutput(someText)(f"Вы очнулись возле костра, но он был не таким, как тот\n")
            text = textOutput(someText)(f"Подняв глаза, вы увидели, что перед вами находится скрюченный силуэт.\n")
            text = textOutput(someText)(f"Он сказал вам: 'akflsalsdfadsfkl asdlfkdfsa'.\n")
            text = textOutput(someText)(f"Вы не поняли, что он вам сказал, но вы заметили {items[1]}, который он протянул вам.\n")
            text = textOutput(someText)(f"Вы взяли {items[1]}.\n")
            text = textOutput(someText)(f"Пройдя дальше, вы увидели домик.\n")
            text = textOutput(someText)(f"Подойдя к домику, вы попробовали открыть дверь, но вы поняли, что она заперта.\n")
            text = textOutput(someText)(f"Вы решили использовать ключ, который идеально подошёл к данной двери.\n")
            text = textOutput(someText)(f"Пройдя в дверь вы услышали резкий хлопок.\n")
            text = textOutput(someText)(f"Это была дверь позади вас.\n")
            text = textOutput(someText)(f"Вы решили попробовать открыть дверь, но вы услышали, что после вашей попытки открылось нечто иное.\n")
            text = textOutput(someText)(f"Это был проход в противоположной части дома, из которого вышли три {enemy2}.\n")
            text = textOutput(someText)(f"Вы хотели было убежать, но ваши попытки были тщетны.\n")
            text = textOutput(someText)(f"ВЫ УМЕРЛИ\n")
            Break

def num1():
    text = (f'Вы очнулись в {loca1}.\n')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    text = ('Вы поняли, что ваш разум затуманен.\n')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    text = (f'Встав с пятой точки, вы наткнулись ногами на {items[0]}.\n')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
  
print("Добро пожаловать в игру 'Негорящий'!")
print("1. Начать игру")
print("2. Выйти")
answer = int(input())
if answer == 1:
    player_name = input("Введите ваше имя: ")
    num1()
    text = ("Вы возьмёте меч?\n")
    
    text = ("Введите 1, если'да' или 2, если 'нет'. \n")
    a = int(input())
    if a == 1:
        nesmert1()
        text = ('Вы возьмёте с собой щит?\n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        z = int(input('Напишите 1, если "да" или 2, если "нет"'))
        for char in z:
            print(char, end='', flush=True)
            time.sleep(0.05)
        if z == 1:
            nesmert2()
        elif z == 2:
            smert2()
    elif a == 2:
        smert1()
elif answer == 2:
    print("Ладно")
    Break
