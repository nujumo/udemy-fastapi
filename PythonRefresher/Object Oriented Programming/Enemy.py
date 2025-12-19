class Enemy:

    # type_of_enemy: str
    # health_points: int #= 10
    # attack_damage: int #= 1

    # def __init__(self): # self refers to the current class/object - empty constructor and is automatically created if no constructor is found
    #     pass

    # no argument constructor
    # def __init__(self):
    #     print('New enemy created with no starting values')

    # parameter constructor
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy # private attribute
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage.")

    # New special_attack() method that enemies can default to when they do not have a special attack
    def special_attack(self):
        print("Enemy has no special attack")