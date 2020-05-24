import random as r

things_names = ["Золотой меч", "Кожанный пояс", "Серебрянное кольцо", "Железный меч", "Платиновый щит",
                "Огненный шлем", "Мифриловая кольчуга", "Бронзовый нагрудник", "Кожанные сапоги",
                "Платиновый меч", "Кольцо Всевластия", "Меч света", "Точный арбалет", "Пронзающее копьё",
                "Смертельная булава", "Железные наручи", "Платиновые латы", "Жемчужное ожерелье",
                "Магический браслет", "Железный щит"]

persons_names = ["Лара Крофт", "Натан Дрэйк", "Нэнси Дрю", "Зои Кастильйо", "Эйприл Райан", "Гордон Фримен",
                 "Джилл Валентайн", "Леон Кеннеди", "Клэр Редфилд", "Крис Редфилд", "Макс Колфилд",
                 "Геральт из Ривии", "Йенифер из Венгерберга", "Цирилла Фиона Рианон", "Алан Уэйк",
                 "Эллен Рипли", "Чужой", "Капитан Шепард", "Хлои Прайс", "Гендальф Серый"]

class Thing:
    def __init__(self, name, protection, attack, health):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.health = health

class Person:
    def __init__(self, name, baseHealth, baseProtection, baseAttack):
        self.name = name
        self.baseHealth = baseHealth
        self.baseProtection = baseProtection
        self.baseAttack = baseAttack

    def setThings(self, things):
        print(f"Его предметы:")
        for thing in things:
            self.baseHealth += thing.health
            self.baseProtection += thing.protection
            self.baseAttack += thing.attack
            print(f"{thing.name}, здоровье - {thing.health}, атака - {thing.attack}, защита - {thing.protection}")

    def recieve_damage(self, damage):
        self.baseHealth -= damage
    
class Paladin(Person):
    def __init__(self, name, baseHealth, baseProtection, baseAttack):
        super().__init__(name, baseHealth, baseProtection, baseAttack)
        self.baseHealth *= 2
        self.baseProtection *= 2

class Warrior(Person):
    def __init__(self, name, baseHealth, baseProtection, baseAttack):
        super().__init__(name, baseHealth, baseProtection, baseAttack)
        self.baseAttack *= 2

things_list = []
for thing in range(1, r.randrange(2, 20)):
    thing = Thing(r.choice(things_names), round(r.uniform(0, 0.1), 2), r.randint(0, 100), r.randint(0, 100))
    things_list.append(thing)

persons_list = []
for person in range(10):
    if r.random() > 0.5:
        person = Paladin(r.choice(persons_names), r.randint(0, 100), round(r.uniform(0, 0.19), 2), r.randint(0, 50))
        persons_names.remove(person.name)
        print(f"Паладин {person.name} вступает на арену.")
    else:
        person = Warrior(r.choice(persons_names), r.randint(0, 100), round(r.uniform(0, 0.19), 2), r.randint(0, 50))
        persons_names.remove(person.name)
        print(f"Воин {person.name} вступает на арену.")
    print(f"Его характерстики: здоровье - {person.baseHealth}, аттака - {person.baseAttack}, защита - {person.baseProtection}.")
    persons_list.append(person)
    person.setThings(r.choices(things_list, k=r.randrange(1, 5)))
    print('')
    

while len(persons_list) > 1:
    dueling_pair = r.sample(persons_list, 2)
    attacker = dueling_pair[0]
    defender = dueling_pair[1]
    print(f"Атакующий {attacker.name} и защитник {defender.name} начинают бой.")
    damage = round((attacker.baseAttack - attacker.baseAttack * defender.baseProtection), 2)
    defender.recieve_damage(damage)
    print (f"{attacker.name} наносит удар по {defender.name} на {damage} урона.")
    if defender.baseHealth <= 0:
        persons_list.remove(defender)
        print(f"{defender.name} погибает.")
    print('')

winner = persons_list[0]
print(f"Победителем становится {winner.name}!")
