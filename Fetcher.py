import pymongo
from pprint import pprint
import requests
from requests import get
from bs4 import BeautifulSoup
from contextlib import closing


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

## START OF CODE

## MongoDB

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["European-Movies"]
colection = database["Movie"]

## FETCHER

def fetcher(imdbCode):
	link_release_info = 'https://www.imdb.com/title/' + imdbCode + '/releaseinfo'
	raw_html_info = simple_get(link_release_info)
	release_info = BeautifulSoup(raw_html_info, 'html.parser')
	try:
		original_title = release_info.find('td',text=' (original title)').find_next().get_text()
	except:
		original_title = "TO_BE_CHANGED"

	# English movies don't have this, so sometimes we have to comment the line and make a manual adjustment
	try:
		english_title = release_info.find('td',text='World-wide (English title)').find_next().get_text()
	except:
		try:
			english_title = release_info.find('td',text='World-wide').find_next().get_text()
		except:
			english_title = original_title


	# Front Page
	link = 'https://www.imdb.com/title/' + imdbCode
	raw_html = simple_get(link)
	page = BeautifulSoup(raw_html, 'html.parser')

	# Year
	year = page.find('span', id='titleYear').get_text().replace('(','').replace(')','')

	# Countries, Languages and Genres
	details = page.find('div', id='titleDetails')

	# Country
	countries_list = details.find('h4', text='Country:').find_parent('div').find_all('a')
	country = []
	for country_name in countries_list:
		country.append(country_name.get_text())

	# Languages
	languages_list = details.find('h4', text='Language:').find_parent('div').find_all('a')
	language = []
	for language_name in languages_list:
		language.append(language_name.get_text())

	# Genres
	genres_list = page.find('h4', text='Genres:').find_parent('div').find_all('a')
	genre = []
	for genre_name in genres_list:
		genre.append(genre_name.get_text()[1:])

	# Rating
	rating = float(page.find('div', class_ = 'ratingValue').find('span').get_text())

	# Plot
	plot = page.find('div', class_ = "summary_text").get_text().strip()

	# Image
	img_link = page.find('div', class_ = 'poster').find('img').get("src")

	print(original_title)

	mydict = {"imdbCode": imdbCode ,"original_title": original_title, "english_title": english_title, "plot": plot, "year": year, "country": country, "language": language, "genre": genre, "rating": rating, "image": img_link}
	colection.insert_one(mydict)

final_list = []

# Open file to get the list of movies
with open('input.txt', 'r') as input:
	list_ = input.read().splitlines()

# Filter duplicates
with open('codes.txt', 'r') as codes_read:
	code_list = codes_read.read().splitlines()
	for movie in list_:
		if movie not in code_list:
			final_list.append(movie)
		else:
			print("Duplicate: " + movie)

# Looping through movies
for item in final_list:
	fetcher(item)

# Adding the new codes to the codes list
with open('codes.txt', 'a') as codes_append:
	for movie in final_list:
		codes_append.write("\n" + movie)

# Erase the file after retrieving
with open('input.txt', 'w'):
	pass