import requests
from bs4 import BeautifulSoup

base_url = 'https://ani.gamer.com.tw/animeList.php?sort=2&page='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}
start_page = 1
end_page = 5

for page in range(start_page, end_page + 1):
    url = base_url + str(page)
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        print(f'請求成功：{r.status_code}')
        soup = BeautifulSoup(r.text, 'html.parser')
        anime_items = soup.select('.theme-list-block')

        # 依序針對每個動畫區塊擷取資料
        for anime_item in anime_items:
            anime_name_elements = anime_item.select('.theme-name')
            for element in anime_name_elements:
                anime_name = element.text.strip()
                
            anime_number_elements = anime_item.select('.theme-number:not(.theme-info-block)')
            for element in anime_number_elements:
                anime_watch = element.text.strip()   
                print(anime_name)                 
                print(anime_watch)
                print('----------')
    else:
        print(f'請求失敗：{r.status_code}')