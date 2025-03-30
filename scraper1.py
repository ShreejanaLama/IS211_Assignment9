# wikipedia_superbowl.py
# This code get data from Wikipedia about Super Bowl champions
# It shows top 20 games with date, winning team, score, and losing team

import requests  # this helps us open web page
from bs4 import BeautifulSoup  # this helps us read and find data from the page
import re  # this helps us clean up the text

# This is the website link where Super Bowl data is
url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
response = requests.get(url)  # get the web page
soup = BeautifulSoup(response.content, "html.parser")  # change page to something we can read

# Get all the tables in the page that look like Wikipedia tables
tables = soup.find_all("table", class_="wikitable")

# We pick the second table, because first one is not what we need
table = tables[1] if len(tables) >= 2 else None

# If table not found, stop the code and show message
if not table:
    print("Table not found.")
    exit()

# This function clean the text from the table
def clean_text(text):
    text = re.sub(r'\([^)]*\)', '', text)     # remove anything inside ( )
    text = re.sub(r'\[[^\]]*\]', '', text)    # remove anything like [1], [W]
    text = re.sub(r'[a-zA-Z]\s*$', '', text)  # remove last letter like N, A
    return text.strip()  # remove extra space

# Print the column titles (header) in nice format
print(f"{'Date':<15} {'Winning Team':<25} {'Score':<7} {'Losing Team':<25}")
print("-" * 75)  # print a line

# Start counting how many rows we show
count = 0

# Look at each row in the table (skip the first one because it is title)
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")  # get the columns from the row

    # If the row has 5 or more columns, we take the data
    if len(cols) >= 5:
        date = cols[1].text.strip().split("(")[0].strip()  # get only the date
        winner = clean_text(cols[2].text.strip())  # clean the winner team name
        score = cols[3].text.strip()  # get the score
        loser = clean_text(cols[4].text.strip())  # clean the loser team name

        # print the data in good format
        print(f"{date:<15} {winner:<25} {score:<7} {loser:<25}")
        count += 1  # add 1 to count

        # stop after 20 rows
        if count == 20:
            break
