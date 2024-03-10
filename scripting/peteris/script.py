import os, requests

from bs4 import BeautifulSoup


def get_html_from_source(url, file_name):
    if not os.path.exists(file_name):
        response = requests.get(url)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(response.text)

    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()


def main():
    html = get_html_from_source("https://www.delfi.lv/bizness/biznesa_vide", "source.html")
    soup = BeautifulSoup(html, "lxml")

    articles = soup.find_all("article")
    for article in articles:
        print(article)


if __name__ == "__main__":
    main()
