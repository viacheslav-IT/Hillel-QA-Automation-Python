import requests

url = 'https://images-api.nasa.gov'
search_url = f"{url}/search"
asset_url= f"{url}/asset/"

search_params = {
  "q": "Curiosity rover Mars",
  "media_type": "image",
  "page_size": 20
}

# Виконати пошук зображень, пов’язаних з ровером Curiosity на Марсі
response = requests.get(search_url, params=search_params).json()
print('Отримані дані:', response)
print('-' * 100)

# З JSON відповіді витягнути nasa_id для знайдених елементів
list_nasa_id = []
for nasa_id in (response['collection']['items']):
    list_nasa_id.append(nasa_id['data'][0]['nasa_id'])
print(f'Список nasa_id для знайдених елементів:')
for i in list_nasa_id:
    print(f'- {i}')
print('-' * 100)

# Для кожного nasa_id зробити додатковий запит до endpoint-а /asset/{nasa_id}, щоб отримати список URL-ів файлів
print('Cписок URL-ів файлів для кожного nasa_id:')
for i in response['collection']['items']:
    collection_json_url = i['href']
    print(collection_json_url)
print('-' * 100)

# Обрати з цього списку посилання на JPG-зображення (наприклад, перший .jpg або “найкращий” варіант, якщо їх кілька).
print('Посилання на JPG-зображення:')
for nasa_id in list_nasa_id:
    response_nasa_id_url = requests.get(f'{asset_url}{nasa_id}')
    print(response_nasa_id_url.json()['collection']['items'][0]['href'])
print('-' * 100)

# Скачати 2 зображення і зберегти локально
urls_to_download = []
for nasa_id in list_nasa_id[:2]:
    response_nasa_id_url = requests.get(f'{asset_url}{nasa_id}')

    img_url = response_nasa_id_url.json()['collection']['items'][0]['href']
    urls_to_download.append(img_url)

filenames = ["mars_photo1.jpg", "mars_photo2.jpg"]

for i in range(2):
    img_response = requests.get(urls_to_download[i])
    with open(filenames[i], 'wb') as file:
        file.write(img_response.content)
    print(f"Файл {filenames[i]} вдало збережений.")