import flet as ft

# Ovoz balandlagich

def main(page):

    def slider_changed(e):
        t.value = f"Ovoz balandligi {e.control.value} %"
        page.update()

    t = ft.Text()
    page.add(
        ft.Text("ovoz balandlagich"),
        ft.Slider(min=0, max=100, divisions=10, label="{value}%", on_change=slider_changed), t)

ft.app(target=main)