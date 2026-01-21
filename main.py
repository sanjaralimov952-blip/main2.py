# main2.py
import flet as ft
from datetime import datetime, timezone, timedelta


def main(page: ft.Page):
    text_hello = ft.Text(value="Hello world")
    page.theme_mode = ft.ThemeMode.DARK
    text_hello.value = "Hello"

    greeting_history = []
    history_text = ft.Text("История привествий:")

    name_input = ft.TextField(label="Введите что нибудь")

    def text_name(e):
        print(name_input.value)
        tz = timezone(timedelta(hours=6))
        now = datetime.now(tz)

        if name_input.value:
            text_hello.value = f"{now.strftime('%Y-%m-%d %H:%M:%S')} hello {name_input.value}"
            greeting_history.append(name_input.value)

        name_input.value = None
        history_text.value = "История привествий :\n" + ",\n".join(greeting_history)
        page.update()

    def change_theme(e):
        page.theme_mode = (
            ft.ThemeMode.LIGHT
            if page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        page.update()

    def sort_history(e):
        greeting_history.sort(key=str.lower)
        history_text.value = "История привествий :\n" + ",\n".join(greeting_history)
        page.update()

    elevated_button = ft.ElevatedButton("send", on_click=text_name)
    sort_button = ft.ElevatedButton("Сортировать по алфавиту", on_click=sort_history)
    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=change_theme)

    name_input.on_submit = text_name

    page.add(text_hello,name_input,elevated_button,sort_button,thememode_button,history_text)


ft.app(target=main)
