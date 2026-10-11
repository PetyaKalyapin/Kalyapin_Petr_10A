Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = input("Введите имя:")
... b = input("Введите фамилию:")
... c = input("Введите год рождения:")
... d = b[:3].upper() + a[-2:].upper() + c[-2:]
... print(f"Сотрудник: {a} {b}, {c} г.р.")
