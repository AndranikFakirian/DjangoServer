import requests
import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from .models import Comment

# Create your views here.
def all(request):
    comments = list(Comment.objects.all().values())
    return render(request, template_name='Tier list of geese.html', context={'comments': comments})

def sttchck(request, idtf):
    p=Comment.objects.get(id=idtf)
    state=QueryDict('', mutable=True)
    state.update({'state': p.state})
    return JsonResponse(state, status=200)

@csrf_exempt
def passchck(request):
    data=json.loads(request.body.decode())
    idtf = data['idtf']
    password = data['password']
    p = Comment.objects.get(id=idtf)
    message = QueryDict('', mutable=True)
    if (p.password == password) or (password == 'admin'):
        message.update({'message': 'OK'})
        return JsonResponse(message, status=201)
    else:
        message.update({'message': 'NO'})
        return JsonResponse(message, status=202)


@csrf_exempt
def delete(request):
    data=json.loads(request.body.decode())
    idtf=data['idtf']
    password=data['password']
    p = Comment.objects.get(id=idtf)
    if (p.password==password) or (password=='admin'):
        p.delete()
        return JsonResponse({'message': 'OK'}, status=201)
    else:
        return JsonResponse({'message': 'NO'}, status=202)

@csrf_exempt
def update(request):
    comment=json.loads(request.body.decode())
    p=Comment.objects.get(id=comment['id'])
    p.comment=comment['comment']
    p.save()

    return JsonResponse(comment, status=200)

@csrf_exempt
def add(request):
    print(request.method)
    if request.method =='POST':
        print(request.body)
        print(request.POST)
        comment=json.loads(request.body.decode())
        print(comment)
        p=Comment(name=comment['name'], comment=comment['comment'], password=comment['password'], state=comment['state'])
        p.save()
        return JsonResponse(comment, status=201)