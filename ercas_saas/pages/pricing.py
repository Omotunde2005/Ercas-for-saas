import reflex as rx
from ercas_saas.state import AppState
from ercas_saas.components import popover

def feature_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon("check", color=rx.color("grass", 9)),
        rx.text(text, size="4"),
    )


def features(features_list) -> rx.Component:
    return rx.vstack(
        rx.foreach(
            features_list, feature_item
        ),
        width="100%",
        align_items="start",
    )


beginner_plan_features_list = [
    "24/7 customer support",
    "Daily backups",
    "Advanced analytics",
    "Customizable templates",
    "Priority email support"
]


starter_plan_features_list = [
    "24/7 customer support",
    "Daily backups",
    "Advanced analytics",
    "Customizable templates",
    "Priority email support"
]


enterprise_plan_features_list = [
    "24/7 customer support",
    "Daily backups",
    "Advanced analytics",
    "Customizable templates",
    "Priority email support"
]


# A pricing card component. You can use this for multiple card components in your pricing page
def pricing_card(plan, description, price, features_list, usd_amount: int, ngn_amount: int) -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text(plan, weight="bold", size="6"),
            rx.text(
                description,
                size="4",
                opacity=0.8,
                align="center",
            ),
            rx.hstack(
                rx.text(
                    price,
                    weight="bold",
                    font_size="3rem",
                    trim="both",
                ),
                rx.text(
                    "/month",
                    size="4",
                    opacity=0.8,
                    trim="both",
                ),
                width="100%",
                align_items="end",
                justify="center",
            ),
            width="100%",
            align="center",
            spacing="6",
        ),
        features(features_list),
        rx.cond(
            AppState.logged_in,
            popover(
                rx.button(
                    "Pay",
                    size="3",
                    variant="solid",
                    width="100%",
                    color_scheme="blue"
                ),
                usd_amount,
                ngn_amount,
                plan
            ),
            rx.button(
                "Get started",
                size="3",
                variant="solid",
                width="100%",
                color_scheme="blue",
                on_click=rx.redirect("/register")
            ),

        ),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        justify="center",
        border_radius="0.5rem",
    )

# A pricing card component for the free/beginner plan.
def beginner_pricing_card(beginner_plan_features) -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("Free", weight="bold", size="6"),
            rx.text(
                "Start with the basics",
                size="4",
                opacity=0.8,
                align="center",
            ),
            rx.hstack(
                rx.text(
                    "$0",
                    weight="bold",
                    font_size="3rem",
                    trim="both",
                ),
                rx.text(
                    "/month",
                    size="4",
                    opacity=0.8,
                    trim="both",
                ),
                width="100%",
                align_items="end",
                justify="center",
            ),
            width="100%",
            align="center",
            spacing="6",
        ),
        features(beginner_plan_features),
        rx.button(
            "Get started",
            size="3",
            variant="solid",
            width="100%",
            color_scheme="blue",
            on_click=rx.cond(
                AppState.logged_in,
                rx.redirect("/dashboard"),
                rx.redirect("/register")
            )
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        justify="center",
        border_radius="0.5rem",
    )


def pricing_page() -> rx.Component:
    """The pricing page route"""
    return rx.container(
        rx.center(
            rx.heading("Select a pricing that fits your use case", size="8"),
            padding="10px",
            margin_bottom="10px"
        ),
        rx.grid(
            beginner_pricing_card(beginner_plan_features_list),
            pricing_card("Starter", "Perfect for small teams", "$20", starter_plan_features_list, 100, 100),
            pricing_card("Enterprise", "Perfect for large teams with more needs", "$50", enterprise_plan_features_list, 100, 100),
            width="100%",
            spacing="4",
            columns=rx.breakpoints(initial="1", sm="1", md="3", lg="3"),
            padding="10px"
        )
    )


# The redirect page after the user has completed payments on the ErcasPay payment link
@rx.page(route="/verify/payment", on_load=AppState.verify_payment)
def redirect_page() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.heading("Redirecting to dashboard", size="7"),
            rx.spinner(size="3"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
