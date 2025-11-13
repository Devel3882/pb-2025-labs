tasks = [("Проверить почту", 3), ("Написать отчёт", 1), ("Позвонить клиенту", 2)]

tasks = sorted(tasks, key=lambda x: x[1])

print(tasks)