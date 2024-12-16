import reflex as rx
from login_test.state import AppState

def container(*children, **props) ->  rx.Component :
    """A fixed container based on a 960px grid."""
    # Enable override of default props.
    props = (
        dict(
            width="100%",
            max_width="960px",
            background="white",
            height="100%",
            px="9",
            margin="0 auto",
            position="relative",
        )
        | props
    )
    return rx.stack(*children, **props)


def popover(button: rx.Component, usd_amount: int, ngn_amount: int, plan: str) -> rx.Component:
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
                rx.button("Proceed to payment", on_click=lambda: AppState.handle_payment(usd_amount, ngn_amount, plan)),
                direction="column",
                spacing="3",
                align="center"
            )
        )
    )