from random import choice

rules = """Ножницы режут бумагу
Бумага покрывает камень
Камень давит ящерицу
Ящерица отравляет Спока
Спок ломает ножницы
Ножницы обезглавливают ящерицу
Ящерица съедает бумагу
Бумага подставляет Спока
Спок испаряет камень
Камень разбивает ножницы"""

allowed = ["Камень", "Ножницы", "Бумага", "Ящерица", "Спок"]
transformed_allowed = ["камень", "ножницы", "бумагу", "ящерицу", "Спока"]
win_rules = [rule.split() for rule in rules.split("\n")]

players_word = input("Введите свой ход в игре Камень-Ножницы-Бумага-Ящерица-Спок: ")
transformed_player_word = transformed_allowed[allowed.index(players_word)]

computer_word = choice(allowed)
transformed_computer_word = transformed_allowed[allowed.index(computer_word)]

print("Компьютер выбрал: " + computer_word)
for win_condition in win_rules:
    if players_word == win_condition[0] and transformed_computer_word == win_condition[-1]:
        print("Игрок побеждает! " + " ".join(win_condition))
        break
    if computer_word == win_condition[0] and transformed_player_word == win_condition[-1]:
        print("Компьютер побеждает! " + " ".join(win_condition))
        break
else:
    print("Никто не победил")
