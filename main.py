import requests
from bs4 import BeautifulSoup, Comment
import pandas as pd

# Define the URL of the Bilibili video from which we want to scrape the comments
url = "https://www.bilibili.com/video/BV1Jy4y1M7sy/?spm_id_from=333.337.search-card.all.click&vd_source=605f2edb3daf8b83e497c1e9eedba204"

# Send an HTTP GET request to the URL and retrieve the HTML response
html = requests.get(url).text


# Parse the HTML response and extract the comments
soup = BeautifulSoup(html, "html.parser") 

comments = soup.find_all("div", class_="reply-list")

# Extract the text of each comment
comment_list = []
for comment in comments:
    comment_text = comment.text
    comment_list.append(comment_text)

# Store the scraped comments in a tabular format
df = pd.DataFrame({"Comment": comment_list})
df.to_csv("bilibili_comments.csv", index=False)
