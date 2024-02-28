import random


def read_file(name: str):
    """чтение и создание массива

    Ключевые аргументы:
    name -- название файла
    """
    f = open(name, encoding="utf8").read().split('\n')
    a = []
    for i in f:
        a.append(i.split(','))
    return a


def search(a: list, id="-1", name="-1", titleProject_id="-1", grade="-1", score="-1") -> list:
    """
    поиск в массиве

    Ключевые аргументы:
    a -- массив для поиска
    id -- номер участника
    name -- ФИО
    titleProject_id -- номер проэкта
    grade -- ласс участника
    score -- оценка участника
    """
    b = []
    if id == "-1":
        b = a.copy()[1:]
    else:
        for i in range(1, len(a)):
            if id == a[i][0]:
                b.append(a[i])
    c = []
    if name == "-1":
        c = b.copy()
    else:
        for i in range(0, len(b)):
            if name in b[i][1]:
                c.append(b[i])
    b = []
    if titleProject_id == "-1":
        b = c.copy()
    else:
        for i in range(0, len(c)):
            if titleProject_id == c[i][2]:
                b.append(c[i])
    c = []
    if grade == "-1":
        c = b.copy()
    else:
        for i in range(0, len(b)):
            if grade in b[i][3]:
                c.append(b[i])
    b = []
    if score == "-1":
        b = c.copy()
    else:
        for i in range(0, len(c)):
            if score == c[i][4]:
                b.append(c[i])
    return b


def get_grade(a: list, name="-1"):
    """
    выводит получиную оченку по предмету

    a -- массив для поисков
    surname -- фамилия искомого
    name -- имя искомого
    """
    b = search(a, name=name)
    if len(b) != 0:
        for i in b:
            print("Ты получил: ", i[4], ", за проект - ", i[2], sep="")


def create_file(a: list, name: str):
    """
    запись файла

    a -- массив для записи
    name -- имяфайла
    """
    name += ".csv"
    b = []
    for i in a:
        b.append(",".join(i))
    c = "\n".join(b)
    open(name, 'w').write(c)


def get_subject(a: list, name: str) -> list:
    """
    вернуть массив всех найденых элеменетов

    a -- массив для поска
    """
    b = set()
    n = 0
    for i in range(len(a[0])):
        if name == a[0][i]:
            n = i
    for i in range(1, len(a)):
        if (1 - (a[i][n] in b)):
            b.update({a[i][n]})
    return list(b)


def mean_algebra(a: list, name: str) -> float:
    """
    поиск средней осценки по предмету

    a -- массив поиска
    name -- класс
    """
    b = search(a, grade=name)
    c = 0
    cc = 0
    for i in b:
        if i[4] != "None":
            c += int(i[4])
        cc += 1
    return round(c / cc, 3)


def creat_mean_fail(a: list, name="student_new"):
    """
    создание нового csv файла со статиститкой по классам

    a -- массив с участниками
    name -- название создаваймого файла
    """
    b = []
    b.append(("данные,среднее значение").split(","))
    grade = get_subject(read_file("students.csv"), name="class")
    for i in grade:
        b.append(("класс " + i + "," + str(mean_algebra(a, i))).split(","))
    create_file(b, name)


def vin(a: list, grade: str):
    """
    топ три учатника из класса

    a -- массив с данными
    grade -- класс участников
    """
    b = search(a, grade=grade)
    for i in range(1, len(b)):
        x = b[i]
        j = i
        while j > 0 and int(b[j - 1][4]) > int(x[4]):
            b[j] = b[j - 1]
            j -= 1
        b[j] = x
    print(grade, "класс:")
    print("1 место:", b[-1][1])
    print("2 место:", b[-2][1])
    print("3 место:", b[-3][1])


def search_stop(a: list):
    """
    производит поиск по номеру проэкта пока не в ведено слово "СТОП"
    a -- масив поиска
    """
    while (1):
        b = str(input())
        if b == "СТОП":
            break
        c = search(a, titleProject_id=b)
        if len(c) == 0:
            print("Ничего не найдено.")
        else:
            for i in c:
                print("Проект № ", i[2], " делал: ", i[1], " он(а) получил(а) оценку - ", i[4], ".", sep="")


def generation_name(a: list) -> list:
    """
    генерция логина пользователя

    a -- изначальный список пользовотелей
    """
    d = a.copy()
    d[0].append("login")
    for i in range(1, len(d)):
        b = d[i][1].split(" ")
        d[i].append(b[0] + "_" + b[1][0] + b[2][0])
    return d


def generation_password(a: list) -> list:
    """
    генерция пороля пользователя

    a -- изначальный список пользовотелей
    """
    d = a.copy()
    d[0].append("password")
    for i in range(1, len(d)):
        ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
        numeric = "0123456789"
        pas = [random.choice(ascii_uppercase), random.choice(ascii_lowercase), random.choice(numeric),
               random.choice(ascii_uppercase + ascii_lowercase + numeric),
               random.choice(ascii_uppercase + ascii_lowercase + numeric),
               random.choice(ascii_uppercase + ascii_lowercase + numeric),
               random.choice(ascii_uppercase + ascii_lowercase + numeric),
               random.choice(ascii_uppercase + ascii_lowercase + numeric)]
        random.shuffle(pas)
        d[i].append("".join(pas))
    return d


def generation_fail_password(a: list, name="students_password"):
    """
    создания файла с поролем и логином

    a -- массив
    name -- имя файла
    """
    d = generation_password(generation_name(a))
    create_file(d, name)


def hash(s: str, p=66, m=10 ** 9 + 9) -> str:
    """
    создаёт хэш страки

    s -- страка
    p -- мощьность алфавита
    m -- модуль хэша
    """
    cout = 0
    p_pow = 1
    for i in range(len(s)):
        cout = (cout + ord(s[i]) * p) % m
        p_pow = (p_pow * p) % m
    return str(cout)


def creat_hash_fail(a: list, name="students_with_hash"):
    """
    создания файла с хэшем всемсо id

    a -- изночальный массив
    name -- имя файла
    """
    d = a.copy()
    for i in range(1, len(d)):
        d[i][0] = hash(d[i][1])
    create_file(d, name)


p = 0
while (1):
    if p:
        print("Некорректный ввод повторите попытку")
    a = str(input("Введите номер задания(нажмите Enter)"))
    if a == "1":
        get_grade(read_file("students.csv"), name="Хадаров Владимир")  # 1
        creat_mean_fail(read_file("students.csv"))  # 1
        print("Файл создан")
    elif a == "2":
        vin(read_file("students.csv"), "10")  # 2
    elif a == "3":
        search_stop(read_file("students.csv"))  # 3
    elif a == "4":
        generation_fail_password(read_file("students.csv"))  # 4
        print("Файл создан")
    elif a == "5":
        creat_hash_fail(read_file("students.csv"))  # 5
        print("Файл создан")
    else:
        p = 1
