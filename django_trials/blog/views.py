from django.shortcuts import render

posts = [
    {
        'author': 'Jis Mathew',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 1 2019'
    },
    {
        'author': 'Jess Sunny',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 3 2019'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
