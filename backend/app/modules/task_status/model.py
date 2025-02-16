from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from app import db


class TaskStatus(db.Model):
    __tablename__ = "task_status"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
