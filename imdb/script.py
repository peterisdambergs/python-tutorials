import requests


def get_html_from_url(url):
    return requests.get(url).text


def create_toc_file(toc_name, categories, year_list, base_url):
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

    urltext = get_html_from_url(base_url)
    # print(urltext)

    create_toc_file("imdb_toc.html", categories, year_list, base_url)


if __name__ == "__main__":
    main()