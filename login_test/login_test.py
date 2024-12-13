"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from login_test.pages import login, signup, pricing_page
from login_test.state import AppState

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to ErcasPay for Saas!", size="9"),
            rx.text(
                "Get the complete template here ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.button("Check Pricing!", on_click=rx.redirect("/pricing")),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.cond(
            AppState.logged_in,
            rx.text("User is currently logged")
        ),
        rx.logo()
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(signup, route="/register")
app.add_page(login, route="/login")
app.add_page(pricing_page, route="/pricing")
