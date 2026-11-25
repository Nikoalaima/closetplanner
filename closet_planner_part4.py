# === Stage 4: Редактирование записей ===
# Project: ClosetPlanner
import uuid


class EditableItem:
    """Редактирование сущности 'вещь' по идентификатору."""

    ALLOWED_FIELDS = ("name", "color", "season", "material")
    SEASONS = ("spring", "summer", "autumn", "winter")

    def __init__(self, item, changes):
        self.item = item
        self.changes = changes

    def validate(self):
        unknown = set(self.changes) - set(self.ALLOWED_FIELDS)
        if unknown:
            raise ValueError(
                "Недопустимые поля для редактирования: "
                f"{', '.join(sorted(unknown))}"
            )
        for field, value in self.changes.items():
            if field == "season" and value not in self.SEASONS:
                raise ValueError(
                    f"Недопустимое значение сезона: '{value}'"
                )
            if field == "name" and not value:
                raise ValueError("Название вещи не может быть пустым")
            if field == "color" and not value:
                raise ValueError("Цвет вещи не может быть пустым")
            if field == "material" and not value:
                raise ValueError("Материал вещи не может быть пустым")

    def apply(self):
        self.validate()
        for field, value in self.changes.items():
            setattr(self.item, field, value)
        return self.item

    @staticmethod
    def create(item, changes=None):
        changes = changes or {}
        edit = EditableItem(item, changes)
        return edit.apply()

    def __repr__(self):
        return (
            f"EditableItem(item={self.item}, "
            f"changes={self.changes})"
        )


def patch_item(item, changes):
    """Применить частичное обновление к сущности 'вещь'."""
    edit = EditableItem(item, changes)
    edited = edit.apply()
    edited.id = uuid.uuid4()
    return edited
