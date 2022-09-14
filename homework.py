def open_browser(browser_name):
    print_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_name(find_registration_button_on_login_page, page_url, button_text)


def print_name(func, *args):
    print(f'Название функции "{func.__name__.capitalize().replace("_", " ")}" и её аргументы -', *args)


if __name__ == '__main__':
    open_browser("Opera"),
    go_to_companyname_homepage("www.vk.com"),
    find_registration_button_on_login_page("www.vk.com", "Зарегистрироваться")
