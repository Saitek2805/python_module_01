#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        if height >= 0:
            self._height = height
            self._original_height = height
        else:
            self._height = 0
            self._original_height = 0
            print("Height must be equal or greater than 0")
        if days >= 0 and days <= 36500:
            self._days = days
        else:
            print("Age must be equal or greater than 0 and below 100 years")
            self._days = 0

    def show(self) -> None:
        print(self._name.capitalize(), ": ",
              round(self.get_height(), 1), "cm, ",
              self.get_age(), " days old", sep="")

    def grow(self) -> None:
        size_increment = round(self.get_height() / self.get_age(), 1)
        self.set_height(self.get_height() + size_increment)

    def age(self) -> None:
        self.set_age(self.get_age() + 1)

    def get_age(self) -> int:
        return self._days

    def get_height(self) -> float:
        return self._height

    def get_name(self) -> str:
        return self._name

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
            print("Height updated: ", self.get_height(), "cm", sep="")
        else:
            print(self.get_name(), ": Error, height can't be negative", sep="")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0 and new_age <= 36500:
            self._days = new_age
            print("Age updated: ", self.get_age(), " days", sep="")
        else:
            if new_age < 0:
                print(self.get_name(),
                      ": Error, age can't be negative", sep="")
            elif new_age > 36500:
                print(self.get_name(),
                      ": Error, age can't be greater than 100 years", sep="")
            print("Age update rejected")

    @staticmethod
    def check_age(days: int) -> None:
        print("Is", days, "days more than a year?", end="")
        if days < 365:
            print(" -> False")
        else:
            print(" -> True")

    @classmethod
    def unknown(cls) -> "Plant":
        return cls("unknown", 0.0, 0)


class Flower(Plant):
    is_bloomed = False

    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days)
        self.color = color

    def show(self) -> None:
        super().show()
        print(" Color:", self.color)
        if self.is_bloomed:
            print("", self.get_name().capitalize(), "is blooming beautifully!")
        else:
            print("", self.get_name().capitalize(), "has not bloomed yet")

    def bloom(self) -> None:
        self.is_bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(" Trunk diameter: ", self.trunk_diameter, "cm", sep="")

    def produce_shade(self) -> None:
        print("[asking the", self.get_name(), "to produce shade]")
        print("Tree ", self.get_name().capitalize(),
              " now produces a shade of ",
              self.get_height(), "cm long and ",
              self.trunk_diameter, "cm wide.", sep="")


class Vegetable(Plant):
    nutritional_value = 0.0

    def __init__(self, name: str, height: float,
                 days: int, harvest_season: str) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season

    def show(self) -> None:
        super().show()
        print(" Harvest season:", self.harvest_season.capitalize())
        print(" Nutritional value:", round(self.nutritional_value))

    def age(self) -> None:
        self._days = self.get_age() + 1
        self.nutritional_value += 0.5

    def grow(self) -> None:
        size_increment = round(self.get_height() / self.get_age(), 1)
        self._height = self.get_height() + size_increment
        self.nutritional_value += 0.5


class Seed(Flower):
    seeds = 0

    def __init__(self, name: str, height: float, days: int,
                     color: str) -> None:
        super().__init__(name, height, days, color)

    def show(self) -> None:
        super().show()
        print(" Seeds:", self.seeds)
    
    def bloom(self) -> None:
        super().bloom()
        self.seeds +=42


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print("\n=== Tree")
    p2 = Tree("oak", 200.0, 365, 5.0)
    p2.show()
    p2.produce_shade()
    print("\n=== Seed")
    p3 = Seed("sunflower", 80.0, 45, "yellow")
    p3.show()
    print("[make sunflower grow, age and bloom]")
    p3.bloom()
    p3.show()
    print("\n=== Anonymous")
    p4 = Plant.unknown()
    p4.show()


if __name__ == "__main__":
    main()
