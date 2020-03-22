import requests
from bs4 import BeautifulSoup

# Downloads the requested page
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# parse the downloaded document
soup = BeautifulSoup(page.content, 'html.parser')

# prints the formatted contents of the page
#print(soup.prettify())

# Move through the page from top level of HTML to bottom level using
# .children property
# .children returns iterator object so must parse to list
#print(list(soup.children))

# Of the children, we want the 3rd element since it is a Tag object,
# first two are simply the Doctype object and NavigableString object
# Tag obj allows us to navigate the HTML so we can select the html tag
# and take its children by using the 3rd element
html = list(soup.children)[2]

# we can continuously use the .chilren property to access deeper layers
#print (list(html.children))

body = list(html.children)[3]

#print(list(body.children)) 

# now get the p tag
p = list (body.children)[1]

# and now we can isolate the text using .get_text
#print(p.get_text())

# now a faster way to do this is to use the find methods
# find all instances of the p tag -> use findAll('p')[i]
# where i is the index of the text you want
#print(soup.findAll('p')[0].get_text())

# if you only want to find the first occurrence, just use find

#print(soup.find('p').get_text())

# We can also bring in css and use class and id
# if you want to find all paragraphs with the class 'outer'
# do print(soup.findAll('p', class_="outer"))
# using class_
# or simply
# print(soup.findAll('p.outer)) where .[str] is the class

# similarly for id, do
#print(soup.findAll(id = "name"))
# or simply
# print(soup.findAll('p#name)) where #[str] is the id

# so we can actually target the selectors using the select method

#print(soup.select("p.name") to select all p tags with class of name

