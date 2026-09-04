#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.original_height = height

    def show(self) -> None:
        print(self.name.capitalize(), ": ",
              round(self.height, 1), "cm, ", self.days, " days old", sep="")

    def grow(self) -> None:
        size_increment = round(self.height / self.days, 1)
        self.height += size_increment

    def age(self) -> None:
        self.days += 1


def main() -> None:
    print("=== Garden Plant Growth ===")
    p1 = Plant("Rose", 25, 30)
    for day in range(1, 8):
        print("=== Day", day, "===")
        p1.grow()
        p1.age()
        p1.show()
    print("Growth this week: ",
          round(p1.height - p1.original_height, 1), "cm", sep="")


if __name__ == "__main__":
    main()
