import requests
import os

BASE_URL = 'http://127.0.0.1:8080'
IMAGE_PATH = 'example_image.jpg'
FILENAME = os.path.basename(IMAGE_PATH)


def upload_image(image_path):
    url = f"{BASE_URL}/upload"
    with open(image_path, 'rb') as img_file:
        files = {'image': img_file}
        response = requests.post(url, files=files)

    if response.status_code == 201:
        image_url = response.json()['image_url']
        print(f"Завантажено: {image_url}")
        return image_url
    else:
        print(f"Помилка: {response.status_code}")
        return None


def get_image_url(filename):
    url = f"{BASE_URL}/image/{filename}"
    headers = {'Content-Type': 'text'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        image_url = response.json()['image_url']
        print(f"Отримано URL: {image_url}")
        return image_url
    else:
        print(f"Помилка: {response.status_code}")
        return None


def delete_image(filename):
    url = f"{BASE_URL}/delete/{filename}"
    response = requests.delete(url)

    if response.status_code == 200:
        print(f"Зображення видалено!")
        return True
    else:
        print(f"Помилка: {response.status_code}")
        return False


if __name__ == "__main__":
    uploaded_url = upload_image(IMAGE_PATH)
    if not uploaded_url:
        exit()

    retrieved_url = get_image_url(FILENAME)
    if not retrieved_url:
        exit()

    delete_image(FILENAME)
