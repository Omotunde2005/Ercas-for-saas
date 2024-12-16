import reflex as rx
from ercas_saas.state import AppState




def popover(button: rx.Component, usd_amount: int, ngn_amount: int, plan: str) -> rx.Component:
    """Popover that is displayed when a user tries to subscribe to a plan"""
    return rx.popover.root(
        rx.popover.trigger(
            button
        ),
        rx.popover.content(
            rx.flex(
                rx.center(
                    rx.text("Select a currency?"),
                    rx.select(
                        ["NGN", "USD"],
                        value=AppState.currency,
                        on_change=AppState.change_value
                    ),
                    spacing="3"
                ),
                rx.button(
                    rx.cond(
                        AppState.payment_btn_loading,
                        rx.spinner(size="3"),
                        rx.text("Proceed to payment")
                    ), 
                    on_click=lambda: AppState.handle_payment(usd_amount, ngn_amount, plan)
                ),
                direction="column",
                spacing="3",
                align="center"
            )
        )
    )