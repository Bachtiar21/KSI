from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


def index(request):

    db = Post.objects.all()
    context = {
        'title': 'blog1',
        'heading': 'Django',
        'subheading': 'postingan',
        'post': db,
    }
    return render(request, 'blog/index.html', context)

# def index(request):
#     context = {
#         'Judul': 'blog1',
#         'h1': 'Django',
#         'menu': [['blog/', 'Home'], ['blog/recent'], ['/post', 'Post']]
#     }
#     return render(request, 'blog/index.html', context)


def recent(request):
    # context = {
    #     'Judul' : 'Identitas Diri',
    #     'h1' : 'Bachtiar Ramadhan',
    #     'h2' : '21 Desember 2000',
    #     'h3' : 'Pekanbaru, Riau'
    # }
    # return render(request, 'blog/index.html', context)

    return HttpResponse("RECENT BLOG")
