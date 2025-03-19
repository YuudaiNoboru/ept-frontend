import flet as ft


class SingIn:
    ...


class ColumFormSingUp(ft.Column):
    def __init__(self):
        super().__init__()
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
            style=ft.ButtonStyle(
                padding=ft.padding.symmetric(vertical=25)
            ),
            expand=True,
            on_click=self.validar_form,
        )
        self.controls = [
            self.input_nome,
            self.input_email,
            self.input_senha,
            self.input_senha_repitida,
            ft.Container(content=ft.Row(
                controls=[self.button_login],
            ), margin=ft.margin.only(top=25)),
        ]

    def validar_form(self, e):
        valid = True

        if len((self.input_nome.value.strip())) < 1:
            valid = False
            self.input_nome.error_text = 'Você deve digitar um nome válido.'
        else:
            self.input_nome.error_text = None

        self.update()


class ContainerFormSingUp(ft.Container):
    def __init__(self):
        super().__init__()
        self.margin = ft.margin.only(top=25)
        self.content = ColumFormSingUp()


class TabsBemVindo(ft.Tabs):
    def __init__(self):
        super().__init__()
        self.selected_index = 1
        self.tabs = [
            ft.Tab(text='Entre'),
            ft.Tab(text='Crie sua conta', content=ContainerFormSingUp()),
        ]


class ContainerBemVindo(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.symmetric(vertical=50, horizontal=50)
        self.content = TabsBemVindo()


class ColumnMain(ft.Column):
    def __init__(self):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 800
        self.titulo = ft.Text(
            'Seja bem vindo de volta!',
            theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
        )

        self.sub_titulo = ft.Text(
            'Crie sua conta ou faça login para explorar o app.',
            theme_style=ft.TextThemeStyle.TITLE_LARGE,
        )
        self.controls = [self.titulo, self.sub_titulo, ContainerBemVindo()]


def main(page: ft.Page):
    page.fonts = {'IndieFlower': '/fonts/IndieFlower-Regular.ttf'}
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.RED, font_family='IndieFlower'
    )
    page.padding = ft.padding.only(top=50)
    page.title = 'Seja Bem Vindo!'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(ColumnMain())


ft.app(main, assets_dir='assets')
