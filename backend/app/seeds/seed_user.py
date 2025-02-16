"""This module refer user seed"""
from datetime import datetime


def seeds(model) -> list:
    users = [
        model(
            id=1,
            name="Admin",
            email="admin@mail.com",
            password="8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
            is_active=True,
        ),
    ]
    return users
