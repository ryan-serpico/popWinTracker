from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.basketball-reference.com/coaches/popovgr99c.html'


def winScraper(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text.encode(
        'utf-8').decode('ascii', 'ignore'), 'lxml')
    winTotal = soup.select('.thead > td:nth-child(6)')[0]
    return int(winTotal.get_text())


def textGenerator(currentWinCount):
    s = '<div style = "display: grid; place-items: center"><p> Greg Popovich is <span style = "color: green" > ' + \
        str(1336 - currentWinCount) + \
        ' wins </span > away from becoming the all-time leader in regular season wins for an NBA coach.</p></div>'
    return s


currentWinCount = winScraper(url)
text = textGenerator(currentWinCount)

with open('popovichTracker.csv', 'w', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow([text])
