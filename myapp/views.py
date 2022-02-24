from cgitb import enable
from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp import models
import math

def index(request):

    pagesize = 6
    newsall = models.NewsUnit.objects.all().order_by('-id')
    datasize = len(newsall)
    newsunitsall = models.NewsUnit.objects.filter(enabled=False).order_by('-id')[:pagesize]
    newsunitsannouncement = models.NewsUnit.objects.filter(enabled=False,classification="公告").order_by('-id')[:pagesize]
    newsunitsnew = models.NewsUnit.objects.filter(enabled=False,classification="新品").order_by('-id')[:pagesize]
    newsunitsactivity = models.NewsUnit.objects.filter(enabled=False,classification="活動").order_by('-id')[:pagesize]

    return render(request,"index.html",locals())

def information(request,pageinfo=None,pageid=None):
    pagesize = 8
    int(pageid)
    page=pageid
    if pageinfo == '公告':
        start = (page-1)*pagesize
        newsunitsall = models.NewsUnit.objects.filter(enabled=False,classification="公告").order_by('-id')
        datasize = len(newsunitsall)
        totpage = math.ceil(datasize/pagesize)
        if start<datasize:
            newsunits = models.NewsUnit.objects.filter(enabled=False,classification="公告").order_by('-id')[start:(start+pagesize)]
    elif pageinfo == '新品':
        start = (page-1)*pagesize
        newsunitsall = models.NewsUnit.objects.filter(enabled=False,classification="新品").order_by('-id')
        datasize = len(newsunitsall)
        totpage = math.ceil(datasize/pagesize)
        if start<datasize:
            newsunits = models.NewsUnit.objects.filter(enabled=False,classification="新品").order_by('-id')[start:(start+pagesize)]
    elif pageinfo == '活動':
        start = (page-1)*pagesize
        newsunitsall = models.NewsUnit.objects.filter(enabled=False,classification="活動").order_by('-id')
        datasize = len(newsunitsall)
        totpage = math.ceil(datasize/pagesize)
        if start<datasize:
            newsunits = models.NewsUnit.objects.filter(enabled=False,classification="活動").order_by('-id')[start:(start+pagesize)]
    else:   
        start = (page-1)*pagesize
        newsunitsall = models.NewsUnit.objects.filter(enabled=False).order_by('-id')
        datasize = len(newsunitsall)
        totpage = math.ceil(datasize/pagesize)
        if start<datasize:
            newsunits = models.NewsUnit.objects.filter(enabled=False).order_by('-id')[start:(start+pagesize)]       

    currentpage = pageid
    return render(request,"information.html",locals())

def infodetail(request,id=None):
    unit = models.NewsUnit.objects.get(id=id)
    classification = unit.classification
    title = unit.title
    time = unit.time
    name = unit.name
    message = unit.message
    unit.press +=1
    unit.save()

    return render(request,"infodetail.html",locals())

def menu(request):
    news = models.Product.objects.filter(pNew=True).order_by('-id')
    quiches = models.Product.objects.filter(pClass="蛋餅").order_by('id')
    toasts = models.Product.objects.filter(pClass="夾烤吐司").order_by('id')
    hamburgers = models.Product.objects.filter(pClass="漢堡").order_by('id')
    drinks = models.Product.objects.filter(pClass="飲品").order_by('id')
    frieds = models.Product.objects.filter(pClass="炸物").order_by('id')
    chineses = models.Product.objects.filter(pClass="中式小點").order_by('id')
    desserts = models.Product.objects.filter(pClass="甜點").order_by('id')
    easys = models.Product.objects.filter(pClass="簡餐").order_by('id')
    return render(request,"menu.html",locals())

def menudetial(request,item=None):
    if item == '新品':
        units = models.Product.objects.filter(pNew=True).order_by('-id')
    elif item == '蛋餅':
        units = models.Product.objects.filter(pClass="蛋餅").order_by('id')
    elif item == '夾烤吐司':
        units = models.Product.objects.filter(pClass="夾烤吐司").order_by('id')
    elif item == '漢堡':
        units = models.Product.objects.filter(pClass="漢堡").order_by('id')
    elif item == '飲品':
        units = models.Product.objects.filter(pClass="飲品").order_by('id')
    elif item == '炸物':
        units = models.Product.objects.filter(pClass="炸物").order_by('id')
    elif item == '中式小點':
        units = models.Product.objects.filter(pClass="中式小點").order_by('id')
    elif item == '甜點':
        units = models.Product.objects.filter(pClass="甜點").order_by('id')
    elif item == '簡餐':
        units = models.Product.objects.filter(pClass="簡餐").order_by('id')
        
    return render(request,"menudetial.html",locals())

def aboutous(request):
    return render(request,"aboutous.html",locals())