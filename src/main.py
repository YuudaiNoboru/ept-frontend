import flet as ft

from components.column_form_login import ColumnFormLogin
from components.column_form_new_user import ColumnFormSignUp


class TabsBemVindo(ft.Tabs):
    def __init__(self):
        super().__init__()
        self.selected_index = 1
        self.tabs = [
            ft.Tab(
                icon=ft.Icons.LOGIN_OUTLINED,
                text='Entre',
                content=ft.Container(
                    margin=ft.margin.only(top=25),
                    padding=ft.padding.symmetric(horizontal=20),
                    content=ColumnFormLogin(self.mudar_tab),
                ),
            ),
            ft.Tab(
                icon=ft.Icons.PERSON_ADD_OUTLINED,
                text='Crie sua conta',
                content=ft.Container(
                    margin=ft.margin.only(top=25),
                    padding=ft.padding.symmetric(horizontal=20),
                    content=ColumnFormSignUp(self.mudar_tab),
                ),
            ),
        ]

    def mudar_tab(self, index):
        self.selected_index = index
        self.page.update()


class ColumnMain(ft.Column):
    def __init__(self):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 800
        self.height = 700
        self.titulo = ft.Text(
            'Seja bem vindo de volta!',
            theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
            text_align=ft.TextAlign.CENTER,
        )

        self.sub_titulo = ft.Text(
            'Crie sua conta ou faça login para explorar o app.',
            theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
            text_align=ft.TextAlign.CENTER,
        )
        self.controls = [
            self.titulo,
            self.sub_titulo,
            ft.Container(
                margin=ft.margin.symmetric(vertical=20, horizontal=20),
                content=TabsBemVindo(),
            ),
        ]


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.fonts = {'IndieFlower': '/fonts/IndieFlower-Regular.ttf'}
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.RED, font_family='IndieFlower'
    )
    page.padding = ft.padding.only(top=20, left=10, right=10)
    page.title = 'Seja Bem Vindo!'
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(ColumnMain())


ft.app(main, assets_dir='assets')
