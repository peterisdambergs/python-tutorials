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
                link = f"{base_url}&genres={category}&year={year[0]}%2C{year[1]}"
                f.write(f"<h3><a href={link}>{category.capitalize()}: {year[0]} - {year[1]}</a></h3>\n")


def main():
    base_url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    categories = ["drama", "thriller", "action"]
    year_list = [(2004, 2019), (2020, 2024)]

    html = get_html_from_url(base_url)
    soup = BeautifulSoup(html, "lxml")
    movies = soup.find_all('li', attrs={'class': 'ipc-metadata-list-summary-item'})

    for movie in movies:
        print(movie.get_text())
    create_toc_file("imdb_toc.html", base_url, categories, year_list)


if __name__ == "__main__":
    main()