import requests
from bs4 import BeautifulSoup
import pandas


page_input = input("Page: ")
page = requests.get(page_input)

page_content = BeautifulSoup(page.content, 'html.parser')

main_tag_input = input("Main Tag: ")
if ("[id] " in main_tag_input):
    main_tag = page_content.find(id= ''.join(str(elem) for elem in list(main_tag_input)[5::]))
else:
    main_tag = page_content.find(class_= main_tag_input)

tags = []

tag_input = ""

while (tag_input != "quit"):
    tag_input = input("Enter Tag: ")
    