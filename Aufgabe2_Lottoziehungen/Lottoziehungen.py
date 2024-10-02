import random as rnd

def lotto_ziehung():
    lotto_zahlen = list(range(45))
    ziehung = list()

    for i in range(6):
        random_index = rnd.randint(0, 44 - i)
        random_number = lotto_zahlen[random_index]
        ziehung.append(random_number)
        lotto_zahlen[random_index], lotto_zahlen[44 - i] = lotto_zahlen[44 - i], lotto_zahlen[random_index]

    print("Gezogene Lottozahlen:", ziehung)
    return ziehung

lotto_ziehung()
