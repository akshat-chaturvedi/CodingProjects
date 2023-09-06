import os
import requests
import dotenv

dotenv.load_dotenv('.env')

def linkShortener(fullLink, linkName):
    apiKey = os.getenv('CUTTLY_API')
    baseURL = "https://cutt.ly/api/api.php"

    payload = {'key': apiKey, 'short': fullLink, 'name': linkName}
    request = requests.get(baseURL, params=payload)
    data = request.json()

    try:
        title = data['url']['title']
        shortLink = data['url']['shortLink']
        print(f"Title: {title}\nShort URL: {shortLink}")
    except:
        status = data['url']['status']
        print(f"Error status: {status}")


if __name__ == '__main__':
    link = input("Enter a link to be shortened:")
    name = input("Name for shortened link:")

    linkShortener(link, name)
