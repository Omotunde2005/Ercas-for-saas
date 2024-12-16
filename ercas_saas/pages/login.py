import reflex as rx
from ercas_saas.state import AuthState


# This login page route
def login() -> rx.Component:
    """This component styles the login page"""
    return rx.container(
        rx.center(
            rx.form(
                rx.center(
                    rx.card(
                        rx.vstack(
                            rx.center(
                                rx.heading(
                                    "Sign in to your account",
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
                                    width="100%"
                                ),
                                rx.input(
                                    rx.input.slot(rx.icon("blend")),
                                    placeholder="user@gmail.com",
                                    type="email",
                                    size="3",
                                    width="100%",
                                    name="email"
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.hstack(
                                    rx.text(
                                        "Password",
                                        size="3",
                                        weight="medium",
                                    ),
                                    rx.link(
                                        "Forgot password?",
                                        href="#",
                                        size="3",
                                    ),
                                    justify="between",
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
                                spacing="2",
                                width="100%",
                            ),
                            rx.button(
                                rx.cond(
                                    AuthState.btn_loading,
                                    rx.spinner(size="3"),
                                    rx.text("Sign in")
                                ),
                                size="3", 
                                width="100%", 
                                type="submit",
                                on_click=AuthState.btn_clicked
                            ),
                            rx.center(
                                rx.text("New here?", size="3"),
                                rx.link("Sign up", href="/register", size="3"),
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
                    )
                ),
                on_submit=AuthState.login
            )
        ),
        padding="10px"
    )