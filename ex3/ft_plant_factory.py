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
    print("===  Plant Factory Output ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Oak", 200, 365)
    p3 = Plant("Cactus", 5, 90)
    p4 = Plant("Sunflower", 80, 45)
    p5 = Plant("Fern", 15, 120)
    print("Created: ", end="")
    p1.show()
    print("Created: ", end="")
    p2.show()
    print("Created: ", end="")
    p3.show()
    print("Created: ", end="")
    p4.show()
    print("Created: ", end="")
    p5.show()


if __name__ == "__main__":
    main()
