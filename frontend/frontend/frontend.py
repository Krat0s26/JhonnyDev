import reflex as rx


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Jhonny Portillo", size="8"),
            rx.text("Data Center Technician"),
            rx.divider(),
            rx.heading("Skills", size="5"),
            rx.text("• Linux"),
            rx.text("• Networking"),
            rx.text("• Fiber Optics"),
            rx.text("• Python"),
            spacing="4",
            align="center",
        ),
        padding="2em",
    )


app = rx.App()
app.add_page(index)