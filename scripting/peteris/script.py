import os, requests

from bs4 import BeautifulSoup


def get_html_from_source(url, file_name):
    if not os.path.exists(file_name):
        response = requests.get(url)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(response.text)

    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()


def get_link_image_text_from_article(article):
    link = f"https://delfi.lv{article.a.get('href')}"
    image = article.img.get("src")
    text = article.get_text()

    return link, image, text


def main():
    html = get_html_from_source("https://www.delfi.lv/bizness/biznesa_vide", "source.html")
    soup = BeautifulSoup(html, "lxml")

    articles = soup.find_all("article")
    # for article in articles:
    #     print(article)

    for article in articles:
        link, image, text = get_link_image_text_from_article(article)
        print(text)
        print(link)
        print(f"{image}\n")


if __name__ == "__main__":
    main()
