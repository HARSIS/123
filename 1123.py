def read_file(name: str):
    """чтение и создание массива

    Ключевые аргументы:
    name -- название файла
    """
    f = open(name).read().split('\n')
    a = []
    for i in f:
        a.append(i.split(','))
    return a


def search(a: list, surname="-1", name="-1", grade="-1", subject="-1") -> list:
    """
    поиск в массиве

    Ключевые аргументы:
    a -- массив для поиска
    surname -- фамилия искомого
    name -- имя искомого

    """
    b = []
    if surname == "-1":
        b = a.copy()
    else:
        sn = -1
        for i in range(len(a[0])):
            if "Фамилия" == a[0][i] or "фамилия" == a[0][i]:
                sn = i
        if sn != -1:
            for i in range(1, len(a)):
                if surname == a[i][sn]:
                    b.append(a[i])
    c = []
    if name == "-1":
        c = b.copy()
    else:
        n = -1
        for i in range(len(a[0])):
            if "Имя" == a[0][i] or "имя" == a[0][i]:
                n = i
        if n != -1:
            for i in range(0, len(b)):
                if name == b[i][n]:
                    c.append(b[i])
    b = []
    if grade == "-1":
        b = c.copy()
    else:
        g = -1
        for i in range(len(a[0])):
            if "Класс" == a[0][i]:
                g = i
        if g != -1:
            for i in range(0, len(c)):
                if grade == c[i][g]:
                    b.append(c[i])
    c = []
    if subject == "-1":
        c = b.copy()
    else:
        su = -1
        for i in range(len(a[0])):
            if "Любимый предмет" == a[0][i]:
                su = i
        if su != -1:
            for i in range(0, len(b)):
                if subject == b[i][su]:
                    c.append(b[i])
    return c


def get_grade(a: list, surname="-1", name="-1"):
    """
    выводит получиную оченку по предмету

    a -- массив для поисков
    surname -- фамилия искомого
    name -- имя искомого
    """
    b = search(a, surname, name)
    if len(b) != 0:
        for i in b:
            print("Ты получил:", i[4], "за предмет", i[3])


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


def mean_algebra(a: list, p: int, name="-1") -> float:
    """
    поиск средней осценки по предмету

    a -- массив поиска
    p -- класс или предмет
    name -- предмет для поиска
    """
    if p:
        b = search(a, grade=name)
    else:
        b = search(a, subject=name)
    n = 0
    for i in range(len(a[0])):
        if name == a[0][0]:
            n = i
    c = 0
    cc = 0
    for i in b:
        c += int(i[4])
        cc += 1
    return round(c / cc, 3)


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


def creat_mean_fail(a: list, name="student_new"):
    b = []
    b.append(("данные,среднее значение").split(","))
    grade = get_subject(a, "Класс")
    subject = get_subject(a, "Любимый предмет")
    for i in grade:
        b.append(("класс " + i + "," + str(mean_algebra(a, 1, i))).split(","))
    for i in subject:
        b.append((i + "," + str(mean_algebra(a, 0, i))).split(","))
    create_file(b, name)


get_grade(read_file("task 14.csv"), "Колесникова", "Ксения")
creat_mean_fail(read_file("task 14.csv"))
