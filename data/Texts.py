Texts = {
    'start_state': 'Добро пожаловать в Market-bot',
    'balance_state': 'Введите сумму пополнения'
}


def gen_profile_text(name, balance, bought, username):
    text = f'Ваш профиль, {name}:\n' \
           f'Баланс: {balance}\n' \
           f'Покупки: {bought}\n' \
           f'Username: @{username}'
    return text