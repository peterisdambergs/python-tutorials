import os, requests


def get_html_from_source(url="https://www.delfi.lv/bizness/biznesa_vide", file_name="source.html"):
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            r = requests.get(url)
            f.write(r.text)

    with open(file_name, "r", encoding="utf-8") as f:
        html = f.read()

    return html


def get_articles_from_html(html):
    articles = html.replace("<article", "</article>").replace("headline--responsive ", "").split("</article>")[1:-1]
    return [article for article in articles if 'itemtype="http://schema.org/NewsArticle"' in article]


def main():
    html = get_html_from_source()
    articles = get_articles_from_html(html)

    for article in articles:
        print(article)


if __name__ == "__main__":
    main()
