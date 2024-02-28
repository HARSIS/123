def read_fail(name):
    """чтение и создание массива

    Ключевые аргументы:
    name -- название файла
    """
    f = open(name).read().split('\n')
    a = []
    for i in f:
        a.append(i.split(','))
    return a

def search(surname, name, a):
    """
    поиск в массиве

    Ключевые аргументы:
    a -- массив для поиска
    surname -- фамилия искомого
    name -- имя искомого
    """

    b = []
    for i in 
print(read_fail("task 14.csv"))
