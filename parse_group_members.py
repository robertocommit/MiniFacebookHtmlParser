import pandas as pd
from bs4 import BeautifulSoup
results = []
f = open("input.html", "r")
soup = BeautifulSoup(f, 'html.parser')
people = soup.findAll("div", {"class": ["ue3kfks5", "pw54ja7n", "uo3d90p7"]})
for i in range(0, len(people)):
    detail = people[i].findAll("div", {"class": ["qzhwtbm6", "knvmm38d"]})
    if len(detail) > 0:
        name = detail[0].getText() 
        joined = detail[1].getText() 
        work = detail[2].getText()
        temp_url = detail[0].find("a")
        if temp_url:
            url = temp_url.attrs["href"]
        else:
            url = ""
        results.append([name, joined, work, url])
output = pd.DataFrame(results)
output.to_csv('output.csv')
