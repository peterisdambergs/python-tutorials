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


def create_toc(article_dict):
    with open("toc.html", "w", encoding="utf-8") as f:
        f.write("<h1>Table of Contents</h1>\n")
        for category in article_dict:
            f.write(f"<h3>{category}</h3>\n<ol>\n")
            for article in article_dict.get(category):
                f.write(f"<li><a href='{article.get('path')}'>{article.get('name')}</a></li>\n")
            f.write("</ol>\n")


def main():
    root_url = "https://www.delfi.lv/bizness"
    category_dict = {
        "biznesa_vide": "Economy",
        "bankas_un_finanses": "Finance",
        "tehnologijas": "Tech",
        "nekustamais-ipasums": "Real Estate",
        "pasaule": "World"
    }

    article_dict = {category: get_articles(root_url, category, 3) for category in category_dict}
    create_toc(article_dict)


if __name__ == "__main__":
    main()
