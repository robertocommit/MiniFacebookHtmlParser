import pandas as pd
from bs4 import BeautifulSoup
results = []
f = open("input.html", "r")
soup = BeautifulSoup(f, 'html.parser')
people = soup.findAll("div", {"class": ["ue3kfks5", "pw54ja7n", "uo3d90p7"]})
for i in range(1, 100):
    detail = people[i].findAll("div", {"class": ["qzhwtbm6", "knvmm38d"]})
    name = detail[0].getText() 
    joined = detail[1].getText() 
    work = detail[2].getText()
    results.append([name, joined, work])
output = pd.DataFrame(results)
output.to_csv('output.csv')
