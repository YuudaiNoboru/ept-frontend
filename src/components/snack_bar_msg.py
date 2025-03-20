import flet as ft


class SnackBarMsg(ft.SnackBar):
    def __init__(self, msg):
        super().__init__(content=ft.Text(value=msg))
