import reflex as rx
from .base import State

class AppState(State):
    
    def handle_payment(self):
        if not self.logged_in:
            return rx.redirect("/register")
