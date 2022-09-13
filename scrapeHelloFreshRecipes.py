import json
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


def scrape_recipies(html):
    bs = BeautifulSoup(html, 'html.parser')
    recipe_cards_list = bs.select("div[data-test-id^='recipe-card']> div > a")
    recipe_links = []
    for element in recipe_cards_list:
        recipe_links.append(element.attrs['href'])

    recipe_link_result = open("recipes.json", "w")
    recipe_link_result.write(json.dumps(recipe_links))
    recipe_link_result.close()



def main():
    html = open("./source.html", "r")
    scrape_recipies(str(html.read()))
    html.close()


if __name__ == '__main__':
    main()
