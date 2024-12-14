import reflex as rx
from login_test.layouts import auth_layout
from login_test.state import AuthState

# def login() ->  rx.Component:
#     """The login page."""
#     return auth_layout(
#         rx.box(
#             rx.vstack(
#                 rx.input(
#                     placeholder="Username",
#                     size="3",
#                     on_blur=AuthState.set_username,
#                 ),
#                 rx.input(
#                     type="password",
#                     placeholder="Password",
#                     size="3",
#                     on_blur=AuthState.set_password,
#                 ),
#                 rx.button("Log in", on_click=AuthState.login, size="3", width="5em"),
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
#             "Don't have an account yet? ",
#             rx.link("Sign up here.", href="/register"),
#             color="gray",
#         ),
#     )

def login() -> rx.Component:
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
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("user")),
                    placeholder="user@gmail.com",
                    on_blur=AuthState.set_email,
                    type="email",
                    size="3",
                    width="100%",
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
                    on_blur=AuthState.set_password,
                    type="password",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Sign in", size="3", width="100%", on_click=AuthState.login),
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