from bs4 import BeautifulSoup
import requests
url = "https://www.scrapethissite.com/pages/simple"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

countries = soup.find_all("div", class_="country")
print(len(countries))

for country in countries:
    name = country.find("h3", class_="country-name").text.strip()
    capital = country.find("span", class_="country-capital").text.strip()
    population = country.find("span", class_="country-population").text.strip()
    print(f"Country: {name}, Capital: {capital}, Population: {population}")

import csv

with open("countries.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Capital", "Population", "Area"])
    for country in countries:
        name = country.find("h3", class_="country-name").text.strip()
        capital = country.find("span", class_="country-capital").text.strip()
        population = country.find("span", class_="country-population").text.strip()
        area = country.find("span", class_="country-area").text.strip()
        writer.writerow([name, capital, population, area])