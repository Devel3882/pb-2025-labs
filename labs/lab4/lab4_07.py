bad_translation = {
    "hello": "прив",
    "mother": "прив",
    "father": "прив",
    "sister": "прив",
    "brother": "прив",
}

text = input("Введите предложение русского языка: ")
for word in text.split():
    word = word.lower()
    if word not in bad_translation:
        print("привет", end=" ")
    else:
        print(bad_translation[word], end=" ")
