from django.shortcuts import render
from django.http import JsonResponse

def oi(request):
    return JsonResponse({'message': 'Teste de  planner!'})

