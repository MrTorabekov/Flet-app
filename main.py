import time

import flet as ft
#
# def main(page: ft.page):
#     text = ft.Text(value="My nick name is Torabekov_08",color="blue")
#     page.controls.append(text)
#     page.update()
#
#
# ft.app(target=main)



def main(page:ft.Page):
    text = ft.Text(color="blue")
    page.add(text)
    for i in range(10):
        text.value = f"sleep {i}"
        page.update()
        time.sleep(1)

ft.app(target=main)