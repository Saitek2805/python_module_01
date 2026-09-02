#!/usr/bin/env python3

def ft_garden_intro(name: str, height: int, age: int) -> None:
    print("Plant:", name.capitalize())
    print("Height: ", height, "cm", sep="")
    print("Age:", age, "days")


def main() -> None:
    print("=== Welcome to My Garden ===")
    ft_garden_intro("Poppy", 3, 7)
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
