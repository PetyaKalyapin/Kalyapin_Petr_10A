import re
a = input("Введите пароль:")
c = 0
d = []
if len(a) >= 8:
    c += 2
else:
    d.append("Длина")
if re.search(r'[A-Z]', a):
    c += 2
else:
    d.append("Заглавные буквы")
if re.search(r'[a-z]', a):
    c += 2
else:
    d.append("Строчные буквы")
if re.search(r'\d', a):
    c += 2
else:
    d.append("Цифры")
if re.search(r'[!@#$%^&*\(\)]', a):
    c += 2
else:
    d.append("Специальные символы")
if c == 10:
        print("ПАРОЛЬ НАДЕЖНЫЙ: Поздравляем! Пароль соответствует стандарту безопасности.")
        print(f"Рейтинг надежности: 10/10")
else:
    print("ПАРОЛЬ НЕНАДЕЖНЫЙ: Требуются улучшения.")
    print("Проблемы:")
    for d in d:
        print(f"- {d}")
    print(f"Рейтинг надежности: {c}/10")
    
