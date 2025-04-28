# views.py
import datetime
from django.shortcuts import render

# Общие данные для всех страниц
SITE_INFO = {
    'site_name': 'Проект DJ01',
    'current_year': datetime.datetime.now().year,
}

# Базовые пункты меню
DEFAULT_MENU = [
    {'title': 'Главная', 'url': '/', 'active': False},
    {'title': 'О нас', 'url': '/about/', 'active': False},
    {'title': 'Услуги', 'url': '/services/', 'active': False},
    {'title': 'Блог', 'url': '/blog/', 'active': False},
    {'title': 'Контакты', 'url': '/contacts/', 'active': False},
]

# Данные для футера (общие для всех страниц)
FOOTER_INFO = {
    'description': 'Наш проект создан для демонстрации возможностей Django и Bootstrap.',
    'links': [
        {'title': 'Политика конфиденциальности', 'url': '/privacy/'},
        {'title': 'Условия использования', 'url': '/terms/'},
        {'title': 'Карта сайта', 'url': '/sitemap/'},
    ],
    'address': 'ул. Примерная, 12, г. Таллин',
    'phone': '+372 51234567',
    'email': 'info@example.com',
}


def get_base_context(active_page):
    """
    Создаёт базовый контекст с общими данными для всех страниц.
    Устанавливает активный пункт меню.
    """
    # Копируем меню, чтобы не изменять оригинал
    menu_items = DEFAULT_MENU.copy()

    # Устанавливаем активный пункт меню
    for item in menu_items:
        if item['url'] == active_page:
            item['active'] = True
        else:
            item['active'] = False

    # Формируем базовый контекст
    context = {
        **SITE_INFO,
        'menu_items': menu_items,
        'footer': FOOTER_INFO,
    }

    return context


def index(request):
    # Получаем базовый контекст с активной главной страницей
    context = get_base_context('/')

    # Добавляем специфичные для главной страницы данные
    context.update({
        'page_title': 'Главная страница',
        'page_description': 'Добро пожаловать на наш сайт! Здесь вы найдете много полезной информации.',
        'content_items': [
            {
                'title': 'Первый блок',
                'description': 'Описание первого блока контента на сайте.',
                'image': '/static/img/1.png',
                'url': '/item/1/',
            },
            {
                'title': 'Второй блок',
                'description': 'Описание второго блока контента на сайте.',
                'image': '/static/img/2.png',
                'url': '/item/2/',
            },
            {
                'title': 'Третий блок',
                'description': 'Описание третьего блока контента на сайте.',
                'image': '/static/img/3.png',
                'url': '/item/3/',
            },
        ],
    })

    return render(request, 'index.html', context)


def about(request):
    # Получаем базовый контекст с активной страницей "О нас"
    context = get_base_context('/about/')

    # Добавляем специфичные данные
    context.update({
        'page_title': 'О нас',
        'page_description': 'Информация о нашей компании и команде.',
        'team_members': [
            {
                'name': 'Иван Иванов',
                'position': 'Директор',
                'bio': 'Более 10 лет опыта в индустрии.',
                'image': '/static/img/team1.jpg',
            },
            {
                'name': 'Мария Петрова',
                'position': 'Ведущий разработчик',
                'bio': 'Эксперт в Python и Django.',
                'image': '/static/img/team2.jpg',
            },
            {
                'name': 'Алексей Сидоров',
                'position': 'Дизайнер',
                'bio': 'Создает уникальные и удобные интерфейсы.',
                'image': '/static/img/team3.jpg',
            },
        ],
    })

    return render(request, 'about.html', context)


def services(request):
    # Получаем базовый контекст с активной страницей "Услуги"
    context = get_base_context('/services/')

    # Добавляем специфичные данные
    context.update({
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
    })

    return render(request, 'services.html', context)


def blog(request):
    # Получаем базовый контекст с активной страницей "Блог"
    context = get_base_context('/blog/')

    # Добавляем специфичные данные
    context.update({
        'page_title': 'Блог',
        'page_description': 'Последние новости и статьи нашей компании.',
        'blog_posts': [
            {
                'title': 'Обновление Django 5.0',
                'date': '20 апреля 2025',
                'short_description': 'Обзор новых функций в Django 5.0.',
                'image': '/static/img/django.png',
                'url': '/blog/post1/',
            },
            {
                'title': 'Как оптимизировать Django-приложение',
                'date': '15 апреля 2025',
                'short_description': 'Полезные советы по оптимизации производительности.',
                'image': '/static/img/PythonDjango.jpg',
                'url': '/blog/post2/',
            },
            {
                'title': 'Bootstrap 6: что нового',
                'date': '10 апреля 2025',
                'short_description': 'Обзор новых компонентов и функций в Bootstrap 6.',
                'image': '/static/img/bootstrap.jpg',
                'url': '/blog/post3/',
            },
        ],
    })

    return render(request, 'blog.html', context)


def contacts(request):
    # Получаем базовый контекст с активной страницей "Контакты"
    context = get_base_context('/contacts/')

    # Данные для страницы контактов
    context.update({
        'page_title': 'Контакты',
        'page_description': 'Как с нами связаться.',
        'contact_info': {
            'address': context['footer']['address'],
            'phone': context['footer']['phone'],
            'email': context['footer']['email'],
            'working_hours': 'Пн-Пт: 9:00 - 18:00',
        },
        'social_media': [
            {'name': 'Facebook', 'url': 'https://facebook.com/', 'icon': 'bi-facebook'},
            {'name': 'Twitter', 'url': 'https://twitter.com/', 'icon': 'bi-twitter'},
            {'name': 'Instagram', 'url': 'https://instagram.com/', 'icon': 'bi-instagram'},
            {'name': 'LinkedIn', 'url': 'https://linkedin.com/', 'icon': 'bi-linkedin'},
        ],
    })

    return render(request, 'contacts.html', context)