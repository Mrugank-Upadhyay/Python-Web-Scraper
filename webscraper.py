import requests
from bs4 import BeautifulSoup

# Downloads the requested page
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XoGTdohKhPY")

# parse the downloaded document
page_content = BeautifulSoup(page.content, 'html.parser')

seven_day = page_content.find(id="seven-day-forecast-container")

# select all items with the class period-name inside an item tag 
# with the class tombstone-container
period_tags = seven_day.select(".tombstone-container .period-name")

periods = [pt.get_text() for pt in period_tags]

short_desc = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]

temps = [temp.get_text() for temp in seven_day.select(".tombstone-container .temp")]

desc = [description["title"] for description in seven_day.select(".tombstone-container img")]

print(periods)
print(short_desc)
print(temps)
print(desc)