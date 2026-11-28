# === Stage 5: Удаление и восстановление ===
# Project: ClosetPlanner
from __future__ import annotations


class Trash:
    """Хранилище мягко удалённых вещей с возможностью восстановления."""

    def __init__(self) -> None:
        self._deleted: dict[str, dict] = {}

    def soft_delete(self, item: dict) -> None:
        self._deleted[id(item)] = dict(item)

    def restore(self, item: dict) -> bool:
        key = id(item)
        if key not in self._deleted:
            return False
        self._deleted.pop(key)
        return True

    def is_deleted(self, item: dict) -> bool:
        return id(item) in self._deleted

    def count(self) -> int:
        return len(self._deleted)

    def clear(self) -> None:
        self._deleted.clear()


def find_in_trash(trash: Trash, name: str) -> dict | None:
    for entry in trash._deleted.values():
        if entry.get("name") == name:
            return entry
    return None


def remove_item(closet: dict, trash: Trash, name: str) -> bool:
    for i, item in enumerate(closet):
        if item.get("name") == name:
            if trash.is_deleted(item):
                trash.restore(item)
            else:
                trash.soft_delete(item)
            closet.pop(i)
            return True
    return False


def restore_item(closet: dict, trash: Trash, name: str) -> bool:
    entry = find_in_trash(trash, name)
    if entry is None:
        return False
    closet.append(entry)
    return True
