"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from ercas_saas.pages import login, signup, pricing_page
from ercas_saas.state import AppState


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to ErcasPay for Saas!", size="9"),
            rx.text(
                "Launch your app in days not months",
                size="5",
            ),
            rx.cond(
                ~ AppState.logged_in,
                rx.hstack(
                    rx.button("Register", on_click=rx.redirect("/register")),
                    rx.button("Login", on_click=rx.redirect("/login")),
                    spacing="3"
                )
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.section(
            rx.center(
                rx.vstack(
                    rx.text("Checkout the available plans"),
                    rx.button("Pricing", on_click=rx.redirect("/pricing")),
                    align="center"
                )
            ),
            padding="10px"
        )
    )


# Logout Route
@rx.page(route="/logout", on_load=AppState.logout)
def logout() -> rx.Component:
    return rx.container("Logged out")



app = rx.App()
app.add_page(index, route="/")
app.add_page(login, route="/login")
app.add_page(pricing_page, route="/pricing")
app.add_page(signup, route="/register")