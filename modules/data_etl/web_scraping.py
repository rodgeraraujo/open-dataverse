from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

def pageScrapig(page_url):
    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    # print(page_soup)

    containers = page_soup.find("a", {"class": "heading"})
                          .findParent("span", data-format={"json"})


    print(containers)

page_url = "https://dados.ifpb.edu.br/dataset/alunos"
pageScrapig(page_url)
