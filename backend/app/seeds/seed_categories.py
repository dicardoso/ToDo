"""This module refer categories seed"""


def seeds(model) -> list:
    categories = [
        model(
            id=1,
            name="Trabalho",
        ),
        model(
            id=2,
            name="Estudo",
        ),
        model(
            id=3,
            name="Lazer",
        ),
    ]
    return categories
