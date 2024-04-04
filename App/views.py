
from django.shortcuts import render
from .models import TogriSoz, NotogriSoz

def index(request):
    search = request.GET.get("search", None)
    context = {}

    if search is not None:
        togrisozlar = TogriSoz.objects.filter(soz=search.lower())
        if togrisozlar:
            togriSoz = togrisozlar.first()
            notogriSozlar = NotogriSoz.objects.filter(togri_soz=togriSoz)
            context = {
                "togriSoz": togriSoz,
                "notogriSozlar": notogriSozlar
            }
        else:
            context = {
                'error_message': 'Mavjud emas!'
            }
    return render(request, 'html.html', context)