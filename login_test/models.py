from sqlmodel import Field, Relationship
from typing import Optional, List
import datetime
import sqlalchemy

import reflex as rx


class User(rx.Model, table=True):
    """A table of Users."""
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(nullable=False)
    password: str = Field(nullable=False)
    email: str = Field(nullable=False, unique=True)
    created_at: datetime.datetime = Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "created_at",
            sqlalchemy.DateTime(timezone=True),
        )
    )
    updated_at: datetime.datetime = Field(
        sa_column=sqlalchemy.Column(
            "updated_at",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now()
        )
    )

    # One-to-one relationship with the Subscription table
    subscriptions: List["Subscription"] = Relationship(back_populates="user")



class Subscription(rx.Model, table=True):
    """A table for new subscriptions"""

    id: int | None = Field(default=None, primary_key=True)
    plan: str = Field(nullable=False, default="Free")
    price: float = Field(nullable=False, default=0)
    duration: int = Field(nullable=False, default=30)
    start: datetime.datetime = Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "start",
            sqlalchemy.DateTime(timezone=True)
        )
    )

    end: datetime.datetime = Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "end",
            sqlalchemy.DateTime(timezone=True)
        )
    )

    ref_number: str = Field(nullable=False)

    user: Optional[User] = Relationship(back_populates="subscriptions")
    user_id: int = Field(foreign_key="user.id")