from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def dis_topic(request):
    LTO=Topic.objects.all()
    LTO=Topic.objects.filter(topic_name='volley ball')
    LTO=Topic.objects.all()[2::]
    LTO=Topic.objects.all()[::-1]
    d={'LTO':LTO}
    return render(request,'dis_topic.html',d)
def dis_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.all()[:4:-1]
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.all().order_by('-name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    LWO=Webpage.objects.filter(name__startswith='V')
    LWO=Webpage.objects.filter(name__endswith='A')
    LWO=Webpage.objects.filter(name__contains='a')
    LWO=Webpage.objects.filter(name__in=['virat','dhoni'])
    LWO=Webpage.objects.filter(name__regex='i\w+')
    LWO=Webpage.objects.filter((Q(name='Virat') | Q(url__startswith='https')))
    LWO=Webpage.objects.filter((Q(name='Kirillova') & Q(url__startswith='https')))
    d={'LWO':LWO}
    return render(request,'dis_webpages.html',d)
def dis_access(request):
    LAO=AccessRecord.objects.all()
    LAO=AccessRecord.objects.filter(date='1995-12-12')
    LAO=AccessRecord.objects.filter(date__gt='1995-12-12')
    LAO=AccessRecord.objects.filter(date__lt='1995-12-12')
    LAO=AccessRecord.objects.filter(date__gte='1995-12-12')
    LAO=AccessRecord.objects.filter(date__lte='1995-12-12')
    LAO=AccessRecord.objects.filter(date__year__gt='1999')
    LAO=AccessRecord.objects.filter(date__month__lt='12')
    LAO=AccessRecord.objects.exclude(date__day__gte='22')

    d={'LAO':LAO}
    return render(request,'dis_access.html',d)

