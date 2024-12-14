import reflex as rx
from sqlmodel import select
from passlib.context import CryptContext
from .base import State, User
import datetime

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthState(State):
    """The authentication state for sign up and login page."""

    username: str
    password: str
    email: str

    def hash_password(self) -> str:
        return PWD_CONTEXT.hash(self.password)

    def verify_password(self, hashed_password) -> str:
        return PWD_CONTEXT.verify(self.password, hashed_password)

    def signup(self):
        """Sign up a user."""
        with rx.session() as session:
            if session.exec(select(User).where(User.email == self.email)).first():
                return rx.window_alert("User already exists.")
            hashed_password = self.hash_password()
            self.user = User(email=self.email, password=hashed_password, username=self.username, created_at=datetime.datetime.now())
            print(self.user)
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            self.username and self.password and self.email =  " "
            return rx.redirect("/dashboard")

    def login(self):
        """Log in a user."""
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.email == self.email)
            ).first()
            if user and self.verify_password(user.password):
                self.user = user
                return rx.redirect("/dashboard")
            else:
                return rx.window_alert("Invalid email or password.")