from django.shortcuts import render
from datetime import datetime

def home_page(request):
    context = {
        'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', context)