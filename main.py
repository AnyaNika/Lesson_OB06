import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(0, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        self.player = Hero(name="Игрок")
        self.computer = Hero(name="Компьютер")

    def start(self):
        print("Начало игры!")
        round_number = 1
        print()

        while self.player.is_alive() and self.computer.is_alive():
            print("Раунд ", round_number)
            print()
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден!")
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} побежден!")
                break

            print(f"У {self.player.name} осталось {self.player.health} здоровья.")
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
            print()
            round_number+=1

        if self.player.is_alive():
            print("Вы победили!")
        else:
            print("Вы проиграли!")

if __name__ == "__main__":
    game = Game()
    game.start()