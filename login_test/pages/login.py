import reflex as rx
from login_test.layouts import auth_layout
from login_test.state import AuthState

def login() ->  rx.Component:
    """The login page."""
    return auth_layout(
        rx.box(
            rx.vstack(
                rx.input(
                    placeholder="Username",
                    size="3",
                    on_blur=AuthState.set_username,
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    size="3",
                    on_blur=AuthState.set_password,
                ),
                rx.button("Log in", on_click=AuthState.login, size="3", width="5em"),
                spacing="4",
            ),
            align_items="left",
            background="white",
            border="1px solid #eaeaea",
            padding="16px",
            width="400px",
            border_radius="8px",
        ),
        rx.text(
            "Don't have an account yet? ",
            rx.link("Sign up here.", href="/register"),
            color="gray",
        ),
    )