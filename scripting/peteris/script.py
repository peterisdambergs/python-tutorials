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


def main():
    html = get_html_from_url("https://www.delfi.lv/bizness/biznesa_vide")
    soup = BeautifulSoup(html, "lxml")

    raw_articles = soup.find_all("article")

    for num, raw_article in enumerate(raw_articles):
        article = get_formatted_article(raw_article, "bizness", num+1)
        print(article)
        if num == 0: break


if __name__ == "__main__":
    main()
