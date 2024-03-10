import os, re, requests

from bs4 import BeautifulSoup


def get_html_from_source(url="https://www.delfi.lv/bizness/biznesa_vide", file_name="source.html"):
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            r = requests.get(url)
            f.write(r.text)

    with open(file_name, "r", encoding="utf-8") as f:
        html = f.read()

    return html


def main():
    html = get_html_from_source()
    soup = BeautifulSoup(html, "lxml")

    for article in soup.find_all("article"):
        print(article)


if __name__ == "__main__":
    main()
