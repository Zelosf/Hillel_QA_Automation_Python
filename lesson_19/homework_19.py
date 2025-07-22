import requests
import os


url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
	'sol': 1000,
	'camera': 'fhaz',
	'api_key': 'DEMO_KEY'
}

os.makedirs("images", exist_ok=True)
response = requests.get(url, params=params)


if response.status_code == 200:
	data = response.json()

	photos = data.get('photos', [])

	if not photos:
		print("Фото не знайдено.")
	else:
		for idx, photo in enumerate(photos, start=1):
			img_url = photo['img_src']
			img_data = requests.get(img_url).content
			filename = f"images/mars_photo{idx}.jpg"
			with open(filename, 'wb') as file:
				file.write(img_data)

			print(f"Фото збережено: {filename}")
else:
	print(f"Помилка: {response.status_code}")
