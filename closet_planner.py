# === Stage 1: Каркас модуля ===
# Project: ClosetPlanner
from dataclasses import dataclass, field
from enum import Enum


class Season(Enum):
    SPRING = "весна"
    SUMMER = "лето"
    AUTUMN = "осень"
    WINTER = "зима"


@dataclass
class Item:
    name: str
    color: str
    season: Season
    material: str


def demo_items() -> list["Item"]:
    return [
        Item("Пальто", "бежевый", Season.AUTUMN, "шерсть"),
        Item("Худи", "серый", Season.SPRING, "хлопок"),
        Item("Платье", "синий", Season.SUMMER, "шелк"),
        Item("Шерстяной свитер", "бордовый", Season.WINTER, "шерсть"),
        Item("Льняные брюки", "зеленый", Season.SUMMER, "лен"),
    ]


def main() -> None:
    items = demo_items()
    print("Демо-гардероб ClosetPlanner")
    print(f"Добавлено вещей: {len(items)}")
    for item in items:
        print(f"  [{item.season.value}] {item.name} — {item.color}, {item.material}")
    print("Теперь можно создавать образы и планировать стирку.")


if __name__ == "__main__":
    main()
