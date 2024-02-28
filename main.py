#открываем фалы и удаляем лишние строки
f = open('students.csv').read().split("\n")
r = open("answer.csv", mode="w")
r.write(f[0])
f.pop(-1)
f.pop(0)

# создаем словарь для высчитывания среднего значения по классу и новый список для хранения базы данных
base = []
classRes = {}

# проходимся по файлу
for i in f:
    line = i.split(",")
    base.append(line)

    # ищем результат Владимира
    if "Хадаров Владимир" in line[1]:
        print(f"Ты получил: {line[-1]}, за проект - {line[2]}")

    # заполняем словарь с результатами по классам
    try:
        classRes[line[3]] = (int(line[-1]) + classRes[line[3]][0], classRes[line[3]][1] + 1)
    except:
        try:
            classRes[line[3]] = (int(line[-1]), 1)
        except:
            pass

# конечный словарь с средним арифметическим по классу
averageByClass = {}

# высчитываем среднее арифметческое и заполняем класс
for i in classRes.keys():
    averageByClass[i] = round((classRes[i][0] / classRes[i][1]) * 1000) / 1000

# заменяем утерянные данные на среднее по классу
for i in base:
    if i[-1] == "None":
        i[-1] = str(averageByClass[i[-2]])
    r.write(",".join(i) + "\n")
