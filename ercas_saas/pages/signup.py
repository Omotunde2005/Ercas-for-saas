import reflex as rx
from ercas_saas.state import AuthState


# The signup route
def signup() -> rx.Component:
    """This component is used to style the signup page"""
    return rx.container(
        rx.center(
            rx.form(
                rx.center(
                    rx.card(
                        rx.vstack(
                            rx.center(
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
                            rx.button(
                                rx.cond(
                                    AuthState.btn_loading,
                                    rx.spinner(size="3"),
                                    rx.text("Register")
                                ),
                                size="3", 
                                width="100%", 
                                type="submit",
                                on_click=AuthState.btn_clicked,
                                disabled=AuthState.btn_loading
                            ),
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
                    )
                ),
                on_submit=AuthState.signup
            )
        )
    )

