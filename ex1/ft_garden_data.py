#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(self.name.capitalize(), ": ",
              self.height, "cm, ", self.age, " days old", sep="")


def main() -> None:
    print("=== Garden Plant Registry ===")
    p1 = Plant("rose", 5, 24)
    p1.show()
    p2 = Plant("poppy", 49, 10)
    p2.show()
    p3 = Plant("violet", 23, 16)
    p3.show()


if __name__ == "__main__":
    main()
