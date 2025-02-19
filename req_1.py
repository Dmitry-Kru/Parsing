import requests

response = requests.get('https://api.github.com/search/repositories', params={'q': 'html'})

print(f'Статус-код ответа: {response.status_code}')
print(response.json())
