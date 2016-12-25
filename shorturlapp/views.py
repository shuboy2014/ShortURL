from django.shortcuts import render
from django.views import View
import requests
import json

URL = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAlC-t7RRoIqeVWA0GDoDjRoQ8gFMja-eA'


class Index(View):
    def get(self, request):
        return render(request, "homepage.html", {})

    def post(self, request):
        data = {
            "longUrl": request.POST["longurl"]
        }

        x = requests.post(url=URL, data=json.dumps(data), headers={
            'Content-Type': 'application/json'
        })
        print x.json()
        return render(request, "homepage.html", {})
