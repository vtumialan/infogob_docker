from backend.models import Publisher
from backend.serializers import PublisherSerializer
from rest_framework import generics

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bs4 import BeautifulSoup
import requests
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


def scrapeSite(self):
    page = requests.get('https://infogob.jne.gob.pe/Localidad/Peru_procesos-electorales_uHzVUEHmgS0%3dzE', verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    divMapa = soup.find_all('svg', id='Mapa')
    regiones =[]

    for a in divMapa:
        a_tags = a.find_all('g')
        for q in a_tags:
            if 'q' in q.attrs:
                regiones.append({
                    'description' : q['title'],
                    'token' : q['q'],
                    'url_regidor' : '/regidor/?region=' + q['title'].lower() + '&token=' + q['q']
                })

    return JsonResponse(regiones, safe=False)


def scrapeRegion(request):
    url_default = 'https://infogob.jne.gob.pe'
    region = request.GET.get("region")
    token = request.GET.get("token")

    data ={"token":token}
    page = requests.post('https://infogob.jne.gob.pe/Localidad/Peru/' + region.lower() + '_procesos-electorales',params=data, allow_redirects=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    href_region = soup.find_all('a')
    
    href = soup.find_all('a')
    for q in href:
        if 'href' in q.attrs:
            url_region = q['href']

    url_final = url_region.replace("%22", "")
    
    page = requests.post(url_default + url_final)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', id='gridAutoridadesRegionales')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')[0]
    regidor = rows.find_all('td')[1]

    response = {
        'GOBERNADOR REGIONAL' : regidor.find(text=True)
    }

    return JsonResponse(response, safe=False)