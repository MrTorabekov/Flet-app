import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent

# :)


def main(page: ft.Page) -> None:
    page.title = 'increment counter'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'light'

    text_number: TextField = TextField('0', text_align=ft.TextAlign.RIGHT, width=80)

    def minus(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    def plus(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) + 1)
        page.update()


    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=minus),
             text_number,
             ft.IconButton(ft.icons.ADD, on_click=plus)
             ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )



if __name__ == '__main__':
    ft.app(target=main)
