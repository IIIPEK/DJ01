"""
Shared context processors and utilities for DJ01 project.
This module contains functions that can be used across multiple apps
to maintain consistency in templates and views.
"""

import datetime

# Shared site data
SITE_INFO = {
    'site_name': 'Проект DJ03',
    'current_year': datetime.datetime.now().year,
}

# Base menu structure
DEFAULT_MENU = [
    {'title': 'Главная', 'url': '/', 'active': False},
    {'title': 'О нас', 'url': '/about/', 'active': False},
    {'title': 'Услуги', 'url': '/services/', 'active': False},
    {'title': 'Блог', 'url': '/blog/', 'active': False},
    {'title': 'Новости', 'url': '/news/', 'active': False},
    {'title': 'Контакты', 'url': '/contacts/', 'active': False},
]

# Footer data
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


def get_base_context(request):
    """
    Creates a base context with common data for all pages.
    Sets the active menu item.

    Args:
        request (request): Request object

    Returns:
        dict: Context dictionary with common data
    """
    # Copy menu items to avoid modifying the original
    menu_items = DEFAULT_MENU.copy()

    # Set active menu item
    for item in menu_items:
        item['active'] = ( request.path.startswith(item['url']))


    # Create base context
    context = {
        **SITE_INFO,
        'menu_items': menu_items,
        'footer': FOOTER_INFO,
    }

    return context
