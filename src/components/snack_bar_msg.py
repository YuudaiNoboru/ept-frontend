import flet as ft


class ErrorSnackBar(ft.SnackBar):
    def __init__(self, message: str):
        super().__init__(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.icons.ERROR_OUTLINE, color=ft.Colors.RED_100),
                    ft.Text(value=message, color=ft.Colors.WHITE),
                ],
                spacing=15
            ),
            bgcolor=ft.Colors.RED_700,
            duration=3000,
            show_close_icon=True,
            close_icon_color=ft.Colors.WHITE,
            behavior=ft.SnackBarBehavior.FLOATING,
            elevation=10,
            margin=ft.margin.all(10),
            padding=ft.padding.symmetric(vertical=15, horizontal=20)
        )


# SnackBar de Sucesso (Verde)
class SuccessSnackBar(ft.SnackBar):
    def __init__(self, message: str):
        super().__init__(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, color=ft.Colors.GREEN_100),
                    ft.Text(value=message, color=ft.Colors.WHITE),
                ],
                spacing=15
            ),
            bgcolor=ft.Colors.GREEN_700,
            duration=2000,
            show_close_icon=True,
            close_icon_color=ft.Colors.WHITE,
            behavior=ft.SnackBarBehavior.FLOATING,
            elevation=10,
            margin=ft.margin.all(10),
            padding=ft.padding.symmetric(vertical=15, horizontal=20)
        )
