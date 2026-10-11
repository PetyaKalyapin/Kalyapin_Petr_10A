print("Введите строку лога:")
a = input()
b = len(a) 
e = a.lower().replace(" ", "") 
d = {}
for f in e:                       
    if f in d:
        d[f] += 1
    else:
        d[f] = 1
g = max(d.values())     
h = []
for f in d:
    if d[f] == g:
        h.append(f)
print(f"Строка: {a}")
print(f"Длина строки: {b} символов")
print(f"Уникальных символов: {len(d)}")
print(f"Самый частый символ(ы): {','.join(h)} ({g} раз)")
