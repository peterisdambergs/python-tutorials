import requests


def get_html_from_url(url):
    return requests.get(url).text



def main():
    url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    urltext = get_html_from_url(url)
    print(urltext)

if __name__ == "__main__":
    main()