from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from main_app import models

# Create your views here.

def main_page(request):
    return render(request, "index.html")


@csrf_exempt
def add_word(request):
    spell = str(request.POST.get('spell'))
    tp = str(request.POST.get('tp'))
    chinese = str(request.POST.get('chinese'))


    try:
        new_obj = models.Dictionaries.objects.create(spell=spell, tp=tp, chinese=chinese)
        return JsonResponse({"state": 1}, safe=False)
    except:
        return JsonResponse({"state": 0}, safe=False)


@csrf_exempt
def delete_word(request):
    spell = str(request.POST.get('spell'))
    word = models.Dictionaries.objects.get(spell=spell)
    if word is not None:
        word.delete()
        state = 1
    else:
        state = 0

    return JsonResponse({"state": state}, safe=False)


@csrf_exempt
def update_words(request):
    old_spell = str(request.POST.get('old_spell'))
    new_spell = str(request.POST.get('new_spell'))
    tp = str(request.POST.get('tp'))
    chinese = str(request.POST.get('chinese'))

    try:
        word = models.Dictionaries.objects.get(spell=old_spell)
        word.delete()

        new_obj = models.Dictionaries.objects.create(spell=new_spell, tp=tp, chinese=chinese)
        return JsonResponse({"state": 1}, safe=False)
    except:
        return JsonResponse({"state": 0}, safe=False)


@csrf_exempt
def search_by_spell(request):
    spell = str(request.GET.get('spell'))
    words_Q = models.Dictionaries.objects.filter(spell__icontains=spell)
    # print(words_Q)
    words = serializers.serialize("json", words_Q, ensure_ascii=False)
    # print(words)

    if len(words) > 2:
        return JsonResponse({"state": 1, "words": words}, charset='utf-8', safe=False)
    else:
        return JsonResponse({"state": 0}, safe=False)
