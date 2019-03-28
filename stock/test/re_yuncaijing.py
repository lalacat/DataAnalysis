import requests
from bs4 import BeautifulSoup
from lxml import etree

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
cer = "./cer.cer"

r = requests.get(
    "https://www.yuncaijing.com/dock/1456/details.html", headers=header, verify=cer
)
r.encoding = "utf-8"
s = BeautifulSoup(r.content, "html.parser")
print(s)
