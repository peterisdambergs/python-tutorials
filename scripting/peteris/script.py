import os, requests

from bs4 import BeautifulSoup


def get_html_from_source(url, file_name):
    if not os.path.exists(file_name):
        response = requests.get(url)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(response.text)

    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()


def get_formatted_article(raw_article, category, num):

    article = {
        "text": raw_article.get_text(),
        "link": f"https://delfi.lv{raw_article.a.get('href')}",
        "image": raw_article.img.get("src"),
        "path": os.path.join(os.getcwd(), category, f"{num}.html")
    }

    return article


def main():
    html = get_html_from_source("https://www.delfi.lv/bizness/biznesa_vide", "source.html")
    soup = BeautifulSoup(html, "lxml")

    raw_articles = soup.find_all("article")

    for num, raw_article in enumerate(raw_articles):
        article = get_formatted_article(raw_article, "bizness", num+1)
        print(article)






if __name__ == "__main__":
    main()
