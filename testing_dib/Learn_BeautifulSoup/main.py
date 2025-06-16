from bs4 import BeautifulSoup
import requests


def main():
    print("Hello from learn-beautifulsoup!")
    url = "https://www.scrapethissite.com/pages/forms/"

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup.prettify())
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


if __name__ == "__main__":
    main()
