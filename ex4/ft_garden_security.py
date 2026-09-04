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
        print(self._name.capitalize(), ": ", round(self.get_height(), 1), "cm, ",
              self.get_age(), " days old", sep="")

    def grow(self) -> None:
        size_increment = round(self.get_height() / self.get_age(), 1)
        self.set_height(self.get_height() + 1)

    def age(self) -> None:
        self.set_age(self.get_age() + 1)
    
    def get_age(self):
        return self._days

    def get_height(self):
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height > 0:
            self._height = new_height
        else:
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age > 0 and new_age < 36500:
            self._days = new_age
        else:
            print("Age update rejected")


def main() -> None:
    print("===  Plant Factory Output ===")
    p1 = Plant("Rose", -29, -1)
    p1.age()
    p1.grow()
    p1.show()


if __name__ == "__main__":
    main()
