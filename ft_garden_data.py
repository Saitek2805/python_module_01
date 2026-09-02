#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data(name: str, height: int, age: int) -> None:
    plant = Plant(name, height, age)
    print(plant.name.capitalize(), ": ",
          plant.height, "cm, ", plant.age, " days old", sep="")


def main() -> None:
    print("=== Garden Plant Registry ===")
    ft_garden_data("rose", 5, 24)
    ft_garden_data("poppy", 49, 10)
    ft_garden_data("violet", 23, 16)


if __name__ == "__main__":
    main()
