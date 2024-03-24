import os, re, requests

from bs4 import BeautifulSoup


def get_html(url):
    return requests.get(url).text


def create_article_file_path(article_name, article_category):
    forbidden_char_pattern = r"[^a-zA-Z0-9 ()_\-,.*]+"
    file_name = re.sub(forbidden_char_pattern, "", article_name)[:35] + ".html"
    return os.path.join(article_category, file_name)


def get_formatted_article(raw_article, category):
    name = raw_article.get_text()

    article = {
        "name": name,
        "url": f"https://delfi.lv{raw_article.a.get('href')}",
        "img": raw_article.img.get("src"),
        "file_path": create_article_file_path(name, category)
    }

    return article


def get_raw_articles_by_category(root_url, category):
    html = get_html(f"{root_url}/{category}")
    category_soup = BeautifulSoup(html, "lxml")
    return category_soup.find_all("article")


def create_article_file(article, toc_file_name):
    html = get_html(article.get("url"))
    article_soup = BeautifulSoup(html, "lxml")

    with open(article.get("file_path"), "w", encoding="utf-8") as f:
        f.write(f"<a href='{article.get('url')}'><img src={article.get('img')}></img></a>\n")
        f.write(f"<h1><a href='{article.get('url')}'>{article.get('name')}</a></h1>\n")

        for section in article_soup.main.main.find_all("section"):
            f.write(f"<p>{section.get_text()}</p>\n")

        f.write(f"<h3><a href='..\\{toc_file_name}.html'>Go Back</a></h3>\n")


def create_articles(root_url, category_dict, toc_file_name, article_count=5):
    with open(f"{toc_file_name}.html", "w", encoding="utf-8") as f:
        f.write("<h1>Articles</h1>\n")
        for category in category_dict:
            if not os.path.exists(category): os.mkdir(category)

            f.write(f"<h3>{category_dict.get(category)}</h3>\n")
            f.write("<ul>\n")

            raw_articles = get_raw_articles_by_category(root_url, category)
            for num, raw_article in enumerate(raw_articles):
                article = get_formatted_article(raw_article, category)
                create_article_file(article, toc_file_name)

                f.write(f"<li><a href='{article.get('file_path')}'>{article.get('name')}</a></li>\n")
                if num + 1 == article_count: break

            f.write("</ul>\n")


def main():
    root_url = "https://www.delfi.lv/bizness/"

    category_dict = {
        "biznesa_vide": "Economy",
        "bankas_un_finanses": "Finance",
        "tehnologijas": "Tech",
        "nekustamais-ipasums": "Real Estate",
        "pasaule": "World"
    }

    create_articles(root_url, category_dict, "articles", 3)


if __name__ == "__main__":
    main()
