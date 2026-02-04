from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, TimeStampMixin
from sqlalchemy import ARRAY, String, DateTime, ForeignKey, Integer, Enum
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import Integer, func, JSON
import enum
from typing import Optional

class GenderEnum(str, enum.Enum):

    MALE = "мужчина"
    FEMALE = "женщина"


class User(TimeStampMixin, Base):

    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False,
        comment="Email пользователя"
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
        comment="Email пользователя"
    )
    username: Mapped[str] = mapped_column(
        String(100),
        index=True,
        nullable=False,
        comment="Имя пользователя"
    )

    surname: Mapped[str | None] = mapped_column(
        String(100),
        index=True,
        default=None,
        comment="Имя пользователя"
    )

    password: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        comment="пароль пользователя"
    )

    gender: Mapped[Optional[GenderEnum]] = mapped_column(
        Enum(GenderEnum),
        nullable=True
    )

    user_image: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True
    )

