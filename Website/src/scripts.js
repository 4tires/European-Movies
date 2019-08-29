const data = [
{
	"code": "tt6576556",
	"original_title": "Das schweigende Klassenzimmer",
	"english_title": "Silent Revolution",
	"year": "2018",
	"img_link": "https://m.media-amazon.com/images/M/MV5BNzEwZDcwNGUtOGVkYS00M2UzLWE2ZTctNDlhM2M0MWI5NzQ5XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg"
},
{
	"code": "tt3841424",
	"original_title": "Under sandet",
	"english_title": "Under Sand",
	"year": "2015",
	"img_link": "https://m.media-amazon.com/images/M/MV5BMjA0MzQzNjM1Ml5BMl5BanBnXkFtZTgwNjM5MjU5NjE@._V1_UX182_CR0,0,182,268_AL_.jpg"
},
{
	"code": "tt3026488",
	"original_title": "Alone in Berlin",
	"english_title": "Alone in Berlin",
	"year": "2016",
	"img_link": "https://m.media-amazon.com/images/M/MV5BMjEyZmQxOGYtYTk3MS00Njg3LWEwOWItYjFhYzVkNDhkMzYxXkEyXkFqcGdeQXVyMzA3Njg4MzY@._V1_UX182_CR0,0,182,268_AL_.jpg"
},
{
	"code": "tt3127698",
	"original_title": "Freistatt",
	"english_title": "Sanctuary",
	"year": "2015",
	"img_link": "https://m.media-amazon.com/images/M/MV5BYWM4MTEzYTktNmRkOC00NTdhLWJhZjgtNGFlMzdmNjNjOGU3XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY268_CR4,0,182,268_AL_.jpg"
},
{
	"code": "tt2404311",
	"original_title": "Malavita",
	"english_title": "The Family",
	"year": "2013",
	"img_link": "https://m.media-amazon.com/images/M/MV5BMjE2MzI0MzkyNV5BMl5BanBnXkFtZTcwMjQ2MDM2OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg"
},
{
	"code": "tt2800240",
	"original_title": "Qu'est-ce qu'on a fait au Bon Dieu?",
	"english_title": "Serial (Bad) Weddings",
	"year": "2014",
	"img_link": "https://m.media-amazon.com/images/M/MV5BMjI3MDI3MTA0OV5BMl5BanBnXkFtZTgwOTUwNTYxMjE@._V1_UY268_CR7,0,182,268_AL_.jpg"
}
];

const row = document.querySelector(".row");

function fetchMovie ({code, original_title, english_title, year, img_link}) {
	// Create div for each movie
	const div = document.createElement("div");
	div.setAttribute('class', 'item');
	row.append(div);

	// Posting the information of each movie
	const original_title_element = document.createElement("h3");
	original_title_element.setAttribute('class', 'original_title');
	original_title_element.innerHTML = original_title;
	div.append(original_title_element);

	const year_element = document.createElement("h3");
	year_element.setAttribute('class', 'year');
	year_element.innerHTML = " (" + year + ")";
	div.append(year_element);

	const english_title_element = document.createElement("h4");
	english_title_element.setAttribute('class', 'english_title');
	english_title_element.innerHTML = english_title;
	div.append(english_title_element);

	const poster = document.createElement("a");
	poster.setAttribute('href', "https://www.imdb.com/title/" + code + "/");
	div.append(poster);

	const image_element = document.createElement("img");
	image_element.setAttribute('src', img_link);
	poster.append(image_element);
}

data.forEach((movie) => {
	fetchMovie(movie);
})