from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


# views.py
import datetime
from django.shortcuts import render


def index(request):
    # Данные для контекста, включая меню и информацию для футера
    context = {
        'site_name': 'Мой проект',
        'page_title': 'Главная страница',
        'page_description': 'Добро пожаловать на наш сайт! Здесь вы найдете много полезной информации.',
        'current_year': datetime.datetime.now().year,

        # Пункты меню
        'menu_items': [
            {'title': 'Главная', 'url': '/', 'active': True},
            {'title': 'О нас', 'url': '/about/', 'active': False},
            {'title': 'Услуги', 'url': '/services/', 'active': False},
            {'title': 'Блог', 'url': '/blog/', 'active': False},
            {'title': 'Контакты', 'url': '/contacts/', 'active': False},
        ],

        # Информация для футера
        'footer': {
            'description': 'Наш проект создан для демонстрации возможностей Django и Bootstrap.',
            'links': [
                {'title': 'Политика конфиденциальности', 'url': '/privacy/'},
                {'title': 'Условия использования', 'url': '/terms/'},
                {'title': 'Карта сайта', 'url': '/sitemap/'},
            ],
            'address': 'ул. Примерная, 123, г. Москва',
            'phone': '+7 (999) 123-45-67',
            'email': 'info@example.com',
        },

        # Основной контент страницы
        'content_items': [
            {
                'title': 'Первый блок',
                'description': 'Описание первого блока контента на сайте.',
                'image': '/static/img/item1.jpg',
                'url': '/item/1/',
            },
            {
                'title': 'Второй блок',
                'description': 'Описание второго блока контента на сайте.',
                'image': '/static/img/item2.jpg',
                'url': '/item/2/',
            },
            {
                'title': 'Третий блок',
                'description': 'Описание третьего блока контента на сайте.',
                'image': '/static/img/item3.jpg',
                'url': '/item/3/',
            },
        ],
    }

    return render(request, 'index.html', context)
