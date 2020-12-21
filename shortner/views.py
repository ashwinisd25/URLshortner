from django.shortcuts import render, redirect
from django.contrib import messages
from .models import shorturl
import pyshorteners
import requests 
import random
import string
from rest_framework import viewsets
from .serializers import ShorturlSerializer

class ShorturlView(viewsets.ModelViewSet):
    queryset = shorturl.objects.all()
    serializer_class = ShorturlSerializer

def generator(link):
    x=''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    return x

def ckeckURL(link):
    try:
        response=requests.get(link)
    except:
        messages.error(request, "please enter a valid page URL")
    if response.status_code == 404:
        messages.error(request, "please enter a valid page URL")
        result = 0
    else:
        result = response.url.split('//')[1]
    return(result)

# Create your views here.
def home(request):
    allURLs= shorturl.objects.all()
    if request.method == "POST":
        if request.POST['original']:
            original = request.POST['original']
            result = ckeckURL(original)
            if result:
                check = shorturl.objects.filter(result=result)
                if not check:
                    gen_url=generator(original)
                    check_again = shorturl.objects.filter(short_url=gen_url)
                    if not check_again:
                        newurl = shorturl(
                        original_url=original,
                        short_url=gen_url,
                        result=result
                        )
                        newurl.save()
                        messages.info(request, "URL Shortened")
                        return redirect('home')
                    else:
                        pass
                else:
                    messages.error(request, "This url alredy Shorened")
                    return redirect('home')
            else:
                messages.error(request, """The webpage not found for entered URL
                                        Please Check the URL """)
                return redirect('home')
        else:
            messages.error(request, "Empty Fields")
            return redirect('home')
    else:
        return render(request,'shortner/home.html',{'allURLs': allURLs})

def index(request, query=None):
    if not query or query is None:
        return render(request, 'home.html')
    else:
        try:
            check = shorturl.objects.get(short_url=query)
            url_to_redirect = check.original_url
            return redirect(url_to_redirect)
        except shorturl.DoesNotExist:
            return render(request, 'shortner/home.html', {'error': "error"})

