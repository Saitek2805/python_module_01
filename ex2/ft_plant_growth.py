#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(self.name.capitalize(), ": ",
              self.height, "cm, ", self.days, " days old", sep="")

    def grow(self) -> None:
        size_increment = round(self.height / self.days, 1)
        self.height += size_increment

    def age(self) -> None:
        self.days += 1


def main() -> None:
    print("=== Garden Plant Growth ===")
    p1 = Plant("Rose", 25, 30)
    p1.show()
    p1.grow()
    p1.age()
    print("=== Day 1 ===")
    p1.show()
    p1.grow()
    p1.age()
    print("=== Day 2 ===")
    p1.show()


if __name__ == "__main__":
    main()
