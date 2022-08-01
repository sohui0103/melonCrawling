import requests
from bs4 import BeautifulSoup
import json

if __name__ == "__main__":
    RANK = 100  # 랭킹 100위까지

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    url = "https://www.melon.com/chart/index.htm"
    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.text, 'html.parser')

    # html = response.text
    # parse = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all("div", {"class": "ellipsis rank01"})
    songs = soup.find_all("div", {"class": "ellipsis rank02"})

    title = []
    song = []

    for t in titles:
        title.append(t.find('a').text)

    for s in songs:
        song.append(s.find('span', {"class": "checkEllipsis"}).text)

    for i in range(RANK):
        print('%3d위: %s - %s' % (i+1, title[i], song[i]))

    chartlist = []
    for c in range(RANK):
        chartlist.append('%3d위: %s - %s' % (c+1, title[c], song[c]))
        # chartlist.append(title[c] + " - " + song[c])


rank_file = open("rankresult.txt", "a")

# with open('artist.json', 'w', encoding='UTF-8-sig') as file:
# file.write(json.dumps(title, ensure_ascii=False))

# with open('song.json', 'w', encoding='UTF-8-sig') as file:
# file.write(json.dumps(title, ensure_ascii=False))

with open('chartlist.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(chartlist, ensure_ascii=False))
