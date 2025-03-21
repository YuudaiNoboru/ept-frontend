import flet as ft

from components.snack_bar_msg import ErrorSnackBar, SuccessSnackBar
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
            label='Nome', hint_text='Insira o seu nome',
            prefix_icon=ft.Icon(ft.Icons.PERSON_OUTLINE),
        )
        self.input_email = ft.TextField(
            label='E-mail',
            hint_text='Insira o seu email',
            prefix_icon=ft.Icon(ft.Icons.EMAIL_OUTLINED),
            keyboard_type=ft.KeyboardType.EMAIL,
        )
        self.input_senha = ft.TextField(
            label='Senha',
            hint_text='Insira sua senha',
            password=True,
            prefix_icon=ft.Icon(ft.Icons.LOCK_OUTLINE),
            can_reveal_password=True,
        )
        self.input_senha_repetida = ft.TextField(
            label='Senha',
            hint_text='Repita sua senha',
            password=True,
            prefix_icon=ft.Icon(ft.Icons.LOCK_OUTLINE),
            can_reveal_password=True,
        )
        self.button_login = ft.OutlinedButton(
            text='Criar',
            style=ft.ButtonStyle(padding=ft.padding.symmetric(vertical=25)),
            expand=True,
            icon=ft.Icon(name=ft.Icons.ARROW_FORWARD_OUTLINED),
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
                self.page.open(SuccessSnackBar('Usuário criado com sucesso!'))
        except APIError as err:
            self.page.open(ErrorSnackBar(err.message))
