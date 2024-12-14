import reflex as rx
from login_test.state import AppState

def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Home", "airplay", "/"),
        sidebar_item("Settings", "settings", "/settings"),
        sidebar_item("Upgrade plan", "align_center_vertical", "/pricing"),
        # rx.cond(
        #     forms_state.CreateBoardForm.can_create_board,
        #     sidebar_item("Create Board", "badge-plus", "/create/board")
        # ),
        sidebar_item("Log out", "circle-power", "/logout"),
        spacing="1",
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.drawer.root(
            rx.drawer.trigger(
                rx.icon("align-justify", size=30)
            ),
            rx.drawer.overlay(z_index="5"),
            rx.drawer.portal(
                rx.drawer.content(
                    rx.vstack(
                        rx.box(
                            rx.drawer.close(
                                rx.icon("x", size=30)
                            ),
                            width="100%",
                        ),
                        sidebar_items(),
                        spacing="5",
                        width="100%",
                    ),
                    top="auto",
                    right="auto",
                    height="100%",
                    width="20em",
                    padding="1.5em",
                    bg=rx.color("accent", 2),
                ),
                width="100%",
            ),
            direction="left",
        ),
        padding="1em"
    )

def dashboard() -> rx.Component:
    return rx.vstack(
        sidebar(),
        rx.section(
            rx.text(
                f'Welcome {AppState.user.username}!',
                size="6"
            ),
            padding="30px"
        )
    )
