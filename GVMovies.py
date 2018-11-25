#Please follow instructions on how to use selenium from link below
#https://selenium-python.readthedocs.io/installation.html

from selenium import webdriver
from bs4 import BeautifulSoup
import requests

browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
url = "https://www.gv.com.sg/GVHome#/"
browser.get(url) #navigate to the page

innerHTML = browser.execute_script("return document.body.innerHTML")

python_button = browser.find_element_by_xpath("//img[@src='https://www.gv.com.sg/media/imagesresize/img6396.jpg']/parent::a")
python_button.click()

print(browser.execute_script("return document.body.innerHTML"))

python_button = browser.find_element_by_css_selector('li.ng-scope>button')
python_button.click()

soup = BeautifulSoup(innerHTML,"html.parser")


results = soup.find("div",{"id": "movieTabs"})

links = soup.findAll("div",{"ng-repeat": "movie in nowShowingFilms"})

for item in links:
    caption = item.find("div",{"class": "caption"})
    caption_name = caption.find("h5").text

    #print(caption_name)
