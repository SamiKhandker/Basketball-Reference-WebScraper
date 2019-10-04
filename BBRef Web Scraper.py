from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# NBA season to be analyzed
year = 2019
# URL page to be scraped
url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)
# HTML from the URL
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# use findALL() to get the column headers
soup.findAll('tr', limit=2)
# use getText()to extract the text needed into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
# exclude the first column as the ranking order from Basketball Reference is not needed for the analysis
headers = headers[1:]

print(headers)

# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

stats = pd.DataFrame(player_stats, columns = headers)
print(stats.head(10))
