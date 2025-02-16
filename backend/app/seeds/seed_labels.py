"""This module refer labels seed"""


def seeds(model) -> list:
    labels = [
        model(
            id=1,
            name="Alta Prioridade",
        ),
        model(
            id=2,
            name="Baixa Prioridade",
        ),
        model(
            id=3,
            name="Normal",
        ),
        model(
            id=4,
            name="Urgente",
        ),
    ]
    return labels
