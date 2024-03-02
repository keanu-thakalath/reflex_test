import reflex as rx
from vly.plugins.user import AuthState
from reflex.components.radix.themes import theme



def login() -> rx.Component:
    """The login page."""
    return rx.container(
        rx.box(
            rx.vstack(
                rx.input(
                    placeholder="Username",
                    on_blur=AuthState.set_email,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    size="3",
                ),
                rx.button("Log in", on_click=AuthState.login, size="3", width="5em"),
                spacing="4",
            ),
            align_items="left",
            background="white",
            border="1px solid #eaeaea",
            padding="16px",
            width="400px",
            border_radius="8px",
        ),
        rx.text(
            "Don't have an account yet? ",
            rx.link("Sign up here.", href="/signup"),
            color="gray",
        )
    )

def signup() -> rx.Component:
    """The signup page."""
    return rx.container(
        rx.box(
            rx.vstack(
                rx.input(
                    placeholder="Username",
                    on_blur=AuthState.set_email,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    size="3",
                ),rx.input(
                    type="password",
                    placeholder="Confirm Password",
                    on_blur=AuthState.set_confirm_password,
                    size="3",
                ),
                rx.button("Log in", on_click=AuthState.signup, size="3", width="5em"),
                spacing="4",
            ),
            align_items="left",
            background="white",
            border="1px solid #eaeaea",
            padding="16px",
            width="400px",
            border_radius="8px",
        ),
        rx.text(
            "Don't have an account yet? ",
            rx.link("Sign up here.", href="/signup"),
            color="gray",
        )
    )

def index() -> rx.Component:
    return rx.text("Welcome to the Reflex Test!")

app = rx.App(theme=theme(appearance="light", has_background=True, radius="large", accent_color="teal"))
app.add_page(index, on_load=AuthState.check_login, route="/")
app.add_page(login, route="/login")
app.add_page(signup, route="/signup")