from django.shortcuts import render
import requests
from .forms import CityForm
from .utils import clothes, speedInfo, humidityInfo

def index(request):
  

    api_url = "http://api.openweathermap.org/data/2.5/weather"

    city = "London"



    form = CityForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            city = form.cleaned_data.get("city")

    params = {
        'q': city,
        'appid':'11c0d3dc6093f7442898ee49d2430d20',
        'units': 'metric'
    } 
    context = {
        'form':form,
        'errorInput':False
    }   

    res = requests.get(api_url, params=params).json()
    if(res["cod"] == 200):

        info = {
                'city':city,
                'temp':res["main"]["temp"],
                'icon':res["weather"][0]["icon"],
                'pressure':res["main"]["pressure"],
                'humidity':res["main"]["humidity"],
                'windSpeed':res["wind"]["speed"],
                'clothes':clothes(res["main"]["temp"]),
                'speedInfo':speedInfo(res["wind"]["speed"]),
                'humidityInfo':humidityInfo(res["main"]["humidity"])
        }
        context['info'] = info

   

    else:
        context["errorInput"] = True



    
    return render(request, 'weather/show.html', context)
