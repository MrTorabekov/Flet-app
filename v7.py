import flet as ft

# ko'rinishi telegram chatga oxshaydi


class Message(ft.Container):
    def __init__(self, author, body):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text(author, weight=ft.FontWeight.BOLD),
                ft.Text(body),
            ],
        )
        self.border = ft.border.all(1, ft.colors.WHITE70)
        self.border_radius = ft.border_radius.all(15)
        self.bgcolor = ft.colors.RED
        self.padding = 20
        self.expand = True
        self.expand_loose = True


def main(page: ft.Page):
    chat = ft.ListView(
        padding=10,
        spacing=20,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    Message(
                        author="John",
                        body="Hi, how are you?",
                    ),
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    Message(
                        author="Jake",
                        body="Hi I am good thanks, how about you?",
                    ),
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    Message(

                        author="John",
                        body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    ),
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    Message(
                        author="Jake",
                        body="Thank you!",
                    ),
                ],
            ),
        ],
    )

    page.window_width = 393
    page.window_height = 600
    page.window_always_on_top = False

    page.add(chat)


ft.app(target=main)
