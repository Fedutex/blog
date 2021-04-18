from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'fisica alienigena',
        'title': 'Los verdaderos reptiles de Villa General Belgrano',
        'content': 'contenido de la primera publicacion',
        'data_posted': 'abril 13, 2021'
    },
    {
        'author': 'Carlos Django Jure',
        'title': 'Los verdaderos secretos de la tecnologia Moscoviana',
        'content': 'contenido de la segunda publicacion',
        'data_posted': 'marzo 13, 1800'
    }
]



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'blog/home.html', context )

def about(request):
    return render(request, 'blog/about.html',{'title': 'about'} )
