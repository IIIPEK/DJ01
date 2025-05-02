import json
from django.core.management.base import BaseCommand
from news.models import News
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Load posts from a JSON file into the database'

    def handle(self, file_path = '../utils/posts.json',*args, **kwargs):
        # Путь к JSON-файлу
        print(os.listdir())
        print(file_path)

        try:
            # Открываем JSON-файл
            with open(file_path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)

            for post_data in posts_data:
                # Получаем автора по его ID
                author_id = post_data['author_id']
                try:
                    author = User.objects.get(id=author_id)
                except User.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"User with ID {author_id} does not exist. Skipping post."))
                    continue

                # Создаем пост
                News.objects.create(
                    title=post_data['title'],
                    description=post_data['description'],
                    text=post_data['text'],
                    author=author
                )

            self.stdout.write(self.style.SUCCESS('Posts successfully loaded into the database.'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File {file_path} not found."))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR("Invalid JSON format in the file."))
