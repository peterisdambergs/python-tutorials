import os, requests

from bs4 import BeautifulSoup


def get_html_from_url(url):
    html = requests.get(url).text
    return html


def get_formatted_article(raw_article, category, num):
    link = f"https://delfi.lv{raw_article.a.get('href')}"
    article = {
        "name": raw_article.get_text(),
        "link": link,
        "image": raw_article.img.get("src"),
        "path": os.path.join(category, f"{num}.html"),
        "content": get_article_content(link)
    }

    return article


def get_article_content(link):
    html = get_html_from_url(link)
    soup = BeautifulSoup(html, "lxml")

    raw_sections = soup.find("main").find("main").find_all("section")
    return "\n".join([raw_section.text for raw_section in raw_sections])


def get_articles(root_url, category, article_count):
    html = get_html_from_url(f"{root_url}/{category}")
    soup = BeautifulSoup(html, "lxml")

    raw_articles = soup.find_all("article")
    articles = []

    for num, raw_article in enumerate(raw_articles, start=1):
        article = get_formatted_article(raw_article, category, num)
        articles.append(article)
        if num == article_count: break

    return articles


def main():
    root_url = "https://www.delfi.lv/bizness"
    categories = ["biznesa_vide", "bankas_un_finanses", "tehnologijas", "nekustamais-ipasums", "pasaule"]

    article_dict = {}

    for category in categories:
        article_dict[category] = get_articles(root_url, category, 5)

    print(article_dict)


if __name__ == "__main__":
    main()
