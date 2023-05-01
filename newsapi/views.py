from django.shortcuts import render
import requests
API_KEY = '24b6b1d2961e4a248a006697cba68f91'

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    context = {
        'articles': articles
    }
    return render(request , 'newsapi/home.html', context)