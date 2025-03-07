#get all text parts and write to variables
from typing_extensions import TextIO

with open("text.txt", 'r', encoding='utf-8') as textfile:
    content = textfile.read()
texts = content.split('\n\n')
text_start = texts[0]
text_call_oksana = texts[1]
text_call_gleb = texts[2]
text_bef_items = texts[3]
text_password_bruteforce = texts[4]
text_password_bruteforce_passed = texts[5]
text_password_bruteforce_not_passed = texts[6]
text_end_citizen = texts[7]
text_random_get_to_place = texts[8]
text_taxi_no_money = texts[9]
text_end_not_your_day = texts[10]
text_park_with_lighter = texts[11]
text_end_train_is_gone = texts[12]
text_taxi_with_money = texts[13]
text_gleb_route = texts[14]
text_end_papers_please = texts[15]
text_end_default_guy = texts[16]
text_oksana_route = texts[17]
text_end_prisoners = texts[18]
text_end_lovecraft = texts[19]
text_end_farewell = texts[20]


#config - structure that preserves all the choices
config = {
    "route": "",
    "phone": ""
}

#list with items
pockets = ["Ключи", "Наушники"]

#functions
def work_with_pockets(choice: str):
    data = choice.split(' ')
    item = "UNDEFINED"
    if len(data) != 2:
        return "Проверьте ввод"
    if data[1] == "1":
        item = "Таблетки"
    if data[1] == "2":
        item = "Деньги"
    if data[1] == "3":
        item = "Зажигалка"
    if data[1] == "4":
        item = "Повербанк"
    if data[1] == "5":
        item = "Паспорт"
    if item == "UNDEFINED":
        return "Проверьте ввод"

    if data[0] == "Взять":
        if item in pockets:
            return "Предмет уже взят!"
        pockets.append(item)
        return "GOOD"
    if data[0] == "Вернуть":
        if not(item in pockets):
            return "Предмет не в кармане!"
        pockets.remove(item)
        return "GOOD"
    return "Проверьте ввод"
def generate_rand_str(s: str):
    int_from_s = 0
    for c in s:
        int_from_s += ord(c)
    return  ((int_from_s * 9301 + 49297) % 233280) % 2

