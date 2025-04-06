# CTRL + SHIFT + P
# Type: “Python: Select Interpreter”
# Pick the interpreter that matches your Pipenv virtual environment.

# Or run from terminal "python 10_popular_pyton_packages/7_web_scraping.py"

from bs4 import BeautifulSoup
import requests

# Our goal is to return stackoverflow question titles with a number of votes
response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")
for question in questions:
    print(question.select_one(".s-link").get_text())
    print(question.select_one(".s-post-summary--stats-item-number").get_text())
