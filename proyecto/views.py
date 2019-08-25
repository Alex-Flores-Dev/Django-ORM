"""para los views"""
from django.http import HttpResponse
from datetime import datetime


def hello_word(request):
    """return algo"""

    return HttpResponse('Hello,world! is {now}'.format(now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def hi(request):
    numbers=[int(i) for i in request.GET['numbers'].split(',')]
    sorted_num=sorted(numbers)
    return HttpResponse(str(sorted_num),content_type='application/json')

def say_hi(request,name,age):
    if age<12:
        message='Perdon {}, tu tienes {} eres menor de edad'.format(name,age)
    else:
        message=' Hola {}  tienes {} anios bienvenido'.format(name,age)
    return HttpResponse(message)
