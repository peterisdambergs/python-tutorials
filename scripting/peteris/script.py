import os, requests

from bs4 import BeautifulSoup


def get_html_from_url(url):
    return requests.get(url).text


def get_formatted_article(raw_article, root_url, category, num):
    link = raw_article.a.get('href')
    content, date = get_article_content_and_date(link)
    name = raw_article.get_text()
    image = raw_article.img.get("src")
    path = os.path.join(category, f"{num}.html")

    return {"name": name, "link": link, "category": category, "category_link": root_url+category,
            "date": date, "image": image, "path": path, "content": content}


def get_article_content_and_date(link):
    html = get_html_from_url(link)
    soup = BeautifulSoup(html, "lxml")

    raw_sections = soup.find("main").find("main").find_all("section")
    content = "\n".join([raw_section.text for raw_section in raw_sections])

    date = soup.find("time").get_text()[:10]

    return content, date


def get_articles(root_url, category, article_count):
    html = get_html_from_url(root_url+category)
    soup = BeautifulSoup(html, "lxml")

    raw_articles = soup.find_all("article")
    articles = []

    for num, raw_article in enumerate(raw_articles, start=1):
        article = get_formatted_article(raw_article, root_url, category, num)
        articles.append(article)
        if article_count == num: break

    return articles


def create_toc(article_list, toc_name):
    with open(toc_name, "w", encoding="utf-8") as f:
        f.write("<h1>Table of Contents</h1>\n")
        for article in article_list:
            date = article.get("date")
            category = f"<a href={article.get('category_link')}>{article.get('category')}</a>"
            name = f"<a href={article.get('path')}>{article.get('name')}</a>"
            f.write(f"<p>{date} [{category}] {name}</p>\n")


def create_article_dirs(article_dict):
    for category in article_dict:
        if not os.path.exists(category):
            os.mkdir(category)


def create_formatted_articles(article_dict):
    for category in article_dict:
        for article in article_dict.get(category):
            with open(article.get('path'), "w", encoding="utf-8") as f:
                f.write(f"<a href='{article.get('link')}'><img src={article.get('image')} alt='Text'></a>")
                f.write(f"<h1><a href='{article.get('link')}'>{article.get('name')}</a></h1>")
                f.write(f"<p>{article.get('content')}</p>")
                f.write(f"<p>{article.get('date')}</p>")
                f.write(f"<a href='..//toc.html'>Go Back!</a>")


def main():
    categories = ["biznesa_vide", "bankas_un_finanses", "tehnologijas", "nekustamais-ipasums", "pasaule"]
    delfi_categories = ["Ekonomika", "Finanses", "Tehnologijas", "Nekustamais Ipasums", "Pasaule"]
    root_url = "https://www.delfi.lv/bizness/"

    # article_dict = {category: get_articles(root_url, category, 2) for category in categories}
    article_list = []
    for category in categories:
        article_list.extend(get_articles(root_url, category, 2))

    create_toc(article_list, "toc.html")
    # create_article_dirs(article_dict)
    # create_formatted_articles(article_dict)

    # for element in article_list:
    #     print(element)


if __name__ == "__main__":
    main()
