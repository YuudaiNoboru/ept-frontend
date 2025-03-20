import flet as ft

from components.snack_bar_msg import SnackBarMsg
from util.exception import APIError
from util.validator import validator_form_new_user


class ColumnFormSignUp(ft.Column):
    def __init__(self, callback_mudar_tab):
        super().__init__()
        self.callback_mudar_tab = callback_mudar_tab
        self.expand = True
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.alignment = ft.MainAxisAlignment.START
        self.spacing = 25
        self.input_nome = ft.TextField(
            label='Nome', hint_text='Insira o seu nome'
        )
        self.input_email = ft.TextField(
            label='E-mail',
            hint_text='Insira o seu email',
            keyboard_type=ft.KeyboardType.EMAIL,
        )
        self.input_senha = ft.TextField(
            label='Senha',
            hint_text='Insira sua senha',
            password=True,
            can_reveal_password=True,
        )
        self.input_senha_repetida = ft.TextField(
            label='Senha',
            hint_text='Repita sua senha',
            password=True,
            can_reveal_password=True,
        )
        self.button_login = ft.OutlinedButton(
            text='Criar',
            style=ft.ButtonStyle(padding=ft.padding.symmetric(vertical=25)),
            expand=True,
            on_click=self.submit_form,
        )
        self.controls = [
            self.input_nome,
            self.input_email,
            self.input_senha,
            self.input_senha_repetida,
            ft.Container(
                content=ft.Row(
                    controls=[self.button_login],
                ),
                margin=ft.margin.only(top=20),
            ),
        ]

    async def submit_form(self, e):
        try:
            self.user = await validator_form_new_user(self, e)
            if self.user:
                self.callback_mudar_tab(0)
        except APIError as err:
            self.page.open(SnackBarMsg(err.message))


class ContainerFormSignUp(ft.Container):
    def __init__(self, callback_mudar_tab):
        super().__init__()
        self.margin = ft.margin.only(top=25)
        self.padding = ft.padding.symmetric(horizontal=20)
        self.content = ColumnFormSignUp(callback_mudar_tab)


class TabsBemVindo(ft.Tabs):
    def __init__(self):
        super().__init__()
        self.selected_index = 1
        self.tabs = [
            ft.Tab(text='Entre'),
            ft.Tab(
                text='Crie sua conta',
                content=ContainerFormSignUp(
                    self.mudar_tab
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
