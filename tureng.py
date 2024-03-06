from bs4 import BeautifulSoup
import requests 

def tureng(input):

    s = requests.get(f"https://tureng.com/tr/turkce-ingilizce/{input}", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})

    soup = BeautifulSoup(s.content, "lxml")
    wordstr = soup.find_all("td", attrs={"class": "tr ts"})
    wordstd = soup.find("td", attrs={"class": "rc0 hidden-xs"})
    
    for index1 in wordstd:
        for index in dict(wordstr[:5]):
            print(index.text)

tureng("cool")
