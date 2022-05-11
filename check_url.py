from urllib import response
import requests
# urls=['www.osogoodwingbar.com','www.nonabistro.com','myorlandofoodtruck.com','Www.fatboipotatoes.com']

# response=requests.get('https://www.osogoodwingbar.com')

# print(response.status_code)

# import json
# import urllib.request

# response = urllib.request.urlopen('http://konafoodtruckluaus.com')
# text = response.read()
# print(json.loads(text.decode('utf-8')))
status=[]
urls=['www.osogoodwingbar.com',
'www.nonabistro.com',
'myorlandofoodtruck.com',
'Www.fatboipotatoes.com ',
'Conchqueen.com',
'http://www.onefatfrog.com',
'www.tastytakeover.com',
'www.gooddogtreattruck.com',
'Bignatesbbqco.com',
'Sweetandsaltygrindz.com',
'www.brazilianfunfoods.com',
'wanderinggoatfoodtruck.com',
'Www.chiavestx.com',
'http://konafoodtruckluaus.com',
'www.Lingosfishloavesgrill.com',
'www.reosneworleanskitchen.com']

for url in urls:
    if not url.startswith('http://'):
        url='http://'+url.lower()
    try:
        response=requests.get(url)
        if response.status_code ==200:
            status.append([url,'working'])
        else:
            status.append([url,'bad website'])
        print(url,response.status_code)
    except:
        print("Exception in ",url)
        status.append([url,'bad website'])


for stat in status:
    print(stat)