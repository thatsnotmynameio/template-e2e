"""The last n items of a list."""


def last_items(items: list[int], n: int) -> list[int]:
    """Return the last n items, oldest first."""
    return items[len(items) - n - 1:]
