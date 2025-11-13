class Conditioner:
    isOn: bool

    def turnOn(self):
        self.isOn = True
    def turnOff(self):
        self.isOn = False

    def __init__(self):
        self.isOn = True
    def __str__(self):
        if self.isOn:
            return f"Кондиционер | состояние - ВКЛЮЧЕН"
        return f"Кондиционер | состояние - ВЫКЛЮЧЕН"


conditioner = Conditioner()


t = int(input("Введите комнату температуры: "))

if t >= 20:
    conditioner.turnOn()
else:
    conditioner.turnOff()

print(conditioner)