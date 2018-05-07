from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import BookInfo,HeroInfo

# Create your views here.
def index(request):
    # temp = loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    bookList = BookInfo.objects.all()
    cont = {'name':'朝哥','age':18}
    return  render(request,'booktest/index.html',{'list':bookList,'cont':cont})

def show(request,id):
    book = BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    content = {'list':herolist}
    return render(request,'booktest/show.html',content)