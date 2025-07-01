import requests
import bs4

prefix = "https://bc.godfat.org"
seed = input("Please input seed: ")
event = input("Please input event code: ")
last = input("Please input last code: ")
lang = "tw"
count = "5"

url = f"{prefix}/?seed={seed}&event={event}&last={last}&lang={lang}&count={count}"

web = requests.get(url)
soup = bs4.BeautifulSoup(web.text, "html.parser")

cat = soup.find_all('a')

print(cat)