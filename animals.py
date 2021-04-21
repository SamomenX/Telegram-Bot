import requests
import random
from config import cat_mas, dog_mas

class Animals():
	
	def give_me_a_cat():
		caption = cat_mas[int(random.uniform(0, len(cat_mas)))]
		json = requests.get("https://api.thecatapi.com/v1/images/search").json()
		cat = json[0]['url']
		return [cat, caption]
	
	def give_me_a_dog():
		caption = dog_mas[int(random.uniform(0, len(dog_mas)))]
		json = requests.get("https://dog.ceo/api/breeds/image/random").json()
		dog = json['message']
		return [dog, caption]