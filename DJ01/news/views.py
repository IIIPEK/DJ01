from django.shortcuts import render
from .models import News

# Create your views here.
def news(request):


    # Добавляем специфичные данные
    context={
        'page_title': 'Новости',
        'page_description': 'Последние новости и статьи нашей компании.',
        'posts': News.objects.all(),
    }
    return render(request, 'news/index.html', context)

def post_detail(request, post_id):
    post = News.objects.get(pk=post_id)
    context={
        'page_title': post.title,
        'page_description': post.description,
        'post': post,
    }
    return render(request, 'news/post_detail.html', context)