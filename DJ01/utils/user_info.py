from django.contrib.auth.models import User

def print_users():
    # Получаем всех пользователей из базы данных
    users = User.objects.all()

    if not users.exists():
        print("В базе данных нет пользователей.")
        return

    print("Список пользователей:")
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}")

# Вызов функции
print_users()
