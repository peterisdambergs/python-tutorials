import os, re, requests

from bs4 import BeautifulSoup


def get_html_from_source(url, file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            r = requests.get(url)
            f.write(r.text)

    with open(file_name, "r", encoding="utf-8") as f:
        html = f.read()

    return html


def create_article_file_path_based_on_article_name_and_category(name, category):
    forbidden_char_pattern = r"[^a-zA-Z0-9 ()_\-,.*]+"
    file_name = re.sub(forbidden_char_pattern, "", name)[:35] + "***.md"
    print(os.path.join(os.getcwd(), category, file_name).replace("\\", "\\\\"))
    return os.path.join(os.getcwd(), category, file_name).replace("\\", "\\\\")


def get_formatted_article(article, category):
    name = article.get_text()

    article = {
        "name": name,
        "link": f"https://delfi.lv{article.a.get('href')}",
        "img": article.img.get("src"),
        "file_path": create_article_file_path_based_on_article_name_and_category(name, category)
    }

    return article


def main():
    root_url = "https://www.delfi.lv/bizness/"

    category_dict = {
        "biznesa_vide": "Economy",
        "bankas_un_finanses": "Finance",
        "tehnologijas": "Tech",
        "nekustamais-ipasums": "Real Estate",
        "pasaule": "World"
    }

    with open("articles.md", "w", encoding="utf-8") as f:
        f.write("# Articles\n")
        for category in category_dict:
            f.write(f"### {category_dict.get(category)}\n")

            if not os.path.exists(category): os.mkdir(category)

            html = get_html_from_source(f"{root_url}/{category}", f"{category}.html")
            soup = BeautifulSoup(html, "lxml")

            for num, article in enumerate(soup.find_all("article")):
                formatted_article = get_formatted_article(article, category)
                f.write(f"- [{formatted_article.get('name')}]({formatted_article.get('file_path')})\n")
                if num == 4: break


if __name__ == "__main__":
    main()
