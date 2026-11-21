# === Stage 2: Проверка полей ===
# Project: ClosetPlanner
import re


def normalize_text(value):
    text = str(value).strip()
    text = re.sub(r"\s+", " ", text)
    return text.title()


def normalize_color(value):
    color = str(value).strip().lower()
    color = re.sub(r"\s+", " ", color)
    color = color.replace("чёрн", "черн").replace("чёрн", "черн")
    return color


SEASONS = {"весна", "лето", "осень", "зима"}


def validate_season(value):
    season = str(value).strip().lower()
    if season not in SEASONS:
        raise ValueError(
            "Неверный сезон. Допустимые значения: весна, лето, осень, зима."
        )
    return season.capitalize()


def validate_material(value):
    material = str(value).strip().lower()
    if not material:
        raise ValueError("Материал не может быть пустым.")
    return material


class ClothingValidation:
    def __init__(self, name=None, color=None, season=None, material=None):
        self.name = self.validate_name(name)
        self.color = self.validate_color(color)
        self.season = self.validate_season(season)
        self.material = self.validate_material(material)

    def validate_name(self, value):
        name = normalize_text(value)
        if not name:
            raise ValueError("Название не может быть пустым.")
        if len(name) > 50:
            raise ValueError("Название слишком длинное (максимум 50 символов).")
        return name

    def validate_color(self, value):
        color = normalize_color(value)
        if not color:
            raise ValueError("Цвет не может быть пустым.")
        return color
