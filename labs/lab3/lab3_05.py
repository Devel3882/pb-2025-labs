password = input("Введите НАДЁЖНЫЙ пароль: ")

latin = "qwertyuiopasdfghjklzxcvbnnm"
digits = "1234567890"

hasCapitalChar = False
hasSmallChar = False
has8chars = False
hasDigit = False
hasSpecialSymbol = False

for c in password:
    if c in latin.upper():
        hasCapitalChar = True
    elif c in latin.lower():
        hasSmallChar = True
    elif c in digits:
        hasDigit = True
    else:
        hasSpecialSymbol = True
if len(password) >= 8:
    has8chars = True

if hasCapitalChar and hasSmallChar and has8chars and hasDigit and hasSpecialSymbol:
    print("Пароль оказывается надёжен (но это не точно")
else:
    print("Пароль не удолетворяет минимальным требованиям:")
    if not hasCapitalChar:
        print("- Нету загланвых букв латинского алфавита")
    if not hasSmallChar:
        print("- Нету строчных букв латинского алфавита")
    if not has8chars:
        print("- Пароль меньше 8 символов")
    if not hasDigit:
        print("- Нету цифр")
    if not hasSpecialSymbol:
        print("- Нету спец символов")