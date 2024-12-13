import reflex as rx

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



def pricing_card(plan, description, price, features_list) -> rx.Component:
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
        rx.button(
            "Get started",
            size="3",
            variant="solid",
            width="100%",
            color_scheme="blue",
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
    return rx.container(
        rx.center(
            rx.heading("Select a pricing that fits your use case", size="8"),
            padding="10px",
            margin_bottom="10px"
        ),
        rx.grid(
            pricing_card("Free", "Ideal choice for personal use & for your next project.", "$0", beginner_plan_features_list),
            pricing_card("Starter", "Perfect for small teams", "$20", starter_plan_features_list),
            pricing_card("Enterprise", "Perfect for large teams with more needs", "$50", enterprise_plan_features_list),
            width="100%",
            spacing="4",
            columns=rx.breakpoints(initial="1", sm="1", md="3", lg="3"),
            padding="10px"
        )
    )