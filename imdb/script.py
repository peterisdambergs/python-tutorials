import requests

from bs4 import BeautifulSoup


def get_html_from_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    return requests.get(url, headers=headers).text


def create_toc_file(toc_name, base_url, categories, year_list):
    with open(toc_name, "w", encoding="utf-8") as f:
        f.write("<h1>Table of Contents</h1>\n")
        for category in categories:
            for year in year_list:
                category_link, movie_links = get_category_and_movie_links(base_url, category, year)
                f.write(f"<h1><a href={category_link}>{category.capitalize()}: {year[0]} - {year[1]}</a></h1>\n")
                for movie_link in movie_links:
                    movie = get_formatted_movie(movie_link)
                    f.write(f"<h3><a href={movie_link}>{movie.get('title')}</a></h3>\n")
                    f.write(f"<img src='{movie.get('img_link')} alt=''>")
                    f.write(f"<p><i>{movie.get('rating')}</i></p>")
                    f.write(f"<p>{movie.get('description')}</p>")
                    f.write("<hr>")


def get_movie_link_from_movie_element(base_url, movie):
    return f"{base_url}{movie.find('a', attrs={'class': 'ipc-title-link-wrapper'}).get('href')}"


def get_category_and_movie_links(base_url, category, year):
    category_link = f"{base_url}/chart/moviemeter/?ref_=nv_mv_mpm&genres={category}&year={year[0]}%2C{year[1]}"
    html = get_html_from_url(category_link)
    soup = BeautifulSoup(html, "lxml")
    movies = soup.find_all('li', attrs={'class': 'ipc-metadata-list-summary-item'})

    return category_link, [get_movie_link_from_movie_element(base_url, movie) for movie in movies][:3]


def get_formatted_movie(movie_link):
    soup = BeautifulSoup(get_html_from_url(movie_link), "lxml")

    movie = {
        'link': movie_link,
        'title': soup.find('h1', attrs={'data-testid': 'hero__pageTitle'}).text,
        'rating': soup.find('div', attrs={'data-testid': 'hero-rating-bar__aggregate-rating__score'}).text,
        'description': soup.find('span', attrs={'data-testid': 'plot-xl'}).text,
        'img_link': soup.find('div', attrs={'data-testid': 'hero-media__poster'}).find('img').get('src')
    }

    return movie



def main():
    base_url = "https://www.imdb.com"
    categories = ["drama", "thriller", "action"]
    year_list = [(2004, 2019), (2020, 2024)]

    create_toc_file("imdb_toc.html", base_url, categories, year_list)


if __name__ == "__main__":
    main()