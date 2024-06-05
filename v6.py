import asyncio
import flet as ft

# buttonni ustiga bossangiz salom xabarini olasiz!

def main(page: ft.Page):
    async def button_click(e):
        await asyncio.sleep(1)
        page.add(ft.Text("Salom!"))

    page.add(
        ft.ElevatedButton("Say hello with delay!", on_click=button_click)
    )

ft.app(main)