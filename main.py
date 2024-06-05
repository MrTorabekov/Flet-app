import time

import flet as ft

from flet import TextField
from flet_core.control_event import ControlEvent


#
# def main(page: ft.page):
#     text = ft.Text(value="My nick name is Torabekov_08",color="blue")
#     page.controls.append(text)
#     page.update()
#
#
# ft.app(target=main)


# def main(page:ft.Page):
#     text = ft.Text(color="blue")
#     page.add(text)
#     for i in range(10):
#         text.value = f"sleep {i}"
#         page.update()
#         time.sleep(1)
#
# ft.app(target=main)


def main(page: ft.Page) -> None:
    page.title = 'increment counter'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'light'

    text_number: TextField = TextField('0', text_align=ft.TextAlign.RIGHT, width=80)

    def decrement(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    def increment(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) + 1)
        page.update()


    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=decrement),
             text_number,
             ft.IconButton(ft.icons.ADD, on_click=increment)
             ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=decrement),
             text_number,
             ft.IconButton(ft.icons.ADD, on_click=increment)
             ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
