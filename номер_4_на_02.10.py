email = input("Введите идентификатор:")
if email.count('@') != 1:
    print(f"ИДЕНТИФИКАТОР {email} НЕВАЛИДЕН")
else:
    name, domain = email.split('@')
    if not name or " " in name or '\t' in name or '.' not in domain or domain.endswith('.') or domain.startswith('-'):
        print(f"ИДЕНТИФИКАТОР {email} НЕВАЛИДЕН")
    else:
        valid_domain = True
        for char in domain:
            if not (char.isalnum() or char in '-.'):
                valid_domain = False
                break
        if valid_domain:
            print(f"ИДЕНТИФИКАТОР {email} ВАЛИДЕН")
        else:
            print(f"ИДЕНТИФИКАТОР {email} НЕВАЛИДЕН")