def story(storyfile):
    print(text_start)
    storyfile.write("\n" + text_start + "\n")

    while True:
        choice = input("Кому позвонить?\n1. Позвонить Оксане\n2. Позвонить Глебу\n")
        if choice == "1":
            config["route"] = "OKSANA"
            print(text_call_oksana)
            storyfile.write("\n" + text_call_oksana + "\n")
            break
        if choice == "2":
            config["route"] = "GLEB"
            print(text_call_gleb)
            storyfile.write("\n" + text_call_gleb + "\n")
            break
        print("Неверный выбор")

    print(text_bef_items)
    storyfile.write("\n" + text_bef_items + "\n")
    while True:
        print("Ваши предметы:")
        for i in pockets:
            print(i)

        work_with_pockets(input("Список предметов (напишите \"Взять\" или \"Вернуть\" и цифру предмета)\n1. Таблетки\n2. Деньги\n3. Зажигалка\n4. Повербанк\n5. Паспорт\n"))
        if len(pockets) == 4:
            print("Ваши предметы:")
            for i in pockets:
                print(i)
            break

    storyfile.write("Ваши предметы:\n")
    for i in pockets:
        storyfile.write(i+"\n")

    var_for_random = ""
    print(text_password_bruteforce)
    storyfile.write("\n" + text_password_bruteforce + "\n")
    for i in range(3):
        password = input("Введите пароль...\n")
        if password == "4882":
            config["phone"] = "UNLOCKED"
            print("Пароль верный")
            print(text_password_bruteforce_passed)
            storyfile.write("\n" + text_password_bruteforce_passed + "\n")
            break
        if i != 2:
            print("Пароль неверный, осталось попыток: ", 2 - i)
            continue
        config["phone"] = "LOCKED"
        print("Телефон заблокирован!")
        print(text_password_bruteforce_not_passed)
        storyfile.write("\n" + text_password_bruteforce_not_passed + "\n")
        var_for_random = password

    #random banned ;(
    if config["phone"] == "LOCKED":
        if generate_rand_str(var_for_random) == 0:
            print(text_end_citizen)
            storyfile.write("\n" + text_end_citizen + "\n")
            print('<' * 10 + "КОНЦОВКА \"КОРЕННОЙ ЖИТЕЛЬ\"" + '>' * 10)
            exit(0)
        print(text_random_get_to_place)
        storyfile.write("\n" + text_random_get_to_place + "\n")
    else:
        while True:
            choice = input("Что делать?\n1.Вызвать такси\n2.Срезать через парк\n3. Идти по улице\n")
            if choice == "1":
                if "Деньги" in pockets:
                    print(text_taxi_with_money)
                    storyfile.write("\n" + text_taxi_with_money + "\n")
                    break
                print(text_taxi_no_money)
                storyfile.write("\n" + text_taxi_no_money + "\n")
                continue
            if choice == "2":
                if "Зажигалка" in pockets:
                    print(text_park_with_lighter)
                    storyfile.write("\n" + text_park_with_lighter + "\n")
                    break
                print(text_end_not_your_day)
                storyfile.write("\n" + text_end_not_your_day + "\n")
                print('<' * 10 + "КОНЦОВКА \"НЕ ТВОЙ ДЕНЬ\"" + '>' * 10)
                storyfile.write('<' * 10 + "КОНЦОВКА \"НЕ ТВОЙ ДЕНЬ\"" + '>' * 10)
                exit(0)
            if choice == "3":
                if config["route"] == "OKSANA":
                    print(text_end_train_is_gone)
                    storyfile.write("\n" + text_end_train_is_gone + "\n")
                    print('<' * 10 + "КОНЦОВКА \"Конец никогда не наступит. Поезд ушёл\"" + '>' * 10)
                break
            print("Неправильный выбор")

    if config["route"] == "GLEB":
        print(text_gleb_route)
        storyfile.write(text_gleb_route)
        if "Паспорт" in pockets:
            print(text_end_default_guy)
            storyfile.write("\n" + text_end_default_guy + "\n")
            print('<' * 10 + "КОНЦОВКА \"НОРМИС\"" + '>' * 10)
            exit(0)
        print(text_end_papers_please)
        storyfile.write("\n" + text_end_papers_please + "\n")
        print('<' * 10 + "КОНЦОВКА \"Papers, please\"" + '>' * 10)

    print(text_oksana_route)
    storyfile.write("\n" + text_oksana_route + "\n")
    catacombs = {
        "left":  0,
        "right": 0
    }
    while True:
        if catacombs["left"] > 4 and catacombs["right"] < 3:
            print(text_end_prisoners)
            storyfile.write("\n" + text_end_prisoners + "\n")
            print('<' * 10 + "КОНЦОВКА \"ПЛЕННИКИ РАЗУМА\"" + '>' * 10)
            storyfile.write('<' * 10 + "КОНЦОВКА \"ПЛЕННИКИ РАЗУМА\"" + '>' * 10)
            break
        if catacombs["left"] > 2 and catacombs["right"] > 2:
            print(text_end_lovecraft)
            storyfile.write("\n" + text_end_lovecraft + "\n")
            print('<' * 10 + "КОНЦОВКА \"H. P. Lovecraft\"" + '>' * 10)
            storyfile.write('<' * 10 + "КОНЦОВКА \"H. P. Lovecraft\"" + '>' * 10)
            break
        if catacombs["left"] < 4 and catacombs["right"] > 3:
            print(text_end_farewell)
            storyfile.write("\n" + text_end_farewell + "\n")
            print('<' * 10 + "КОНЦОВКА \"Farewell\"" + '>' * 10)
            storyfile.write('<' * 10 + "КОНЦОВКА \"Farewell\"" + '>' * 10)
            break
        choice = input("Куда повернуть?\n1. Налево \n2. Направо\n")
        if choice == "1":
            catacombs["left"] += 1
            continue
        if choice == "2":
            catacombs["right"] += 1
            continue
        print("Неверный выбор")

with open("story.txt", 'w', encoding='utf-8') as sf:
    story(sf)