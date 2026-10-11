import re
a = input("Введите идентификатор:")
b = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.fullmatch(b, a):
    print(f"ИДЕНТИФИКАТОР {a} ВАЛИДЕН")
else:
    print(f"ИДЕНТИФИКАТОР {a} НЕВАЛИДЕН")
