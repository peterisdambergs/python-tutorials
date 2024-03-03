import os, requests


def get_html_from_source(url, file_name):
    if not os.path.exists(file_name):
        response = requests.get(url)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(response.text)

    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()


def main():

    html = get_html_from_source("https://www.delfi.lv/bizness/biznesa_vide", "source.html")
    print(html)



if __name__ == "__main__":
    main()