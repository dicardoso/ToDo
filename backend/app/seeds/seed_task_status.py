"""This module refer task_status seed"""


def seeds(model) -> list:
    task_status = [
        model(
            id=1,
            name="Concluído",
        ),
        model(
            id=2,
            name="Em Andamento",
        ),
        model(
            id=3,
            name="Pendente",
        ),
    ]
    return task_status
