from bs4 import BeautifulSoup
import requests 
import json

url = 'https://www.futbin.com/popular'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml',)
name = soup.find_all('li', class_="popular-box")
rank = 1
player_stats_dict = {}
for row in name:
    pid = row['data-site-id']
    url = f"https://www.futbin.com/22/getTp?pid={pid}&type=player"
    response = requests.request("GET", url,)
    r = response.json()['data']['g']
    _ = r[9], r[18], r[10], r[3], r[4], r[5], r[6], r[7], r[8]
    name, rat,pos ,pac ,sho ,pas, dri, defence ,phy = _
    player_stats_dict[rank] = {name : {"Rating" : rat, "Position" : pos, "Pacing": pac, "Shot": sho, "Pas" : pas, "Dribble" : dri, "Defence" : defence, "Physical" : phy }}
    rank += 1
    togo = 100 - rank
    print (f"Players left : {togo} ")
with open('players.json', 'w') as fp:
    json.dump(player_stats_dict, fp, indent = 4 ,)
print(f"Players have been added to the 'Players.json file!") 