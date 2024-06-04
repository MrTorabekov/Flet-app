import flet as ft

def main(page: ft.page):
    text = ft.Text(value="My nick name is Torabekov_08",color="blue")
    page.controls.append(text)
    page.update()


ft.app(target=main)