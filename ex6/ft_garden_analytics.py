#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._stats = self.PlantStats()
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

    class PlantStats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def print_stats(self) -> None:
            print("Stats:", self._grow_count, "grow,", self._age_count,
                  "age,", self._show_count, "show")

    def show(self) -> None:
        self._stats.increment_show()
        print(self._name.capitalize(), ": ",
              round(self.get_height(), 1), "cm, ",
              self.get_age(), " days old", sep="")

    def grow(self) -> None:
        self._stats.increment_grow()
        size_increment = round(self.get_height() / self.get_age(), 1)
        self.set_height(self.get_height() + size_increment)

    def age(self) -> None:
        self._stats.increment_age()
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
        else:
            print(self.get_name(), ": Error, height can't be negative", sep="")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0 and new_age <= 36500:
            self._days = new_age
        else:
            if new_age < 0:
                print(self.get_name(),
                      ": Error, age can't be negative", sep="")
            elif new_age > 36500:
                print(self.get_name(),
                      ": Error, age can't be greater than 100 years", sep="")
            print("Age update rejected")

    def print_stats(self) -> None:
        self._stats.print_stats()

    @staticmethod
    def check_age(days: int) -> None:
        print("Is", days, "days more than a year?", end="")
        if days < 365:
            print(" -> False")
        else:
            print(" -> True")

    @classmethod
    def unknown(cls) -> "Plant":
        return cls("unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days)
        self.color = color
        self.is_bloomed = False

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
        self._shade_count = 0

    def show(self) -> None:
        super().show()
        print(" Trunk diameter: ", self.trunk_diameter, "cm", sep="")

    def produce_shade(self) -> None:
        self._shade_count += 1
        print("[asking the", self.get_name(), "to produce shade]")
        print("Tree ", self.get_name().capitalize(),
              " now produces a shade of ",
              self.get_height(), "cm long and ",
              self.trunk_diameter, "cm wide.", sep="")

    def print_stats(self) -> None:
        super().print_stats()
        print("", self._shade_count, "shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days: int, harvest_season: str) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def show(self) -> None:
        super().show()
        print(" Harvest season:", self.harvest_season.capitalize())
        print(" Nutritional value:", round(self.nutritional_value))

    def age(self) -> None:
        self._stats.increment_age()
        self._days = self.get_age() + 1
        self.nutritional_value += 0.5

    def grow(self) -> None:
        self._stats.increment_grow()
        size_increment = round(self.get_height() / self.get_age(), 1)
        self._height = self.get_height() + size_increment
        self.nutritional_value += 0.5


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(" Seeds:", self.seeds)

    def bloom(self) -> None:
        super().bloom()
        self.seeds += 42


def statistics(plant: Plant) -> None:
    plant.print_stats()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)

    print("\n=== Flower")
    p1 = Flower("rose", 15.0, 10, "red")
    p1.show()
    print("[statistics for ", p1.get_name().capitalize(), "]",
          sep="")
    statistics(p1)
    print("[asking the rose to grow and bloom]")
    p1.grow()
    p1.bloom()
    p1.show()
    print("[statistics for ", p1.get_name().capitalize(), "]",
          sep="")
    statistics(p1)

    print("\n=== Tree")
    p2 = Tree("oak", 200.0, 365, 5.0)
    p2.show()
    p2.produce_shade()
    print("[statistics for ", p2.get_name().capitalize(), "]",
          sep="")
    statistics(p2)

    print("\n=== Seed")
    p3 = Seed("sunflower", 80.0, 45, "yellow")
    p3.show()
    print("[make sunflower grow, age and bloom]")
    p3.age()
    p3.grow()
    p3.bloom()
    p3.show()
    print("[statistics for ", p3.get_name().capitalize(), "]",
          sep="")
    statistics(p3)

    print("\n=== Anonymous")
    p4 = Plant.unknown()
    p4.show()
    print("[statistics for ", p4.get_name().capitalize(), "]",
          sep="")
    statistics(p4)


if __name__ == "__main__":
    main()
