import requests
from bs4 import BeautifulSoup
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
        ret.append((i['href']))
    return ret

    # image_list = soup.find(
    #     "div", {"class": "GalleryItems-module__searchContent___DbMmK"})
    # print(image_list)
    # for i in gallery_list:
    #     ret.append((i['src']))
    # return ret


def main():
    amir = get_amirkhan("https://www.gettyimages.in/photos/aamir-khan-actor")
    head = "https://www.gettyimages.in"
    for i in amir:
        print("---------------", head+i,
              "----------------")


if __name__ == "__main__":
    main()
