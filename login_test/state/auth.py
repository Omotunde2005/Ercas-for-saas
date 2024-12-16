import reflex as rx
from sqlmodel import select
from passlib.context import CryptContext
from .base import State, User
import datetime

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthState(State):
    """The authentication state for sign up and login page."""

    def hash_password(self, password) -> str:
        return PWD_CONTEXT.hash(password)

    def verify_password(self, hashed_password, password) -> bool:
        return PWD_CONTEXT.verify(password, hashed_password)

    def signup(self, form_data):
        """Sign up a user."""
        password = form_data["password"]
        email = form_data["email"]
        username = form_data["username"]
        with rx.session() as session:
            if session.exec(select(User).where(User.email == email)).first():
                return rx.window_alert("User already exists.")
            hashed_password = self.hash_password(password)
            self.user = User(email=email, password=hashed_password, username=username, created_at=datetime.datetime.now())
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            if self.user:
                print(self.user.id)
            return rx.redirect("/dashboard")

    def login(self, form_data):
        """Log in a user."""
        email = form_data["email"]
        password = form_data["password"]
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.email == email)
            ).first()
            self.user = user
            if user and self.verify_password(user.password, password):
                return rx.redirect("/dashboard")
            else:
                return rx.window_alert("Invalid email or password.")