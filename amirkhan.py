import requests
from bs4 import BeautifulSoup


def get_amirkhan(site_url):
    ret = []
    r = requests.get(site_url)
    soup = BeautifulSoup(r.content, features="html.parser")
    image_list = soup.find(
        "img", {"class": "MosaicAsset-module__thumb___yvFP5"})


def crawl():

    amir = get_amirkhan("https://www.gettyimages.in/photos/aamir-khan-actor")
    for i in amir:
        print("-----------------------------------------", i,
              "-----------------------------------------")


if __name__ == "__main__":
    crawl()
