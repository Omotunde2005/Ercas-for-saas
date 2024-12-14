"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from login_test.pages import login, signup, pricing_page, dashboard
from login_test.state import AppState

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to ErcasPay for Saas!", size="9"),
            rx.text(
                "Launch your app in days not months",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.cond(
                not AppState.logged_in,
                rx.hstack(
                    rx.button("Register", on_click=rx.redirect("/register")),
                    rx.button("Login", on_click=rx.redirect("/login")),
                    spacing=3
                )
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.section(
            rx.center(
                rx.vsatck(
                    rx.text("Checkout the available plans"),
                    rx.button("Pricing", on_click=rx.redirect("/pricing")),
                    align="center"
                )
            ),
            padding="10px"
        ),
        rx.cond(
            AppState.logged_in,
            rx.text("User is currently logged")
        ),
        rx.logo()
    )

@rx.page(route="/logout", on_load=AppState.logout)
def logout() -> rx.Component:
    return rx.container("Logged out")



app = rx.App()
app.add_page(index, route="/")
app.add_page(signup, route="/register")
app.add_page(login, route="/login")
app.add_page(pricing_page, route="/pricing")
app.add_page(dashboard, route="/dashboard")