import reflex as rx
from sqlmodel import select

from .base import State, User


class AuthState(State):
    """The authentication state for sign up and login page."""

    username: str
    password: str
    email: str

    def signup(self):
        """Sign up a user."""
        with rx.session() as session:
            if session.exec(select(User).where(User.email == self.email)).first():
                return rx.window_alert("User already exists.")
            self.user = User(email=self.email, password=self.password)
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            return rx.redirect("/dashboard")

    def login(self):
        """Log in a user."""
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.email == self.email)
            ).first()
            if user and user.password == self.password:
                self.user = user
                return rx.redirect("/dashboard")
            else:
                return rx.window_alert("Invalid email or password.")