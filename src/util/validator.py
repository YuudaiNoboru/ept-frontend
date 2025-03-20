import re

from services.new_user import create_new_user


async def validator_form_new_user(form, e):
    valid = True
    email_patern = re.compile(
        r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,}$'
    )
    # Precisa ter pelo menos 1 letra minúscula, 1 letra maiúscula, 1 número, 1 caractere especial e 8 caracteres
    password_patern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_\-#])[A-Za-z\d@$!%*?&_\-#]{8,}$'

    if len((form.input_nome.value.strip())) < 1:
        valid = False
        form.input_nome.error_text = 'Você deve digitar um nome válido.'
    else:
        form.input_nome.error_text = None

    if not email_patern.match(form.input_email.value or ''):
        valid = False
        form.input_email.error_text = 'Você deve digitar um email válido.'
    else:
        form.input_email.error_text = None

    if not re.match(password_patern, form.input_senha.value):
        valid = False
        form.input_senha.error_text = 'A senha deve conter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e símbolos.'
    else:
        form.input_senha.error_text = None
    if form.input_senha.value != form.input_senha_repitida.value:
        valid = False
        form.input_senha_repitida.error_text = 'As senhas deven ser iguais.'
    else:
        form.input_senha_repitida.error_text = None

    if valid:
        await create_new_user(
            nome=form.input_nome.value,
            email=form.input_email.value,
            senha=form.input_senha.value,
        )

    form.update()
