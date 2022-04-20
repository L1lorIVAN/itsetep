class S12:
    hp = 145
    ec = 1990
    ms = 205
    gc = 7
class S13(S12):
    hp = 205
class S14(S13):
    hp = 200
    ec = 1998
    gc = 14
class S15(S14):
    ms = 235
    hp = 250
    gc = 9
S12 = S12()
S13 = S13()
S14 = S14()
S15 = S15()
print("Nissan Silvia | Коняч Сили | Обйом Двигуна | Макс.Швидкість | Расход палива")
print("S 12 ",S12.hp,S12.ec,"см3",S12.ms,"км/ч",S12.gc,"л/100 км")
print("S 13 ",S13.hp,S13.ec,"см3",S13.ms,"км/ч",S13.gc,"л/100 км")
print("S 14 ",S14.hp,S14.ec,"см3",S14.ms,"км/ч",S14.gc,"л/100 км")
print("S 15 ",S15.hp,S15.ec,"см3",S15.ms,"км/ч",S15.gc,"л/100 км")