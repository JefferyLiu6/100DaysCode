from bs4 import BeautifulSoup
import lxml

with open('100DaysCode/Day45/bs4-start/website.html') as file:
    contents = file.read()

#print(contents)

soup = BeautifulSoup(contents, "html.parser")
ccc = soup.find_all(name = "p")
for tag in ccc:
    print(tag.get("href"))