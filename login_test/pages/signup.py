import reflex as rx

from login_test.layouts import auth_layout
from login_test.state import AuthState

# def signup() -> rx.Component:
#     """The sign up page."""
#     return auth_layout(
#         rx.box(
#             rx.vstack(
#                 rx.input(
#                     placeholder="Username",
#                     on_blur=AuthState.set_username,
#                     size="3",
#                 ),
#                 rx.input(
#                     type="password",
#                     placeholder="Password",
#                     on_blur=AuthState.set_password,
#                     size="3",
#                 ),
#                 rx.input(
#                     type="password",
#                     placeholder="Confirm password",
#                     on_blur=AuthState.set_confirm_password,
#                     size="3",
#                 ),
#                 rx.button(
#                     "Sign up",
#                     on_click=AuthState.signup,
#                     size="3",
#                     width="6em",
#                 ),
#                 spacing="4",
#             ),
#             align_items="left",
#             background="white",
#             border="1px solid #eaeaea",
#             padding="16px",
#             width="400px",
#             border_radius="8px",
#         ),
#         rx.text(
#             "Already have an account? ",
#             rx.link("Sign in here.", href="/login"),
#             color="gray",
#         ),
#     )

def signup() -> rx.Component:
    return rx.card(
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
                    rx.input.slot(rx.icon("envelope")),
                    placeholder="user@gmail.com",
                    on_blur=AuthState.set_email,
                    type="email",
                    size="3",
                    width="100%",
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
                    on_blur=AuthState.set_username,
                    type="text",
                    size="3",
                    width="100%",
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
                    on_blur=AuthState.set_password,
                    type="password",
                    size="3",
                    width="100%",
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
            rx.button("Register", size="3", width="100%", on_click=AuthState.signup),
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