import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})

if response.ok:
    print("Полученные записи:")
    for post in response.json():
        print(post)
else:
    print(f"Произошла ошибка: {response.status_code}")