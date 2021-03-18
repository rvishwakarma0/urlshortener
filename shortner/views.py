from django.shortcuts import get_object_or_404, redirect,render
from django.http import HttpResponse
from .models import URL

def root(request,url_hash):
    url = get_object_or_404(URL,url_hash=url_hash)
    url.clicked()
    return redirect(url.full_url)




def index(request):
    if request.method == 'POST':
         
        url_obj = URL(full_url = request.POST['txtMsg'])
         
        
        try:
            url_obj.save()
            res = str(request.META['HTTP_HOST']) + '/' + url_obj.url_hash       
            return render(request,"urlshortener.html",context={'hash_url':res, 'full_url':url_obj.full_url})
        except Exception as e:
            return render(request,"urlshortener.html",context={'err':e})
    return render(request,"urlshortener.html")    