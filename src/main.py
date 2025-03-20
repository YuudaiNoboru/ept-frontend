import re

import flet as ft


class SingIn: ...


class ColumFormSingUp(ft.Column):
    def __init__(self):
        super().__init__()
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
        self.input_senha_repitida = ft.TextField(
            label='Senha',
            hint_text='Repita sua senha',
            password=True,
            can_reveal_password=True,
        )
        self.button_login = ft.OutlinedButton(
            text='Criar',
            style=ft.ButtonStyle(padding=ft.padding.symmetric(vertical=25)),
            expand=True,
            on_click=self.validar_form,
        )
        self.controls = [
            self.input_nome,
            self.input_email,
            self.input_senha,
            self.input_senha_repitida,
            ft.Container(
                content=ft.Row(
                    controls=[self.button_login],
                ),
                margin=ft.margin.only(top=20),
            ),
        ]

    def validar_form(self, e):
        valid = True
        email_patern = re.compile(
            r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,}$'
        )
        # Precisa ter pelo menos 1 letra minúscula, 1 letra maiúscula, 1 número, 1 caractere especial e 8 caracteres
        password_patern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_\-#])[A-Za-z\d@$!%*?&_\-#]{8,}$'

        if len((self.input_nome.value.strip())) < 1:
            valid = False
            self.input_nome.error_text = 'Você deve digitar um nome válido.'
        else:
            self.input_nome.error_text = None

        if not email_patern.match(self.input_email.value or ''):
            valid = False
            self.input_email.error_text = 'Você deve digitar um email válido.'
        else:
            self.input_email.error_text = None

        if not re.match(password_patern, self.input_senha.value):
            valid = False
            self.input_senha.error_text = 'A senha deve conter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e símbolos.'
        else:
            self.input_senha.error_text = None
        if self.input_senha.value != self.input_senha_repitida.value:
            valid = False
            self.input_senha_repitida.error_text = (
                'As senhas deven ser iguais.'
            )
        else:
            self.input_senha_repitida.error_text = None

        self.update()


class ContainerFormSingUp(ft.Container):
    def __init__(self):
        super().__init__()
        self.margin = ft.margin.only(top=25)
        self.padding = ft.padding.symmetric(horizontal=20)
        self.content = ColumFormSingUp()


class TabsBemVindo(ft.Tabs):
    def __init__(self):
        super().__init__()
        self.selected_index = 1
        self.tabs = [
            ft.Tab(text='Entre'),
            ft.Tab(text='Crie sua conta', content=ContainerFormSingUp()),
        ]


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
        self.controls = [self.titulo, self.sub_titulo, ft.Container(
            margin=ft.margin.symmetric(vertical=20, horizontal=20), content=TabsBemVindo())]


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
