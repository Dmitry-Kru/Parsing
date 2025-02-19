import requests
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

print(f'Статус-код: {response.status_code}')
print('Содержание ответа:')
print(response.text)
