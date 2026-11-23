# === Stage 3: Хранилище в памяти ===
# Project: ClosetPlanner
"""Модуль ClosetPlanner: в-memory хранилище вещей.

Реализует сущность «вещь» и простой список для её хранения в памяти.
Использует только стандартную библиотеку.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Item:
    """Представляет отдельную вещь в гардеробе.

    Атрибуты:
        name (str): название вещи.
        color (str): цвет вещи.
        season (str): сезон, в который вещь подходит.
        material (str): материал, из которого изготовлена вещь.
    """

    name: str
    color: str
    season: str
    material: str


class ItemStore:
    """Хранилище вещей в памяти.

    Предоставляет функционал добавления, получения по идентификатору
    и получения списка всех вещей.
    """

    def __init__(self) -> None:
        self._items: Dict[str, Item] = {}

    def add(self, item: Item) -> Item:
        """Добавляет вещь в хранилище, используя её название как ключ.

        Если вещь с таким названием уже существует, её данные перезаписываются.

        Возвращает сам объект вещи.
        """

        self._items[item.name] = item
        return item

    def get(self, name: str) -> Optional[Item]:
        """Возвращает вещь с указанным названием или None, если её нет."""

        return self._items.get(name)

    def all(self) -> List[Item]:
        """Возвращает список всех вещей в порядке добавления."""

        return list(self._items.values())

    def __len__(self) -> int:
        return len(self._items)
