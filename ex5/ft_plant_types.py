#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        if height > 0:
            self._height = height
            self._original_height = height
        else:
            self._height = 0
            self._original_height = 0
            print("Height must be equal or greater than 0")
        if days > 0 and days < 36500:
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
        return self._name.capitalize()

    def set_height(self, new_height: float) -> None:
        if new_height > 0:
            self._height = new_height
            print("Height updated: ", self.get_height(), "cm", sep="")
        else:
            print(self.get_name(), ": Error, height can't be negative", sep="")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age > 0 and new_age < 36500:
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


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days)

    def show(self) -> None:
        super().show()


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    p1 = Flower("rose", 15, 10, "red")
    p1.show()

if __name__ == "__main__":
    main()
