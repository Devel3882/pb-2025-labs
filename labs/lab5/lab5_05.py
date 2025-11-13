def palindrom(text):
    text = text.replace(" ", "").lower()

    if text == text[::-1]:
        return "Да"
    else:
        return "Нет"

print(palindrom("А роза упала на лапу Азора"))