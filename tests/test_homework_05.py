from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=4)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    is_dark_theme = current_time.hour >= 22 or current_time.hour < 6

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=5)
    dark_theme_enabled_by_user = None
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    is_dark_theme = None

    is_dark_theme = dark_theme_enabled_by_user if dark_theme_enabled_by_user is not None \
        else (is_dark_theme := current_time.hour >= 22 or current_time.hour < 6)

    """
    Ниже альтернативное решение, но длинное, укоротил выше вроде корректно через моржевой оператор
    """
    # if dark_theme_enabled_by_user is None:
    #     is_dark_theme = current_time.hour >= 22 or current_time.hour < 6
    # elif dark_theme_enabled_by_user:
    #     is_dark_theme = True
    # else:
    #     is_dark_theme = False

    assert is_dark_theme is True

def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"

    suitable_user = next((user for user in users if user["name"] == "Olga"), None)

    assert suitable_user == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = [user for user in users if user["age"] <= 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

    # либо решение через filter и lambda
    # suitable_users = list(filter(lambda user: user['age'] < 20, users))
    # assert suitable_users == [
    #         {"name": "Stanislav", "age": 15},
    #         {"name": "Maria", "age": 18},
    #     ]

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def simple_read_function(my_func, *args):
    func_name = my_func.__name__.replace('_', ' ').title()
    func_args = ', '.join(args)
    return f"{func_name} [{func_args}]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = simple_read_function(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"
    print("\n" + actual_result)


def go_to_companyname_homepage(page_url):
    actual_result = simple_read_function(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"
    print(actual_result)

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = simple_read_function(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
    print(actual_result)