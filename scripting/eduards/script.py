import os, re, requests

from bs4 import BeautifulSoup

from PIL import Image


def get_html_from_source(url="https://www.delfi.lv/bizness/biznesa_vide", file_name="source.html"):
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            r = requests.get(url)
            f.write(r.text)

    with open(file_name, "r", encoding="utf-8") as f:
        html = f.read()

    return html


def get_text_img_from_article(article):
    text = article.get_text()
    link = f"https://delfi.lv{article.a.get('href')}"
    img = article.img.get("src")

    return text, link, img


def create_file_from_article(dir, file_name, article):
    text, link, img = get_text_img_from_article(article)

    if not os.path.exists(dir):
        os.makedirs(dir)

    with open(os.path.join(dir, file_name), "w", encoding="utf-8") as f:
        f.write(f"Text: {text}\n")
        f.write(f"Link: {link}\n")
        f.write(f"Image: {img}\n")


def main():
    html = get_html_from_source()
    soup = BeautifulSoup(html, "lxml")

    for num, article in enumerate(soup.find_all("article")):
        create_file_from_article("articles", f"article_{num+1}.txt", article)


if __name__ == "__main__":
    main()
