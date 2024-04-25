from django.shortcuts import render
import requests

def home(request):
  # to get the random quotes
  quotes = []
  while len(quotes) < 6:
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote_content = response.json()['content']
        if quote_content not in quotes:
            quotes.append(quote_content)
        else:
            quotes.append("Failed to fetch quote")
            
  # Fetch cars from the pexels api in terms of videos--
    api_key = '4ounCQ02Y4DWHYHQQ69ZglThi8c7FtpemrBZ1BC1Vm1E8lA8heRc51xh'
    
    endpoint = 'https://api.pexels.com/videos/search'
    headers = {
        'Authorization': api_key
    }
    params = {
        'query': 'supercars',
        'per_page': 12  # Number of car-related videos to fetch
    }
    response = requests.get(endpoint, headers=headers, params=params)
    
    # Handle the response
    video_data = []
    if response.status_code == 200:
        video_data = response.json()['videos']
        for video in video_data:
            video['video_url'] = video['video_files'][0]['link']
            video['user_name'] = video['user']['name']
            video['user_url'] = video['user']['url']
        
    else:
        video_data = []  


  
  return render(request, 'templates/index.html', {'quotes':quotes, 'video_data': video_data})