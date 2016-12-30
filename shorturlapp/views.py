from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import requests
import json
import os

URL = 'https://www.googleapis.com/urlshortener/v1/url?key='
key = os.environ.get('key', '')


class Index(View):
    def get(self, request):
        return render(request, "homepage.html", {})

    def post(self, request):
        urls = request.POST.get("longUrls", "")

        # if key is not in environment variable
        if key is None:
            print("Your API is not in Environment Variable!")
            return JsonResponse({"error": "Api key is not exist!"})

        if urls:
            urls = urls.split("\n")
            shorturls = {}
            for index, url in enumerate(urls):
                # is url is empty or not
                if url:
                    data = {
                        "longUrl": url
                    }
                    x = requests.post(url=URL + key, data=json.dumps(data), headers={
                        'Content-Type': 'application/json'
                    })
                    response = x.json()
                    # if url is shortened or not
                    if response.get("id", ""):
                        shorturls[str(index)] = response["id"]
                    else:
                        shorturls[str(index)] = "Something went wrong with url!"
                else:
                    shorturls[str(index)] = ""
            return JsonResponse({'status': 'okay', "shorturls": json.dumps(shorturls)})
        else:
            return JsonResponse({'status': 'failed'})
