from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Game
from .serializers import GameSerializer
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By



def scrapePrice(title):
    url = f"https://jp.mercari.com/search?keyword={title}%E3%80%80ワンダースワン"
    # response = requests.get(url)
    # html_content = response.text

    browser = webdriver.Chrome()
    # browser = webdriver.Chrome()
    browser.get(url)


    time.sleep(2)

    prices = browser.find_elements(By.CSS_SELECTOR, "[class*='number']")
    prices_num = []

    for price in prices:
            prices_num.append(int(price.text.replace(",", "")))

    average_price = sum(prices_num)/len(prices_num)

    print(average_price)
    return average_price

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all() 
    serializer_class = GameSerializer

    @action(detail=True, methods=['get'])
    def updateprice(self, request, pk=None):
        print("hi")
        game = self.get_object()
        print(game)
        game.loose_price = scrapePrice(game.title)
        custom_response = {"price": "updated"}
        return Response(custom_response, status=200)
        
         
    

