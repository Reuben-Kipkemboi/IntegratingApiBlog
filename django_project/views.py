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
            
  # Fetch random GIF
    # api_key = 'otZpJ4dwyhheSAr0QaM76oYuMOjCGZJq'
    api_key = '4ounCQ02Y4DWHYHQQ69ZglThi8c7FtpemrBZ1BC1Vm1E8lA8heRc51xh'
    
    endpoint = 'https://api.pexels.com/videos/search'
    headers = {
        'Authorization': api_key
    }
    params = {
        'query': 'supercars',
        'per_page': 9  # Number of car-related videos to fetch
    }
    response = requests.get(endpoint, headers=headers, params=params)
    
    # Handle the response
    if response.status_code == 200:
        video_data = response.json()['videos']
        video_urls = [video['video_files'][0]['link'] for video in video_data]
    else:
        video_urls = []  

    
    gif_urls=[]
    for _ in range(10):
        gif_response = requests.get(f'https://api.giphy.com/v1/gifs/random?api_key={api_key}')
        if gif_response.status_code == 200:
            gif_url = gif_response.json()['data']['images']['downsized']['url']
            gif_urls.append(gif_url)
        else:
            # this is like a fallback giphy
            gif_urls.append("https://media.giphy.com/media/yFQ0ywscgobJK/giphy.gif")  
    

  
  return render(request, 'templates/index.html', {'quotes':quotes, 'video_urls': video_urls})