import requests

BASE_URL = "http://127.0.0.1:8080"
filename = "my_image.jpg"

# 1. POST
with open(filename, 'rb') as f:
    files = {'image': (filename, f)}
    response_post = requests.post(f"{BASE_URL}/upload", files=files)

if response_post.status_code == 201:
    print("Зображення вдало завантажено.")

    uploaded_url = response_post.json().get('image_url')
    print(f"URL зображення: {uploaded_url}")

    uploaded_filename = uploaded_url.split('/')[-1]

# 2. GET
    headers = {'Content-Type': 'text/plain'}
    response_get = requests.get(f"{BASE_URL}/image/{uploaded_filename}", headers=headers)
    print(f"GET: {response_get.json()}")

# 3. DELETE
    response_delete = requests.delete(f"{BASE_URL}/delete/{uploaded_filename}")
    if response_delete.status_code == 200:
        print("Зображення вдало видалено.")
