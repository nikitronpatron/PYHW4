# Вычислить число c заданной точностью d

d = int(input("Введите d: "))
num = float(input("Введите нецелое число: "))
roundD = round(num, d)

print(roundD)