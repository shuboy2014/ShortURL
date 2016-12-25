from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import requests
import json

URL = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAlC-t7RRoIqeVWA0GDoDjRoQ8gFMja-eA'


class Index(View):
    def get(self, request):
        return render(request, "homepage.html", {})

    def post(self, request):
        urls = request.POST.get("longUrls", "")
        urls = urls.split("\n")
        if urls:
            shorturls = {}
            for index, url in enumerate(urls):
                data = {
                    "longUrl": url
                }
                x = requests.post(url=URL, data=json.dumps(data), headers={
                    'Content-Type': 'application/json'
                })
                shorturls[str(index)] = x.json()["id"]
            return JsonResponse({'status': 'okay', "shorturls": json.dumps(shorturls)})
        else:
            return JsonResponse({'status': 'failed'})
