import requests
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(response)
print(response.text[:12])
response = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    response.raise_for_status()
except Exception as exc:
    print(f'There was a problem: {exc}')

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
response.raise_for_status()
with open('RomeoAndJuliet.txt', 'wb') as play_file:
     for chunk in response.iter_content(100000):
        play_file.write(chunk)