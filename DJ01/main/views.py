# views.py for main app
import datetime
from django.shortcuts import render


def index(request):
    # Получаем базовый контекст с активной главной страницей


    # Добавляем специфичные для главной страницы данные
    context={
        'page_title': 'Главная страница',
        'page_description': 'Добро пожаловать на наш сайт! Здесь вы найдете много полезной информации.',
        'content_items': [
            {
                'title': 'Первый блок',
                'description': 'Описание первого блока контента на сайте.',
                'image': 'img/1.png',
                'url': '/item/1/',
            },
            {
                'title': 'Второй блок',
                'description': 'Описание второго блока контента на сайте.',
                'image': 'img/2.png',
                'url': '/item/2/',
            },
            {
                'title': 'Третий блок',
                'description': 'Описание третьего блока контента на сайте.',
                'image': 'img/3.png',
                'url': '/item/3/',
            },
        ],
    }

    return render(request, 'main/index.html', context)


def about(request):
    # Получаем базовый контекст с активной страницей "О нас"

    # Добавляем специфичные данные
    context={
        'page_title': 'О нас',
        'page_description': 'Информация о нашей компании и команде.',
        'team_members': [
            {
                'name': 'Иван Иванов',
                'position': 'Директор',
                'bio': 'Более 10 лет опыта в индустрии.',
                'image': 'img/team1.jpg',
            },
            {
                'name': 'Мария Петрова',
                'position': 'Ведущий разработчик',
                'bio': 'Эксперт в Python и Django.',
                'image': 'img/team2.jpg',
            },
            {
                'name': 'Алексей Сидоров',
                'position': 'Дизайнер',
                'bio': 'Создает уникальные и удобные интерфейсы.',
                'image': 'img/team3.jpg',
            },
        ],
    }

    return render(request, 'main/about.html', context)


def services(request):
    # Получаем базовый контекст с активной страницей "Услуги"

    # Добавляем специфичные данные
    context={
        'page_title': 'Услуги',
        'page_description': 'Услуги, которые мы предлагаем нашим клиентам.',
        'services_list': [
            {
                'title': 'Веб-разработка',
                'description': 'Создание современных веб-приложений на Django.',
                'icon': 'bi-code-slash',
            },
            {
                'title': 'Дизайн интерфейсов',
                'description': 'Разработка удобных и интуитивно понятных интерфейсов.',
                'icon': 'bi-palette',
            },
            {
                'title': 'SEO-оптимизация',
                'description': 'Повышение видимости вашего сайта в поисковых системах.',
                'icon': 'bi-graph-up',
            },
            {
                'title': 'Поддержка и сопровождение',
                'description': 'Техническая поддержка и обновление существующих проектов.',
                'icon': 'bi-gear',
            },
        ],
    }

    return render(request, 'main/services.html', context)


def blog(request):
    # Получаем базовый контекст с активной страницей "Блог"

    # Добавляем специфичные данные
    context={
        'page_title': 'Блог',
        'page_description': 'Последние новости и статьи нашей компании.',
        'blog_posts': [
            {
                'title': 'Обновление Django 5.0',
                'date': '20 апреля 2025',
                'short_description': 'Обзор новых функций в Django 5.0.',
                'image': 'img/django.png',
                'url': '/blog/post1/',
            },
            {
                'title': 'Как оптимизировать Django-приложение',
                'date': '15 апреля 2025',
                'short_description': 'Полезные советы по оптимизации производительности.',
                'image': 'img/PythonDjango.jpg',
                'url': '/blog/post2/',
            },
            {
                'title': 'Bootstrap 6: что нового',
                'date': '10 апреля 2025',
                'short_description': 'Обзор новых компонентов и функций в Bootstrap 6.',
                'image': 'img/bootstrap.jpg',
                'url': '/blog/post3/',
            },
        ],
    }

    return render(request, 'main/blog.html', context)


def contacts(request):
    from utils.context_processors import FOOTER_INFO

    # Данные для страницы контактов
    context={
        'page_title': 'Контакты',
        'page_description': 'Как с нами связаться.',
        'contact_info': {
            'address': FOOTER_INFO['address'],
            'phone': FOOTER_INFO['phone'],
            'email': FOOTER_INFO['email'],
            'working_hours': 'Пн-Пт: 9:00 - 18:00',
        },
        'social_media': [
            {'name': 'Facebook', 'url': 'https://facebook.com/', 'icon': 'bi-facebook'},
            {'name': 'Twitter', 'url': 'https://twitter.com/', 'icon': 'bi-twitter'},
            {'name': 'Instagram', 'url': 'https://instagram.com/', 'icon': 'bi-instagram'},
            {'name': 'LinkedIn', 'url': 'https://linkedin.com/', 'icon': 'bi-linkedin'},
        ],
    }

    return render(request, 'main/contacts.html', context)