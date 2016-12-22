from django.shortcuts import render
from django.views import View
import requests

URL = 'https://www.googleapis.com/urlshortener/v1/url?key='
API_KEY = 'AIzaSyAlC-t7RRoIqeVWA0GDoDjRoQ8gFMja-eA'


class Index(View):
    def get(self, request):
        return render(request, "homepage.html", {})

    def post(self, request):
        pass
