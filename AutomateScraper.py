import requests
from bs4 import BeautifulSoup
import pandas


page_input = input("Page: ")
page = requests.get(page_input)

page_content = BeautifulSoup(page.content, 'html.parser')

main_tag_input = input("Main Tag: ")
main_tag = page_content.find(main_tag_input)

tags = []
