# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def open_browser(browser_name):
    print(f'Название функции "{open_browser.__name__.capitalize().replace("_", " ")}", у которой аргемент -', browser_name)


open_browser("Browser name")


def go_to_companyname_homepage(page_url):
    print(f'Название функции "{go_to_companyname_homepage.__name__.capitalize().replace("_", " ")}", у которой аргемент -', page_url)


go_to_companyname_homepage("Page url")


def find_registration_button_on_login_page(page_url, button_text):
    print(f'Название функции "{find_registration_button_on_login_page.__name__.capitalize().replace("_", " ")}", у которой аргементы -',
          page_url, button_text)


find_registration_button_on_login_page("Page url и", "Button text")









