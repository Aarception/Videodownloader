import urllib.parse
import requests
from bs4 import BeautifulSoup

def decode_url():
    while True:
        input_url = input("Facebook URL: \n\t")
        if input_url.lower() == '':
            break
        base_url = 'https://mbasic.facebook.com/plugins/video.php?href='
        encoded_url = urllib.parse.quote_plus(input_url)
        full_url = base_url + encoded_url

        # Decode the URL
        decoded_url = urllib.parse.unquote(full_url)

        # Get the source code
        response = requests.get(decoded_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the video link
        video_linked = ''
        for a in soup.find_all('a', href=True):
            if a['href'].startswith('/video_redirect/?src='):
                video_linked = a['href']
                break

        # Decode the URL
        video_link = urllib.parse.unquote(video_linked)

        # Find the start of the string to decode
        src_start = video_link.find('?src=')
        if src_start == -1:
            print("Can't Locate.")
            continue
        src_start += 5  # Skip past "?src="
        decode_url = video_link[src_start:]

        # Decode the URL
        print("Download Link:\n\t", decode_url)

        # Extract the part of the response
        id_start = video_link.find('&id=')
        if id_start == -1:
            print("Can't Locate.")
            continue
        id_start += 4  # Skip past "&id="
        id_end = video_link.find('&', id_start)
        video_id = video_link[id_start:id_end]

        # Construct a new URL
        new_url = input_url.split('/')[2] + '/' + input_url.split('/')[3] + '/videos/' + video_id
        print("New URL:\n\t",'https://'+ new_url)

decode_url()
