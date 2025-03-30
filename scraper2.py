# country_population.py
# This program gets the top 25 most populated countries from Wikipedia.
# It shows the country name, population, percent of world population, date, and source.
# Website: https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population

import requests  # To get the web page
from bs4 import BeautifulSoup  # To read and understand the HTML
import re  # To remove footnotes like [1], [a], etc.

# Step 1: Go to the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
response = requests.get(url)  # Ask the website for the page
soup = BeautifulSoup(response.content, "html.parser")  # Use BeautifulSoup to read the page

# Step 2: Find the population table
table = soup.find("table", {"class": "wikitable"})  # Look for a table with class "wikitable"

# Step 3: Print column headers
print(f"{'Country':<35} {'Population':<18} {'% of World':<12} {'Date':<15} {'Source'}")
print("-" * 110)  # Print a line under the header

# Step 4: Go through each row in the table
count = 0
for row in table.find_all("tr")[1:]:  # Skip the first row (header row)
    cols = row.find_all(["th", "td"])  # Get each column in the row (some are <th>, some <td>)

    if len(cols) >= 5:  # Make sure there are enough columns
        # Get text and remove extra things like [1], [note], etc.
        country = re.sub(r"\[.*?\]", "", cols[0].text.strip())  # Column 0: Country name
        population = re.sub(r"\[.*?\]", "", cols[1].text.strip())  # Column 1: Population
        percent = re.sub(r"\[.*?\]", "", cols[2].text.strip())  # Column 2: Percent of world
        date = re.sub(r"\[.*?\]", "", cols[3].text.strip())  # Column 3: Date
        source = re.sub(r"\[.*?\]", "", cols[4].text.strip())  # Column 4: Source

        # Skip the first row if it says "World" (we only want countries)
        if country.lower() == "world":
            continue

        # Print the clean result
        print(f"{country:<35} {population:<18} {percent:<12} {date:<15} {source}")
        
        count += 1  # Count the country
        if count == 25:  # Stop when we have 25 countries
            break
