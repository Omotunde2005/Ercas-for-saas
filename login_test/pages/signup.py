import reflex as rx

from login_test.layouts import auth_layout
from login_test.state import AuthState


def signup() -> rx.Component:
    return rx.container(
        rx.form(
            rx.card(
                rx.vstack(
                    rx.center(
                        rx.image(
                            src="/logo.jpg",
                            width="2.5em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.heading(
                            "Create an account",
                            size="6",
                            as_="h2",
                            text_align="center",
                            width="100%",
                        ),
                        direction="column",
                        spacing="5",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text(
                            "Email address",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("blend")),
                            placeholder="user@gmail.com",
                            type="email",
                            size="3",
                            width="100%",
                            name="email"
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text(
                            "Username",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            placeholder="Enter your username",
                            type="text",
                            size="3",
                            width="100%",
                            name="username"
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),

                    rx.vstack(
                        rx.text(
                            "Password",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            placeholder="Enter your password",
                            type="password",
                            size="3",
                            width="100%",
                            name="password"
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.box(
                        rx.checkbox(
                            "Agree to Terms and Conditions",
                            default_checked=True,
                            spacing="2",
                        ),
                        width="100%",
                    ),
                    rx.button("Register", size="3", width="100%", type="submit"),
                    rx.center(
                        rx.text("Already registered?", size="3"),
                        rx.link("Sign in", href="/login", size="3"),
                        opacity="0.8",
                        spacing="2",
                        direction="row",
                        width="100%",
                    ),
                    spacing="6",
                    width="100%",
                ),
                max_width="28em",
                size="4",
                width="100%",
            ),
            on_submit=AuthState.signup
        )
    )