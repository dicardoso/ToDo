from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from typing import List
from app import db
from app.modules.categories.model import Category
from app.modules.labels.model import Label
from app.modules.task_status.model import TaskStatus

from app.modules.user import User


class Task(db.Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), nullable=False
    )
    user: Mapped["User"] = relationship("User", back_populates="tasks")

    category_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=True
    )
    category: Mapped["Category"] = relationship("Category", back_populates="tasks")

    status_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("task_status.id"), nullable=False
    )
    status: Mapped["TaskStatus"] = relationship("TaskStatus", back_populates="tasks")

    labels_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("labels.id"), nullable=False
    )
    labels: Mapped[List["Label"]] = relationship("Label", back_populates="tasks")
