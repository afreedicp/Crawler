import requests
from bs4 import BeautifulSoup
import wget
import os
header = {
    'User-Agent': 'Mozilla/5.0 (MacintoshIntel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def get_amirkhan(site_url):
    ret = []
    r = requests.get(url=site_url, headers=header)
    soup = BeautifulSoup(r.content, features="html.parser")
    gallery = soup.find(
        "div", {"class": "GalleryItems-module__searchContent___DbMmK"})
    link = gallery.find_all("a")
    for i in link:
        ret.append((i.text, i['href']))
    return ret


def download_amirkhan(site_url):
    r = requests.get(url=site_url, headers=header)
    soup = BeautifulSoup(r.content, features="html.parser")
    gallery = soup.find(
        "img", {"class": "AssetCard-module__image___dams4"})
    thisimage = gallery['src']
    print(thisimage)
    return thisimage


def main():
    amirlink = get_amirkhan(
        "https://www.gettyimages.in/photos/aamir-khan-actor")
    head = "https://www.gettyimages.in"
    os.mkdir("images")
    for name, link in amirlink:
        wget.download(download_amirkhan(head+link))


if __name__ == "__main__":
    main()
