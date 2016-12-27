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
        if urls:
            urls = urls.split("\n")
            shorturls = {}
            for index, url in enumerate(urls):
                if url:
                    data = {
                        "longUrl": url
                    }
                    x = requests.post(url=URL, data=json.dumps(data), headers={
                        'Content-Type': 'application/json'
                    })
                    shorturls[str(index)] = x.json()["id"]
                else:
                    shorturls[str(index)] = ""
            return JsonResponse({'status': 'okay', "shorturls": json.dumps(shorturls)})
        else:
            return JsonResponse({'status': 'failed'})
