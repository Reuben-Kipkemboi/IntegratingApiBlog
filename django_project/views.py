from django.shortcuts import render
import requests

def home(request):
  quotes = []
  while len(quotes) < 6:
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote_content = response.json()['content']
        if quote_content not in quotes:
            quotes.append(quote_content)
        else:
            quotes.append("Failed to fetch quote")
  
  return render(request, 'templates/index.html', {'quotes':quotes})