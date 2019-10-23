# Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
# Вывод всех проверенных пользователей.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# def get_formatted_name(first_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""

#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)



# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Возвращает аккуратно отформатированное полное имя."""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name

#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#     musician = get_formatted_name('jimi', 'hendrix')
#     print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# def build_person(first_name, last_name):
#     """Возвращает словарь с информацией о человеке."""

#     person = {'first': first_name, 'last': last_name}

#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)

# def get_formatted_name(first_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# # Бесконечный цикл!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

# formatted_name = get_formatted_name(f_name, l_name)
# print("\nHello, " + formatted_name + "!")




# def make_pizza(*toppings):
#     """Вывод списка заказанных дополнений."""
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

