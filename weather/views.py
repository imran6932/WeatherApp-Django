from django.shortcuts import render
import requests

# Create your views here.

def main(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = f'http://api.weatherstack.com/current?access_key=513acdeac665cad844600eeae5ac5d3c&query={city}'
        response = requests.get(url).json()

        data = {
            "name": response['location']['name'],
            "country": response['location']['country'],
            "region": response['location']['region'],
            "temperature": response['current']['temperature'],
            "weather_icons": response['current']['weather_icons'][0],
            "weather_descriptions": response['current']['weather_descriptions'][0],
            "humidity": response['current']['humidity'],
            "wind_speed": response['current']['wind_speed'],
            "feelslike": response['current']['feelslike'],
        }
        return render(request, 'main.html', {'data':data})
    else:
        return render(request, 'main.html')
            

        


